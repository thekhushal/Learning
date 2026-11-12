package com.example.ecom.controler;

import com.example.ecom.dto.RegisterRequest;
import com.example.ecom.dto.UserResponse;
import com.example.ecom.dto.LoginRequest;
import com.example.ecom.dto.LoginResponse;
import com.example.ecom.service.AuthService;

import jakarta.validation.Valid;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class AuthController {

    // Di
    private final AuthService authService;

    public AuthController(AuthService authService) {
        this.authService = authService;
    }
    

    @PostMapping("/register")
    @ResponseStatus(HttpStatus.CREATED)
    public UserResponse register(
            @Valid @RequestBody RegisterRequest request) {

        return authService.register(request);
    }

    @PostMapping("/login")
    public LoginResponse login(
            @Valid @RequestBody LoginRequest request) {

        return authService.login(request);
    }
}