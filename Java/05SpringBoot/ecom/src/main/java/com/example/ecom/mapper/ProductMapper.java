package com.example.ecom.mapper;

import com.example.ecom.Product;
import com.example.ecom.dto.CreateProductRequest;
import com.example.ecom.dto.ProductResponse;

public class ProductMapper {
    public Product toProduct(CreateProductRequest request){
        Product product = new Product();

        product.setName(request.getName());
        product.setDescription(request.getDescription());
        product.setCategory(request.getCategory());
        product.setBrand(request.getBrand());
        product.setPrice(request.getPrice());
        product.setStockQuantity(request.getStockQuantity());
        product.setAvailable(request.getAvailable());
        product.setSku(request.getSku());
        product.setManufacturer(request.getManufacturer());
        product.setColor(request.getColor());
        product.setWarranty(request.getWarranty());
        return product;
    }

    public ProductResponse toResponse(Product product){
        ProductResponse response = new ProductResponse();
        response.setId(product.getId());
        response.setName(product.getName());
        response.setCategory(product.getCategory());
        response.setBrand(product.getBrand());
        response.setPrice(product.getPrice());
        response.setAvailable(product.getAvailable());
        response.setColor(product.getColor());
        response.setWarranty(product.getWarranty());
        return response;
    }
}
