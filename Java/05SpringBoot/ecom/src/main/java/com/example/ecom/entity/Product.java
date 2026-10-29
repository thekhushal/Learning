package com.example.ecom.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.DecimalMax;
import jakarta.validation.constraints.DecimalMin;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity 
@Table(name = "products")
@Getter
@Setter
@NoArgsConstructor 
public class Product {

    @Id 
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "name", nullable = false, length = 100)
    private String name;

    @Column (name = "description", columnDefinition = "text")
    private String description;

    @Column (name = "category", length = 100)
    private String category;

    @Column(name = "brand", nullable = false, length = 100)
    private String brand;

    @Column (name = "price", nullable = false)
    private Integer price;

    @Column (name = "stock_quantity", nullable = false)
    private Integer stockQuantity;

    @Column (name = "available", nullable = false)
    private Boolean available;

    @Column (name = "rating")
    private Double rating;

    @Column (name = "review_count")
    private Integer reviewCount;

    @Column (name = "sku", length = 100)
    private String sku;

    @Column (name = "manufacturer", length = 100)
    private String manufacturer;

    @Column (name = "color", length = 50)
    private String color;

    @Column (name = "warranty", length = 100)
    private String warranty;
}