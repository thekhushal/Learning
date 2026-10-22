package com.example.ecom.dto;

public record UserResponse(
    Long id,
    String username,
    String email,
    boolean enabled
) {}


