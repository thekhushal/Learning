# Lesson 6 — Spring Security's Authentication Architecture

This is one of the most important lessons so far.

You have already learned **what authentication is**. Now we are going to see how Spring Security breaks the authentication process into separate components.

You will encounter these names repeatedly in production code:

```text
Authentication
AuthenticationManager
AuthenticationProvider
UserDetailsService
UserDetails
PasswordEncoder
SecurityContext
```

The goal is not to memorize them.

The goal is to understand **why each one exists and how they work together**.

---

# 1. Start with the login problem

Suppose the client sends:

```http
POST /auth/login
Content-Type: application/json
```

```json
{
    "email": "khushal@example.com",
    "password": "MyPassword123"
}
```

Ultimately, Spring Security needs to answer:

> Is this user authenticated?

To answer that, it needs to:

1. Find the user.
2. Retrieve the stored password hash.
3. Compare the submitted password with the stored hash.
4. Determine whether authentication succeeded.
5. Create an authenticated representation of the user.
6. Make that authentication available to the rest of the request.

Spring Security separates these responsibilities.

---

# 2. The big picture

Here is the architecture we are going to understand:

```text
Login credentials
       │
       ↓
Authentication
       │
       ↓
AuthenticationManager
       │
       ↓
AuthenticationProvider
       │
       ├───────────────┐
       ↓               ↓
UserDetailsService  PasswordEncoder
       ↓               ↓
  UserDetails      Password verification
       │               │
       └───────┬───────┘
               ↓
       Authentication result
               │
               ↓
        SecurityContext
```

There are some nuances depending on the authentication mechanism, but this is the core model.

---

# 3. First: `Authentication`

Let's start with the object representing an authentication attempt/result.

Spring Security has:

```java
Authentication
```

Think of it as a representation of:

> **Who is attempting authentication, what credentials they supplied, and what authorities they have.**

Conceptually:

```text
Authentication
├── Principal
├── Credentials
├── Authorities
└── Authenticated
```

---

# 4. Authentication before verification

This is subtle.

Before authentication succeeds, an `Authentication` object can represent an **authentication request**.

For example:

```text
email = khushal@example.com
password = MyPassword123
```

Conceptually:

```text
Authentication
├── Principal = khushal@example.com
├── Credentials = MyPassword123
└── Authenticated = false
```

This represents:

> "Please authenticate this user using these credentials."

---

# 5. Authentication after verification

If the credentials are correct, the result becomes an authenticated representation.

Conceptually:

```text
Authentication
├── Principal = User 42
├── Authorities = ROLE_USER
├── Credentials = ...
└── Authenticated = true
```

Now it means:

> "This request has been successfully authenticated as User 42."

This distinction is extremely important.

---

# 6. What is the principal?

You encountered this in Lesson 1.

The **principal** represents the identity being authenticated.

It might initially be:

```text
username = khushal
```

After authentication, it might represent:

```text
User
id = 42
email = khushal@example.com
roles = USER
```

So:

```text
Principal
   ↓
Who is this?
```

Later, when we discuss `UserDetails`, you will see how Spring Security represents this information.

---

# 7. What are authorities?

Authorities represent permissions associated with the authenticated identity.

For example:

```text
ROLE_USER
ROLE_ADMIN
PRODUCT_READ
PRODUCT_DELETE
ORDER_CREATE
```

So an authenticated `Authentication` might conceptually contain:

```text
Principal:
    Khushal

Authorities:
    ROLE_USER
    ORDER_CREATE
```

Authorization later uses these authorities.

Therefore:

```text
Authentication
       ↓
Identity + Authorities
       ↓
Authorization
```

---

# 8. Now: `AuthenticationManager`

The next component is:

```java
AuthenticationManager
```

Its primary job is:

> **Take an authentication request and attempt to authenticate it.**

Its main method is conceptually:

```java
Authentication authenticate(Authentication authentication)
```

So the flow becomes:

```text
Authentication request
        ↓
AuthenticationManager
        ↓
Authentication result
```

But the manager generally does not perform all authentication logic itself.

That is where `AuthenticationProvider` comes in.

---

# 9. Why do we need `AuthenticationProvider`?

Imagine Spring Security needs to support different authentication mechanisms:

```text
Username/password
JWT
LDAP
OAuth2
X.509 certificate
etc.
```

You do not want one giant class containing every possible authentication mechanism.

Instead, Spring Security has:

```java
AuthenticationProvider
```

An `AuthenticationProvider` knows how to authenticate a particular kind of authentication request.

Conceptually:

