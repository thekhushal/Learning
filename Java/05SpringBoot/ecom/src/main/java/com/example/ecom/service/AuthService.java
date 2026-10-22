package com.example.ecom.service;

import com.example.ecom.dto.RegisterRequest;
import com.example.ecom.dto.UserResponse;
import com.example.ecom.repository.UserRepository;

import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

@Service
public class AuthService {

    // DI
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public AuthService(
            UserRepository userRepository,
            PasswordEncoder passwordEncoder) {

        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    // 
    public UserResponse register(RegisterRequest request) {

        if (userRepository.existsByUsernameOrEmail(
                request.username(), request.email())) {

            throw new ResponseStatusException(
                HttpStatus.CONFLICT,
                "Username or email is already registered"
            );
        }

        String passwordHash =
            passwordEncoder.encode(request.password());

        Long id = userRepository.createUser(
            request.username(),
            request.email(),
            passwordHash
        );

        return new UserResponse(
            id,
            request.username(),
            request.email(),
            true
        );
    }
}