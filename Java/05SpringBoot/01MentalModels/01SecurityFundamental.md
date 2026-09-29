## 1. Fundamentals goals of security

CIA - traid

1. Confidentiality - only authorized people should see info
2. Integrety - data should not be modified by someone who isnt authorized
3. Availablity - Authorised user should be able to use the system when they need to (An attacker can flood the api with enomorous requests)

---

## 2. Authentication vs Authorization

1. Authentication - Who are you???

    So,

    ```text
    Server verifies the credentials
            ↓
    (if valid credentials)
            ↓
    Authenticated user = Khushal
    ```

2. Authorization - What are you allowed to do???

    Suppose...

    ```text
    Khushal --> Role = USER
    Admin ----> Role = ADMIN
    ```

    API might allow:

    ```text
    USER:
        GET /products
        POST /orders

    ADMIN:
        POST   /products
        PUT    /products/{id}
        DELETE /products/{id}
    ```

    So,

    ```text
    Authentication
        ↓
    "Who are you?"

    Authorization
        ↓
    "What can you do?"
    ```

IMPORTANT: Authentication comes before Authorization

---

## 3. Identity & Principal:

1. Identity: Information that identifies an entity/user.

2. Principal: the identity associated with the current request.

    ```text
    Login
        ↓
    username + password
        ↓
    Authentication succeeds
        ↓
    Spring Security identifies the user
        ↓
    Principal = Khushal's authenticated identity
    ```

---

## 4. Credentials: Information used to prove identity
1. Password
2. API key
3. Access token
4. Certificate
5. OTP
6. Biometric authentication
---

## 5. Session & Tokens

1. Session-based authentication: The server maintains authentication state.

    Conceptually,

    ```text
    Login
        ↓
    Server creates session
        ↓
    Session ID
        ↓
    Client stores session ID
        ↓
    Future requests send session ID
    ```

2. Token-based authentication (JWT):

    Conceptually,

    ```text
    Login
        ↓
    Server verifies credentials
        ↓
    Access token
        ↓
    Client sends token with requests
    ```

---

## 6. Registration vs Login

1. Registration: User says --> Create an identity for me

    The server needs to,

    ```text
    Validate information
            ↓
    Check whether user already exists
            ↓
    Hash password
            ↓
    Store user
    ```

2. Login: User says --> I already have an identity. Prove I am that user.

    The server needs to,

    ```text
    Find user
        ↓
    Verify credential
        ↓
    Authenticate user
    ```

---

## 7. Password hashing:

1. Insted of storing raw pass in DB we use hash function to modify pass before storing
2. Hash function alter pass in a way that even if our DB is compromised, actual pass of user isnt exposed.
3. "Never store raw pass in DB", many users use same pass accross platforms

IMP: we don't usually manually hash passwords, but use specialized pass hashing algorithms like,

- bcrypt
- Argon2
- salt
- work factor
- brute-force resistance

---

## 8. Password verification steps:

1. User enters password (MyPass)
2. We pull pass hash from db
3. We pass both (Pass hash from DB & user pass) to the verification function of the algorithm that generated the hash and it verifies the user pass against the stored pass
4. If verified request moves further, else user gets error response

---

## 9. Registration Flow:

```text
      Registration Request
               │
               ↓
          Validate DTO
               │
               ↓
   Does user already exist?
        /            \
      YES             NO
       ↓               ↓
     Error       Hash password
                       │
                       ↓
                   Save user
                       │
                       ↓
                    Success
```

---

## 10. Login Flow:

```text
        Login Request
              │
              ↓
         Validate DTO
              │
              ↓
          Find user
              │
              ↓
         User exists?
          /        \
        NO          YES
        ↓            ↓
      Reject   Verify password
                     │
               ┌─────┴─────┐
             WRONG       CORRECT
               ↓            ↓
             Reject    Authenticate
                            │
                            ↓
                   Establish auth state
```

---

## 11. Authentication state:

