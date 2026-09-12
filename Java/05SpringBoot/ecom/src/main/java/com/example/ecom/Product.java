package com.example.ecom;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import jakarta.validation.constraints.Size;

public class Product {
    private int id;

    @NotBlank
    private String name;

    @NotBlank 
    private String category;

    @NotNull 
    @Positive 
    @Size (min=500, max = 5000)
    private Integer price;

    public Product(String name, String category, Integer price){
        // this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
    }

    // Getters
    public String getCategory() {
        return category;
    }
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public Integer getPrice() {
        return price;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setCategory(String category) {
        this.category = category;
    }
    public void setPrice(Integer price) {
        this.price = price;
    }
}
