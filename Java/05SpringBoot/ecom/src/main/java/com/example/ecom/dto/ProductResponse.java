package com.example.ecom.dto;

import lombok.Getter;
import lombok.Setter;

@Getter 
@Setter 
public class ProductResponse {

    private Integer id;

    private String name;
    private String category;
    private String brand;

    private Integer price;
    private Boolean available;

    private String color;
    private String warranty;
}
