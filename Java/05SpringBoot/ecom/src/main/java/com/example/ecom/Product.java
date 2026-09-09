package com.example.ecom;

public class Product {
    private int id;
    private String name;
    private String category;
    private int price;

    public Product(String name, String category, int price){
        // this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
    }

    public String getCategory() {
        return category;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public void setId(int id) {
        this.id = id;
    }
}
