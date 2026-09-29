## 1. Request flow so far:

```text
HTTP Request
    ↓
Controller
    ↓
Service
    ↓
Repository
```

- But, that isn't what happens, there is a infrastructure that processes request before it reaches Controller.

```text
HTTP Request
    ↓
Servlet Container
    ↓
Filters
    ↓
DispatcherServlet
    ↓
Controller
```

- Spring Security integrates into this filter-based request processing.

---

## 2. What is a Filter???

A filter is something that can inspect or modify an HTTP request/response before it reaches your controller.

Conceptually,

```text
Request
    ↓
Filter
    ↓
Controller
```

Filters can do things like,

- Check authentication
- Log request
- Add headers
- Check CORS
- Process security credentials
- Reject request
- Continue request

For example,

If user credentials can be authenticated,

```text
Request
    ↓
Authentication Filter
    ↓
Controller
```

If not,

```text
Request
    ↓
REJECT
```

---

## 3. Multiple Filters: This is the basic idea behind Security Filter Chain, having multiple filters.

Conceptually,

```text
Request
    ↓
Filter A
    ↓
Filter B
    ↓
Filter C
    ↓
Filter D
    ↓
Controller
```

- Each filter has a specific responsiblity

---

## 4. Spring Security Filter Chain: A simplified architecture would be

```text
                    HTTP Request
                         │
                         ↓
              Security Filter Chain
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Filter 1       Filter 2       Filter 3
          │              │              │
          └──────────────┼──────────────┘
                          ↓
                   Authorization
                          ↓
                     Controller
```

Just remember,

A request passes through a sequence of security filters before your application code is allowed to process it.

---

## 5. Why use filters???

Because without filters we'll end up doing something closer to,

```java
@GetMapping("/products")
public ... {
    checkAuthentication();
    ...
}

@PostMapping("/orders")
public ... {
    checkAuthentication();
    ...
}

@DeleteMapping("/products/{id}")
public ... {
    checkAuthentication();
    ...
}
```

1. This is repetitive and error prone.
2. A better architecture would be,

    ```text
    HTTP Request
          ↓
    Security Filter Chain
          ↓
    Authentication
          ↓
    Authorization
          ↓
    Controller
    ```

Security can be applied consistently before the controller.

---

## 6. Security Filter Chain:

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http)
        throws Exception {

    return http
            .authorizeHttpRequests(auth -> auth
                    .anyRequest().authenticated()
            )
            .build();
}
```

Let's Understand this code properly,

1. SecurityFilterChain: It represents a configured chain of security filters.

    Conceptually,

    ```text
    SecurityFilterChain
            │
            ├── Filter A
            ├── Filter B
            ├── Filter C
            ├── Filter D
            └── ...
    ```

2. Why @Bean???

    The annotation tells spring to create and manage the object as a spring bean.

    Then Spring Security can use that configured filter chain as part of the application's security infrastructure.

3. What's HttpSecurity???

    ```java
    SecurityFilterChain securityFilterChain(HttpSecurity http)
    ```

    1. Think of this as a configuration builder for web security.

        You use it to Configure things such as:

        - Authentication
        - Authorization
        - CSRF
        - CORS
        - Sessions
        - Form login
        - HTTP Basic
        - OAuth2
        - etc.

    2. For example ,

        ```java
        http
            .authorizeHttpRequests(...)
        ```

        Means,

        Configure authorization rules for HTTP requests.

4. The Builder Pattern

    ```java
    http
        .authorizeHttpRequests(...)
        .csrf(...)
        .sessionManagement(...)
        .build();
    ```

    This is essentially a builder style api.

    Conceptually,

    ```text
    HttpSecurity
        ↓
    configure something
        ↓
    configure something else
        ↓
    configure something else
        ↓
    build()
        ↓
    SecurityFilterChain
    ```

    So,

    ```text
    .build()
    ```

    ultimately creates the configured securityFilterChain

---

## 7. First Security configuration:

Consider,

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http)
        throws Exception {

    return http
            .authorizeHttpRequests(auth -> auth
                    .anyRequest().authenticated()
            )
            .build();
}
```

The important part is,

```text
.anyRequest().authenticated()
```

It means, any request must be authenticated. Request does not simply reaches the controller.

So Conceptually,

```text
GET /products
    ↓
Authenticated?
  /       \
YES        NO
 ↓          ↓
Continue  Reject
```

---

## 8. Public vs Protected endpoints:

Suppose we have,

```text
POST /auth/register
POST /auth/login
GET  /products
POST /products
DELETE /products/{id}
```

We probably want,