```text
AuthenticationManager
        │
        ├── Provider A → username/password
        ├── Provider B → LDAP
        ├── Provider C → something else
        └── Provider D → ...
```

---

# 10. The manager delegates

This is the important relationship:

```text
AuthenticationManager
        ↓
"Which provider can handle this?"
        ↓
AuthenticationProvider
        ↓
Perform authentication
```

So:

```text
Manager
→ coordinates

Provider
→ performs a particular authentication mechanism
```

This distinction is worth remembering.

---

# 11. The common username/password provider

For traditional username/password authentication, Spring Security commonly uses:

```text
DaoAuthenticationProvider
```

The name can look intimidating.

The important idea is:

> It authenticates a username/password request using a `UserDetailsService` and a `PasswordEncoder`.

Conceptually:

```text
AuthenticationManager
        ↓
DaoAuthenticationProvider
        ↓
UserDetailsService
        ↓
UserDetails
        ↓
PasswordEncoder
```

Now we need to understand those two components.

---

# 12. `UserDetailsService`

This is one of the most commonly misunderstood interfaces.

```java
UserDetailsService
```

Its job is relatively simple:

> **Load user information for a username.**

It has a method conceptually like:

```java
UserDetails loadUserByUsername(String username)
```

Notice the name:

```text
loadUserByUsername
```

Even if your application actually uses an email address as the login identifier, Spring Security may still call that value the "username."

For example:

```text
username argument
        ↓
khushal@example.com
```

The implementation can query:

```sql
SELECT *
FROM users
WHERE email = ?
```

---

# 13. `UserDetails`

`UserDetails` represents the user information that Spring Security needs for authentication and authorization.

Conceptually:

```text
UserDetails
├── username
├── password
├── authorities
├── accountNonExpired
├── accountNonLocked
├── credentialsNonExpired
└── enabled
```

Not every application needs to use every property in a sophisticated way.

But Spring Security provides these concepts because real authentication systems often need things like:

```text
Is account active?
Is account locked?
Has the account expired?
Have credentials expired?
```

---

# 14. Your database User vs Spring's UserDetails

This is an important architectural distinction.

Your application might have:

```java
@Entity
class User {

    private Integer id;
    private String email;
    private String password;
    private String name;
    private String phone;
    ...
}
```

Spring Security has:

```java
UserDetails
```

These are **not necessarily the same thing**.

Your database entity represents your application's user.

`UserDetails` represents the information Spring Security needs about that user.

You can create an adapter:

```text
Database User
      ↓
UserDetails
      ↓
Spring Security
```

This is a very common pattern.

---

# 15. Why separate them?

Your application's `User` might contain:

```text
id
email
password
firstName
lastName
phone
address
dateOfBirth
createdAt
updatedAt
```

Spring Security does not need all of that to authenticate a user.

It primarily needs things like:

```text
username
password
authorities
account status
```

Separating the concepts keeps security concerns from unnecessarily taking over your domain model.

---

# 16. Now the password enters the picture

Suppose:

```text
Database:

email:
khushal@example.com

password:
$2a$10$....
```

The client submitted:

```text
password:
MyPassword123
```

The `AuthenticationProvider` needs to determine whether:

```text
MyPassword123
```

matches:

```text
$2a$10$....
```

This is where:

```java
PasswordEncoder
```

comes in.

---

# 17. `PasswordEncoder`

You already learned this in Lesson 3.

Its conceptual responsibilities are:

```text
encode(rawPassword)
        ↓
stored password hash
```

and:

```text
matches(rawPassword, storedHash)
        ↓
true / false
```

So the authentication provider can effectively do:

```text
Submitted password
        ↓
PasswordEncoder
        ↓
Matches stored hash?
```

---

# 18. The complete username/password flow

Now we can finally connect everything.

Client sends:

```text
email = khushal@example.com
password = MyPassword123
```

Spring Security creates an authentication request.

```text
Authentication
        ↓
AuthenticationManager
        ↓
AuthenticationProvider
        ↓
UserDetailsService
        ↓
Database
        ↓
UserDetails
        ↓
PasswordEncoder
        ↓
Password verification
```

If successful:

```text
Authentication
    ↓
authenticated = true
    ↓
SecurityContext
```

---

# 19. Let's trace it slowly

Imagine:

```text
POST /login
```

with:

```text
email = khushal@example.com
password = MyPassword123
```

### Step 1

An authentication request is created.

```text
Authentication
email = khushal@example.com
password = MyPassword123
```

---

### Step 2

It reaches:

```text
AuthenticationManager
```

