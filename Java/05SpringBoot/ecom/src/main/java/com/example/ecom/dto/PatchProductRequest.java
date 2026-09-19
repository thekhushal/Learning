package com.example.ecom.dto;

import jakarta.validation.constraints.Positive;
import jakarta.validation.constraints.PositiveOrZero;
import lombok.Getter;
import lombok.Setter;

@Getter 
@Setter 
public class PatchProductRequest{
    private String name;

    private String description;
    private String category;
    private String brand;

    @Positive 
    private Integer price;

    @PositiveOrZero 
    private Integer stockQuantity;

    private Boolean available;

    private String sku;
    private String manufacturer;
    private String warranty;
    private String color;
}

