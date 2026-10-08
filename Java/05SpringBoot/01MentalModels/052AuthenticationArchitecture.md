# Spring Security Authentication: The Mental Model

This is your reference guide for Spring Security's authentication architecture. Use this when you feel foggy on how the different components fit together.

---

## 1. The Core Components (The "Security Department" Analogy)

Understanding *why* these exist is more important than memorizing their names. Spring uses these abstractions to support many authentication types (JWT, LDAP, OAuth2, etc.) without hardcoding them into one giant class.

*   **`AuthenticationManager` (The Reception/Coordinator):** 
    *   *Role:* Takes the initial authentication request and routes it to the correct provider.
    *   *Motto:* "Someone wants to authenticate. I will route their request appropriately."
*   **`AuthenticationProvider` (The Specialized Security Officer):**
    *   *Role:* Performs the actual authentication logic for a specific mechanism (e.g., `DaoAuthenticationProvider` for username/password).
    *   *Motto:* "I know how to verify this particular type of credential."
*   **`UserDetailsService` (The Employee Directory):**
    *   *Role:* Loads user information from your storage (like a database) based on a username/email.
    *   *Motto:* "Give me the information about this employee."
*   **`PasswordEncoder` (The Credential Verifier):**
    *   *Role:* Hashes raw passwords and checks if submitted passwords match stored hashes.
    *   *Motto:* "Does this supplied password match the stored password representation?"
*   **`Authentication` (The ID Badge / State Object):**
    *   *Role:* Represents the authentication attempt (unverified) or the successful result (verified). 
    *   *Motto:* "This person has been authenticated as this user with these authorities."
*   **`SecurityContext` (The Building Roster):**
    *   *Role:* Holds the `Authentication` object for the current request.
    *   *Motto:* "This request is currently associated with this authenticated identity."

---

## 2. The `Authentication` Object (State Machine)

The `Authentication` object has two distinct states. It holds the **Principal** (Identity/Who), **Credentials** (Password), **Authorities** (Permissions like `ROLE_USER`, `ORDER_CREATE`), and an **Authenticated** boolean flag.

**State 1: Before Verification (The Request)**
*   `Principal` = khushal@example.com
*   `Credentials` = MyPassword123
*   `Authenticated` = **false**
*   *Meaning:* "Please authenticate this user using these credentials."

**State 2: After Verification (The Result)**
*   `Principal` = User 42 (Identity)
*   `Authorities` = ROLE_USER (Permissions for Authorization)
*   `Credentials` = [Hidden/Cleared]
*   `Authenticated` = **true**
*   *Meaning:* "This request has been successfully authenticated as User 42."

---

## 3. Data Representation: Domain User vs. Spring User

Your application's database `User` and Spring's `UserDetails` are **not the same thing**.

*   **Your Database `@Entity User`:** Contains domain data (id, email, password, firstName, address, createdAt).
*   **Spring's `UserDetails`:** Contains only what Spring Security needs (username, password, authorities, accountNonExpired, accountNonLocked, credentialsNonExpired, enabled).
*   **The Bridge:** You usually create an adapter (e.g., `CustomUserDetails` implementing `UserDetails`) that wraps your database `User`. This keeps security concerns from polluting your business domain.

---

## 4. Crucial Distinctions (What Components Do NOT Do)

When debugging, remember these strict separations of concerns:

1.  **`UserDetailsService` does NOT authenticate the password.** It ONLY loads the stored user data and returns it. 
2.  **`PasswordEncoder` does NOT find users or query the database.** It ONLY encodes or verifies (`matches()`) the raw password against the loaded hash.
3.  **`AuthenticationManager` does NOT query the database.** It ONLY coordinates and delegates to an `AuthenticationProvider`.
4.  **Database Connection:** Authentication doesn't magically access the DB. Your `UserDetailsService` implementation uses your standard data layer (e.g., `UserRepository` -> JPA/JDBC -> PostgreSQL).

---

## 5. The Step-by-Step Flow (Username / Password)

Trace this flow when trying to understand where a login request is failing:

1.  **Client POSTs** credentials (email + raw password).
2.  An **`Authentication` Request** object is created (`Authenticated = false`).
3.  **`AuthenticationManager`** receives it and asks: "Which provider handles this?"
4.  **`DaoAuthenticationProvider`** steps up to handle username/password auth.
5.  Provider calls **`UserDetailsService.loadUserByUsername("email")`**.
6.  Your code uses `UserRepository` to fetch the User from the **Database**.
7.  The database `User` is converted into a **`UserDetails`** object (containing the stored password hash and authorities).
8.  Provider passes the raw password and the stored hash to the **`PasswordEncoder.matches()`**.
9.  If it matches, the Provider creates a **New `Authentication` Object** (`Authenticated = true`, populated with Principal and Authorities).
10. This authenticated object is placed into the **`SecurityContext`**.

---

## 6. The Big Picture Architectures

### The Authentication Diagram
```text
                         LOGIN
                           │
                           ↓
                 Authentication Request
                           │
                           ↓
                AuthenticationManager
                           │
                           ↓
                AuthenticationProvider
                           │
                  ┌────────┴─────────┐
                  ↓                  ↓
          UserDetailsService    PasswordEncoder
                  │                  │
                  ↓                  │
             Database               │
                  │                  │
                  ↓                  │
             UserDetails             │
                  │                  │
                  └────────┬─────────┘
                           ↓
                  Authentication (authenticated=true)
                           │
                           ↓
                    SecurityContext
```

### The 3-Layer Application Architecture
1.  **HTTP Layer:** `Request` -> `Security Filter Chain`
2.  **Authentication Layer:** `AuthManager` -> `AuthProvider` -> `UserDetailsService` & `PasswordEncoder` -> `Database`