The manager asks:

> Which authentication provider can handle this request?

---

### Step 3

The appropriate provider handles username/password authentication.

For example:

```text
DaoAuthenticationProvider
```

---

### Step 4

The provider asks:

```text
UserDetailsService
```

to load the user.

```text
loadUserByUsername(
    "khushal@example.com"
)
```

---

### Step 5

Your implementation queries the database.

```text
users
   ↓
email = khushal@example.com
   ↓
User
```

---

### Step 6

The user is converted into `UserDetails`.

```text
UserDetails
├── username
├── password hash
└── authorities
```

---

### Step 7

The provider uses:

```text
PasswordEncoder
```

to check:

```text
submitted password
        ↓
matches()
        ↑
stored password hash
```

---

### Step 8

If correct:

```text
Authentication
authenticated = true
```

---

### Step 9

The authentication is placed into the security context.

```text
SecurityContext
      ↓
Authentication
      ↓
User = Khushal
```

---

# 20. The architecture in one diagram

This is the diagram I want you to remember:

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
                  Authentication
                  authenticated=true
                           │
                           ↓
                    SecurityContext
```

This is the core username/password authentication architecture.

---

# 21. Why does Spring have so many abstractions?

At first this can feel unnecessarily complicated.

You might think:

> "Why not just have one `login()` method?"

Because Spring Security needs to support many authentication architectures.

For example:

```text
AuthenticationManager
        │
        ├── Username/password
        ├── LDAP
        ├── OAuth2
        ├── custom authentication
        └── other mechanisms
```

The abstractions allow the authentication system to remain modular.

This becomes particularly valuable in production applications.

---

# 22. A useful analogy

Think of a company security department.

### AuthenticationManager

Reception/security coordinator:

> "Someone wants to authenticate. I will route their request appropriately."

### AuthenticationProvider

Specialized security officer:

> "I know how to verify this particular type of credential."

### UserDetailsService

Employee directory:

> "Give me the information about this employee."

### PasswordEncoder

Credential verifier:

> "Does this supplied password match the stored password representation?"

### Authentication

The resulting identity/credential state:

> "This person has been authenticated as this user with these authorities."

### SecurityContext

The current request's security record:

> "This request is currently associated with this authenticated identity."

This analogy is not the implementation, but it is useful for remembering the responsibilities.

---

# 23. Where your Repository fits

This connects directly to the data-layer architecture you are studying.

Your implementation might eventually look conceptually like:

```text
UserRepository
      ↓
PostgreSQL
```

Then:

```text
UserDetailsService
      ↓
UserRepository
      ↓
PostgreSQL
```

So authentication does not magically access the database.

Your existing data-layer architecture still applies.

For example:

```text
AuthenticationProvider
        ↓
UserDetailsService
        ↓
UserRepository
        ↓
JPA/JDBC
        ↓
PostgreSQL
```

This is exactly why learning the data layer properly is useful for security.

---

# 24. A custom `UserDetailsService`

A simplified implementation could look like:

```java
@Service
public class CustomUserDetailsService
        implements UserDetailsService {

    private final UserRepository userRepository;

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String email) {

        User user = userRepository.findByEmail(email)
                .orElseThrow(() ->
                    new UsernameNotFoundException("User not found")
                );

        return new CustomUserDetails(user);
    }
}
```

Do not worry about implementing this yet.

We are studying the architecture first.

Notice the flow:

```text
UserDetailsService
        ↓
UserRepository
        ↓
Database
```

That should look familiar from your Spring learning.

---

# 25. What does `UserDetails` actually accomplish?

Suppose your database entity is:

```java
User
```

with:

```text
id
email
password
role
```

You could make it implement `UserDetails` directly.

Or you could create:

```java
CustomUserDetails
```

which wraps your domain user:

```text
CustomUserDetails
        ↓
User
```

Either approach can be appropriate depending on the application's architecture.

The important conceptual point is:

> Spring Security needs a security-oriented representation of the user.

---

# 26. Authorities come from the user

Suppose your database says:

```text
User:
id = 42
email = khushal@example.com
role = ADMIN
```

The `UserDetails` representation might expose:

```text
ROLE_ADMIN
```

Then later:

```java
.hasRole("ADMIN")
```

can make an authorization decision based on that authority.

So the flow becomes:

```text
Database
   ↓
User role
   ↓
UserDetails
   ↓
Authentication
   ↓
Authorities
   ↓
