package com.example.ecom;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor 
@AllArgsConstructor 
public class Product {

    private Integer id;

    private String name;
    private String description;
    private String category;
    private String brand;

    private Integer price;
    private Integer stockQuantity;

    private Boolean available;

    private Double rating;
    private Integer reviewCount;

    private String sku;
    private String manufacturer;

    private String color;
    private String warranty;
}