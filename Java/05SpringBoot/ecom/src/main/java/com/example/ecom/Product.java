package com.example.ecom;

public class Product {
    private int id;
    private String name;
    private String category;
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
