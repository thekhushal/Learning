package com.example.ecom.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter 
@Setter
@AllArgsConstructor
public class LoginResponse {

    private String token;

    private String tokenType;

    private long expiratrionMs;
}
