package com.example.ecom.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter 
@Setter 
@NoArgsConstructor
@AllArgsConstructor 
public class ProductResponse {

    private Integer id;

    private String name;
    private String description;
    private String color;
    private String category;
    private String brand;

    private Integer price;
    private Boolean available;
    private String warranty;
}