1. HTTP itself does not inherently remember previous requests.
2. HTTP requests are fundamentally independent
3. So we need a mechanism to associate future requests with the authenticated identity.
4. There are two major approaches:

    ```text
    Stateful        Stateless
        ↓               ↓
     Session          Token
    ```

---

## 12. Session-based authentication: Or Cookie based authentcation

```text
Client
   │
(username + password)
   │
   ↓
Server
   │
(Verification)
   │
   ↓
Authenticated
   │
   ↓
Create session
```

1. The server might create,

    ```text
    sessionId = abc123xyz
    ```

2. The client recives that session identifier usually by cookie,

    ```text
    Set-Cookie: JSESSIONID=abc123xyz
    ```

3. Browser then stores it.

4. Then next request will contain something like,

    ```text
    Cookie: JSESSIONID=abc123xyz
    ```

5. Server recives,

    ```text
    abc123xyz
    ```

6. And associates it with,

    ```text
    User = Khushal
    ```

Q. Why is this called stateful authentication?

A. Because server maintains a state, something like

```text
session abc123xyz
       ↓
    user 42
```

Authentication state exists on server, Hence statefull

---

## 13. Token-based authentication:

Now consider:

```text
Client
   │
(username + password)
   │
   ↓
Server
   │
(Verification)
   │
   ↓
Generate access token
   │
   ↓
Client
```

1. The client sends,

    ```text
    Authorization: Bearer eyJ...
    ```

    with subsequent request.

2. The server validates the token.

3. Conceptually:

    ```text
    Request
       ↓
    Bearer token
       ↓
    Validate token
       ↓
    Extract identity
       ↓
    Authenticated
    ```

4. JWT is one common format.

5. Since no state was created this is called state-less acrchitecture.

---

## 14. Authentication is a process

1. Credentials were presented
2. Credentials were verified
3. An identity was established
4. Authentication state was established
5. Future requests can be associated with that identity

---

## 15. Authorization:

1. Suppose Authentication succeeds,

    ```text
    User = Khushal
    ```

2. Now the request is,

    ```text
    DELETE /products/42
    ```

3. Authentication tells us,

    ```text
    Khushal is making the request.
    ```

4. But we still need,

    ```text
    Can Khushal delete product 42?
    ```

5. That is Authorization.

6. The request life cycle finally becomes,

    ```text
                Request
                   ↓
             Authentication
                   ↓
             "Who is this?"
                   ↓
                Khushal
                   ↓
             Authorization
                   ↓
          "Can Khushal do this?"
              /           \
            YES            NO
             ↓              ↓
         Controller        403
    ```

---

## 16. 401 VS 403:

1. 401 Unauthorized:

    The request does not have valid authentication credentials.

    Examples,

    - No token
    - Invalid token
    - Expired token
    - Invalid credentials

2. 403 Forbidden:

    The server knows who you are but you are not permitted to perform this action.

    ```text
    User authenticated
            ↓
    Role = USER
            ↓
    DELETE /users/42
            ↓
    Not permitted
            ↓
    403 Forbidden
    ```

---

## 17. Authenticaiton Stages

-> Cerdential Vrification or Password verification is one part of authentication.

1. Authentication lifecycle might look like

    ```text
    Credential verification
            ↓
    Identity established
            ↓
    Authentication object/state created
            ↓
    Authentication stored/transmitted
            ↓
    Future requests recognized
    ```

2. Following are some classes/interfaces used to implement these stages

    - Authentication
    - AuthenticationManager
    - AuthenticationProvider
    - UserDetailsService
    - PasswordEncoder
    - SecurityContext

---

## MENTAL MODEL SO FAR:

### REGISTRATION:

```text
Password
   ↓
Hash
   ↓
Database
```

### LOGIN:

```text
Credentials
   ↓
Find user
   ↓
Verify password
   ↓
Authentication succeeds
   ↓
Establish authentication state
```

### REQUEST AFTER LOGIN:

```text
Session / Token
       ↓
Identify user
       ↓
Authentication
       ↓
Authorization
       ↓
Controller
```
