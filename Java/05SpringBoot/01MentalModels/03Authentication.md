## 1. HTTP:

1. HTTP request/responce flow:

    ```text
    Client
        │
        │ HTTP Request
        ↓
    Server
        │
        │ HTTP Response
        ↓
    Client
    ```

2. Where,

    HTTP request:

    ```text
    GET /products/42 HTTP/1.1
    Host: api.example.com
    ```

    HTTP Response:

    ```text
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "id": 42,
        "name": "Laptop"
    }
    ```

3. Now HTTP is stateless

    1. HTTP itself wouldn't say request 3 came from same person who made request 1.
    2. Each request is fundamentally seperate request.
    3. So if user log's in

        ```text
        POST /auth/login
        ```

        and authentication succeeds, we need some mechanism to tell the server:

        ```text
        "The person making this new request is the same authenticated user."
        ```

        This is where sessions and tokens come in.

---

## 2. HTTP Headers: Headers carry metadata about HTTP requests and responses.

1. HTTP Header Example,

    ```text
    GET /products HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```

2. We will frequently see security related info in Headers.

    For example,

    ```text
    Authorization: Bearer eyJ...
    ```

    or,

    ```text
    Cookie: JSESSIONID=abc123
    ```

---

## 3. Authorization Header:

1. One of the most important Header in api authentication is,

    ```text
    "Authorization"
    ```

    For example,

    ```text
    Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
    ```

    Breaking it down,

    ```text
    Authorization --> authentication information

    Bearer --> authentication scheme

    eyJ... --> credential/token
    ```

2. Bearer: it means whoever posseses this token can present it as credential.

    - This has important security implications that we will discuss later.

---

## 4. Bearer Token:

1. Suppose login returns,

    ```text
    {
        "accessToken": "abc123xyz"
    }
    ```

2. The Client can subsequetly send

    ```text
    GET /products
    Authorization: Bearer abc123xyz
    ```

3. The server recives and validates it.

    ```text
    Client
        │
        │ Authorization: Bearer TOKEN
        ↓
    Server
        │
        ↓
    Validate TOKEN
        │
        ↓
    Identify user
        │
        ↓
    Authenticate request
    ```

JWT is one common format for such token

But:

```text
Bearer token and JWT are not the same thing.
```

---

## 5. Bearer token vs JWT:

1. A Bearer token describes how the credential is presented/used.
2. JWT describes a particular token format.
3. So,

    ```text
    Bearer
    → authentication scheme

    JWT
    → token format
    ```

4. You can have,

    ```text
    Authorization: Bearer <JWT>
    ```

    which is firley common.

    But conceptually they are different things.

---

## 6. Cookies:

1. Server can send,

    ```text
    Set-Cookie: JSESSIONID=abc123
    ```

    The browser stores it.

2. Later the browser automatically sends

    ```text
    Cookie: JSESSIONID=abc123
    ```

3. So,

    ```text
    Login response
        ↓
    Set-Cookie
        ↓
    Browser stores cookie
        ↓
    Future request
        ↓
    Cookie automatically sent
    ```

    this is commonly used for session based authentication

---

## 7. Session authentication:

### Step 1: Login

```text
POST /login

{
    "username": "khushal",
    "password": "..."
}
```

Server verifies the credentials

### Step 2: Create Session

Server Creates,

```text
Session ID = ABC123
```

And associates with,

```text
ABC123 → User 42
```

### Step 3: Send cookie

```text
Set-Cookie: JSESSIONID=ABC123
```

### Step 4: Future request

Browser sends,

```text
GET /orders
Cookie: JSESSIONID=ABC123
```

### Step 5: Server locks up Session

```text
ABC123
    ↓
User 42
    ↓
Authenticated
```

So,

```text
Cookie
    ↓
Session ID
    ↓
Server-side session
    ↓
User identity
```

---

## 8. HTTPS:

1. If communication were unencrypted, someone capable of observing the traffic could potentially see sensitive information.

    ```text
    Client
        │
        │ password/token
        ↓
    Internet
        │
        ↓
    Server
    ```

2. HTTPS uses TLS to provide an encrypted and authenticated communication channel.

    conceptually, HTTP + TLS = HTTPS

---

## 9. Password security vs HTTPS:

1. Password hashing protects stored passwords

2. HTTPS/TLS protects data while it travles.

---

## 10. Cookies have security attributes:

You may enounter,

```text
Set-Cookie: JSESSIONID=ABC123; Secure; HttpOnly; SameSite=Lax
```

1. Secure: The cookie should only be sent over HTTPS

    conceptually, Secure --> HTTPS

    This helps prevent the cookie from being transmitted over an unencrypted connection.

2. HttpOnly: An HttpOnly cookie cannot be normally accessed by Javascript

    This can reduce the impact of certain XSS attacks involving cookie theft.

    Important:
    HttpOnly does not prevent XSS itself.

    It limits one potential consequence: direct JavaScript access to that cookie.

3. SameSite: This controls when browsers send cookies in cross-site contexts.

    You will commonly encounter:

    - Strict
    - Lax
    - None

    This becomes particularly important when we study CSRF.

---

## 11. Authentication information can be attacked:

1. Now we see why protecting credentials matters.

2. Imagine an attacker obtains:

    ```text
    Authorization: Bearer eyJ...
    ```

3. If it is a valid bearer token, the attacker may be able to present it to the server as the user.

    Therefore:

    ```text
    Password security
        +
    Token security
        +
    Session security
        +
    HTTPS
    ```

    all matter.

4. Authentication does not end when the password has been verified.

---

## 12. A complete request lifecycle:

Suppose the user has already logged in and received a JWT.

The client makes:

```text
GET /orders/123
Authorization: Bearer eyJ...
```

The request travels over HTTPS:

```text
Client
   │
   │ HTTPS
   │
   │ Authorization: Bearer JWT
   ↓
Spring Boot
   │
   ↓
Security processing
   │
   ↓
Validate JWT
   │
   ↓
Identify user
   │
   ↓
Authentication
   │
   ↓
Authorization
   │
   ↓
Controller
   │
   ↓
Service
   │
   ↓
Repository
   │
   ↓
Database
```

---

## 13. Security Filter Chain: The missing piece

Imagine the incoming request:

```text
GET /orders/123
Authorization: Bearer eyJ...
```

Before the request reaches your controller, Spring Security can inspect it.

Conceptually:

```text
HTTP Request
    ↓
Security Filters
    ↓
Authentication
    ↓
Authorization
    ↓
Controller
```

This is one of the most important architectural ideas in Spring Security.

We are now ready to study it.
