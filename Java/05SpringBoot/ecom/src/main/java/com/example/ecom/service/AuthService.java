package com.example.ecom.service;

import com.example.ecom.dto.LoginRequest;
import com.example.ecom.dto.LoginResponse;
import com.example.ecom.dto.RegisterRequest;
import com.example.ecom.dto.UserResponse;
import com.example.ecom.repository.UserRepository;

import org.springframework.http.HttpStatus;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

@Service
public class AuthService {

    // DI
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    public AuthService(
            UserRepository userRepository,
            PasswordEncoder passwordEncoder,
            JwtService jwtService,
            AuthenticationManager authenticationManager) {

        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtService = jwtService;
        this.authenticationManager = authenticationManager;
    }

    // Register a new user
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

    // Login a user and generate JWT token
    public LoginResponse login(LoginRequest request){
        Authentication authentication = 
                authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(
                        request.getUsername(),
                        request.getPassword())
                );
        
        UserDetails userDetails = (UserDetails) authentication.getPrincipal();

        String token = jwtService.generateToken(userDetails);

        return new LoginResponse(
            token,
            "Bearer",
            jwtService.getexpirationMs()
        );

    }

}