package com.example.ecom.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import jakarta.validation.constraints.PositiveOrZero;
import lombok.Getter;
import lombok.Setter;

@Getter 
@Setter 
public class CreateProductRequest {

    @NotBlank 
    private String name;

    private String description;
    private String category;

    @NotBlank 
    private String brand;

    @NotNull 
    @Positive 
    private Integer price;

    @NotNull 
    @PositiveOrZero 
    private Integer stockQuantity;

    @NotNull
    private Boolean available;

    private String sku;
    private String manufacturer;

    private String color;
    private String warranty;
}
