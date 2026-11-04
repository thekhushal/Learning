package com.example.ecom.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter 
@Setter 
@NoArgsConstructor 
@AllArgsConstructor 
public class LoginRequest {
    
    @NotBlank 
    @Size(min = 3, max = 25)
    private String username;

    @NotBlank 
    private String password;
}
