# E-commerce Project Structure

```text
ecom/
├── .mvn/
│   └── wrapper/
│       └── maven-wrapper.properties
├── mvnw
├── mvnw.cmd
├── pom.xml
└── src/
    ├── main/
    │   ├── java/com/example/ecom/
    │   │   ├── EcomApplication.java
    │   │   ├── Product.java
    │   │   ├── User.java
    │   │   ├── UserPrincipal.java
    │   │   ├── config/
    │   │   │   ├── MyUserDetailsService.java
    │   │   │   └── SecurityConfig.java
    │   │   ├── controler/
    │   │   │   ├── AuthController.java
    │   │   │   └── EcomControler.java
    │   │   ├── dto/
    │   │   │   ├── CreateProductRequest.java
    │   │   │   ├── PatchProductRequest.java
    │   │   │   ├── ProductResponse.java
    │   │   │   ├── RegisterRequest.java
    │   │   │   ├── UpdateProductRequest.java
    │   │   │   └── UserResponse.java
    │   │   ├── mapper/
    │   │   │   └── ProductMapper.java
    │   │   ├── repository/
    │   │   │   ├── EcomRepository.java
    │   │   │   └── UserRepository.java
    │   │   └── service/
    │   │       ├── AuthService.java
    │   │       ├── EcomService.java
    │   │       └── UserService.java
    │   └── resources/
    │       └── application.properties
    └── test/java/com/example/ecom/
        └── EcomApplicationTests.java
```

## Package responsibilities

- `config/`: Spring configuration, including security configuration and user lookup.
- `controler/`: HTTP endpoints for authentication and products.
- `dto/`: Request and response payloads exposed through the API.
- `mapper/`: Converts between product models and DTOs.
- `repository/`: JDBC/database access for products and users.
- `service/`: Business logic for authentication, users, and products.
- Root model classes: `Product`, `User`, and `UserPrincipal`.
- `resources/`: Application configuration.
- `src/test/`: Automated tests.

## Notes

- This structure reflects the current `main` branch of the `Learning` repository at `Java/05SpringBoot/ecom`.
- The package name is `controler` in the repository; it is conventionally spelled `controller`. Rename it only as a deliberate refactor, updating package declarations and imports.
- `UserPrincipal` is a security adapter implementing `UserDetails`; `MyUserDetailsService` should implement `UserDetailsService`.