Authorization
```

We will go deep into roles and authorities later.

---

# 27. A very important distinction: `UserDetailsService` does not authenticate the password

This is a common beginner mistake.

`UserDetailsService`:

> **Loads user information.**

It does not primarily exist to:

> **Verify the password.**

The password verification is handled by the authentication provider using a password encoder.

So:

```text
UserDetailsService
       ↓
"Here is the user's stored information."

PasswordEncoder
       ↓
"These credentials match / do not match."
```

Keep those responsibilities separate.

---

# 28. Another important distinction: `PasswordEncoder` does not find users

Similarly:

```text
PasswordEncoder
```

does not normally:

```text
query database
find user
check roles
```

It handles password encoding and matching.

So:

```text
UserDetailsService
→ find/load user

PasswordEncoder
→ verify password

AuthenticationProvider
→ coordinate those pieces for that authentication mechanism
```

---

# 29. Another important distinction: `AuthenticationManager` does not necessarily query the database

The manager coordinates authentication.

It delegates to providers.

So think:

```text
AuthenticationManager
        ↓
AuthenticationProvider
        ↓
UserDetailsService
        ↓
Repository
        ↓
Database
```

rather than:

```text
AuthenticationManager
        ↓
Database
```

This separation will become very useful when you work with multiple authentication mechanisms.

---

# 30. What happens after successful authentication?

Suppose:

```text
User = Khushal
Role = USER
```

Authentication succeeds.

We now have:

```text
Authentication
├── Principal = Khushal
├── Authorities = ROLE_USER
└── authenticated = true
```

That gets associated with:

```text
SecurityContext
```

Conceptually:

```text
SecurityContext
       ↓
Authentication
       ↓
Principal
       ↓
Khushal
```

Now authorization mechanisms can ask:

```text
Who is making this request?
What authorities do they have?
```

---

# 31. The most important architecture so far

You now have three layers of understanding:

### Layer 1 — HTTP

```text
Request
   ↓
Security Filter Chain
```

### Layer 2 — Authentication

```text
AuthenticationManager
        ↓
AuthenticationProvider
        ↓
UserDetailsService
        ↓
PasswordEncoder
```

### Layer 3 — Authenticated request

```text
Authentication
        ↓
SecurityContext
        ↓
Authorization
        ↓
Controller
```

Put together:

```text
HTTP Request
     ↓
Security Filter Chain
     ↓
Authentication
     ↓
AuthenticationManager
     ↓
AuthenticationProvider
     ↓
UserDetailsService ──→ Repository ──→ Database
     ↓
PasswordEncoder
     ↓
Authenticated Authentication
     ↓
SecurityContext
     ↓
Authorization
     ↓
Controller
```

That is a major milestone in the course.

---

# 32. What we are deliberately NOT doing yet

We are not going to immediately write a complete JWT authentication system.

There are still important concepts to understand:

* `SecurityContext`
* `SecurityContextHolder`
* authentication persistence
* `UsernamePasswordAuthenticationFilter`
* `DaoAuthenticationProvider`
* how login requests are processed
* how JWT authentication differs
* how authorization uses authorities

If we skipped these and jumped straight to JWT code, you could build something that works without actually understanding it.

That would not achieve your goal.

---

# 33. Checkpoint

At this point you should be able to explain these in your own words:

| Component                | Responsibility                                                    |
| ------------------------ | ----------------------------------------------------------------- |
| `Authentication`         | Represents an authentication request/result                       |
| `AuthenticationManager`  | Coordinates authentication                                        |
| `AuthenticationProvider` | Performs a specific authentication mechanism                      |
| `UserDetailsService`     | Loads user information                                            |
| `UserDetails`            | Security-oriented representation of a user                        |
| `PasswordEncoder`        | Hashes and verifies passwords                                     |
| `SecurityContext`        | Holds authentication information for the current security context |

And especially:

```text
AuthenticationManager
        ↓
AuthenticationProvider
        ↓
UserDetailsService
        ↓
UserDetails

AuthenticationProvider
        ↓
PasswordEncoder
        ↓
Password verification
```

---

# Next — Lesson 7: `SecurityContext` and `SecurityContextHolder`

This is the next piece we need to understand before authentication will really "click."

We will answer:

> **After Spring Security authenticates a user, where does that authentication actually live?**

We will examine:

```text
Authentication
      ↓
SecurityContext
      ↓
SecurityContextHolder
      ↓
Current request
      ↓
Controller / Service
```

We will also see how code such as:

```java
Authentication authentication =
        SecurityContextHolder
                .getContext()
                .getAuthentication();
```

actually works, **why Spring can tell which user is making the current request, and how this changes between session-based and stateless/JWT authentication.**
