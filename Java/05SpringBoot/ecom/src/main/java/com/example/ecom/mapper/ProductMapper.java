package com.example.ecom.mapper;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Component;

import com.example.ecom.Product;
import com.example.ecom.dto.CreateProductRequest;
import com.example.ecom.dto.PatchProductRequest;
import com.example.ecom.dto.ProductResponse;
import com.example.ecom.dto.UpdateProductRequest;

@Component 
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

    public Product UPRtoProduct(UpdateProductRequest request){
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

    public Product PPRtoProduct(PatchProductRequest request){
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

    public List<ProductResponse> productsToResponse(List<Product> products){
        List<ProductResponse> response = new ArrayList<>();

        for (Product product : products){
            response.add(toResponse(product));
        }

        return response;
    }
}