```text
/register → public
/login    → public
/products → authenticated
```

Such authorization rules can be expressed as:

```java
http.authorizeHttpRequests(auth -> auth
    .requestMatchers("/auth/register", "/auth/login").permitAll()
    .anyRequest().authenticated()
);
```

Conceptually,

```text
/auth/register
    ↓
permitAll()
    ↓
Controller


/auth/login
    ↓
permitAll()
    ↓
Controller


/products
    ↓
authenticated()
    ↓
Authentication required
```

---

## 9. permitAll() vs authenticated()

1. permitAll()

    ```java
    .requestMatchers("/auth/login").permitAll()
    ```

    Means, endpoint can be accessed without an authenticated user.

    Spring may still process it, it isn't ignored by security infrastructure of spring, but it'll remain open to all users (authenticated or not)

2. authenticated()

    ```java
    .anyRequest().authenticated()
    ```

    Means, The request must have an authenticated identity.

---

## 10. Roles: We can now configure an endpoint which is accessible depending on role of person making request.

Suppose,

```text
GET /products
```

should be accessible to everyone

But,

```text
DELETE /products/{id}
```

should only be accessible to ADMIN

We could eventually configure,

```java
.requestMatchers(HttpMethod.DELETE, "/products/**")
.hasRole("ADMIN")
```

Conceptually,

```text
DELETE /products/10
         ↓
  Authenticated?
         ↓
        YES
         ↓
   Role = ADMIN?
     /      \
   YES       NO
    ↓         ↓
  Allow      403
```

---

## 11. The request flow with JWT: (JWT Filter)

- JWT processing happens as one of the filters inside the security filter chain.

Suppose client sends,

```text
GET /products
Authorization: Bearer eyJ...
```

That would be something like,

```text
HTTP Request
    ↓
Security Filter Chain
    ↓
JWT-related processing
    ↓
Extract token
    ↓
Validate token
    ↓
Identify user
    ↓
Create authenticated SecurityContext
    ↓
Authorization
    ↓
Controller
```

The exact implementation depends on configuration but this is the rough architecture

---

## 12. Security Context:

1. Suppose spring security has successfully identified:

    ```text
    User ID = 42
    Username = khushal
    Role = USER
    ```

2. Spring security needs somewhere to hold the authentication information of the current request

3. That is where Security Context comes in.

4. Conceptually,

    ```text
    SecurityContext
        │
        ↓
    Authentication
        │
        ├── Principal
        ├── Authorities
        └── Authentication state
    ```

5. so,

    ```text
    Request
        ↓
    Authentication succeeds
        ↓
    SecurityContext
        ↓
    Controller can access authenticated identity
    ```

---

## 13. Authentication Object:

1. Inside the security Context there is an Authentication object.

2. Conceptually,

    ```text
    Authentication
    ├── Principal
    ├── Credentials
    ├── Authorities
    └── authenticated?
    ```

3. For example,

    ```text
    Principal:
        User 42

    Authorities:
        ROLE_USER

    Authenticated:
        true
    ```

4. The object represents the authentication result for the current request.

---

## 14. Authentication vs authorization inside the chain

Consider,

```text
DELETE /products/10
Authorization: Bearer eyJ...
```

The security processing Conceptually does:

1. Authentication:

    ```text
    Is this token valid?
            ↓
    Who does it represent?
            ↓
        Khushal
    ```

Then,

2. Authorization:

    ```text
    Can Khushal-> DELETE /products/10?
            ↓
        Role?
        Permission?
        Ownership?
            ↓
    Allow / Reject
    ```

3. So,

    ```text
          Request
             ↓
      Authentication
             ↓
         Identity
             ↓
      Authorization
             ↓
        Allow/Deny
    ```

---

## 15. What happens when authentication fails?

1. Suppose,

    ```text
    GET /products
    ```

    But no credentials are supplied but endpoint requires authentication

2. Conceptually,

    ```text
    Request
        ↓
    Security Filter Chain
        ↓
    Authentication required
        ↓
    No valid authentication
        ↓
    401
    ```

---

## 16. What happens when authorization fails?

1. Suppose,

    ```text
    User = USER
    ```

2. and,

    ```text
    DELETE /products/10
    ```

3. requires

    ```text
    ADMIN
    ```

4. Authentication Succeeded

    ```text
    USER → authenticated
    ```

5. Authorization Failed

    ```text
    USER → not authorized
    ```

6. Therefore,

    ```text
    403 Forbidden
    ```

7. Again,

    ```text
    401
    → authentication problem
    403
    → authorization problem
    ```
