package com.example.ecom.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import jakarta.validation.constraints.PositiveOrZero;
import lombok.Getter;
import lombok.Setter;

@Getter 
@Setter 
public class UpdateProductRequest{
    @NotBlank 
    private String name;

    @NotBlank 
    private String description;
    @NotBlank
    private String category;

    @NotBlank 
    private String brand;

    @NotNull
    @Positive 
    private Integer price;

    @NotNull 
    @PositiveOrZero 
    private Integer stockQuantity;

    @NotBlank 
    private Boolean available;

    @NotBlank 
    private String sku;
    @NotBlank 
    private String manufacturer;

    @NotBlank 
    private String color;
    @NotBlank 
    private String warranty;
}

