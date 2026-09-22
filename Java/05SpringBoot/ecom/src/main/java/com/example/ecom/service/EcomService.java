package com.example.ecom.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;

import com.example.ecom.Product;
import com.example.ecom.dto.CreateProductRequest;
import com.example.ecom.dto.PatchProductRequest;
import com.example.ecom.dto.ProductResponse;
import com.example.ecom.dto.UpdateProductRequest;
import com.example.ecom.mapper.ProductMapper;
import com.example.ecom.repository.EcomRepository;


@Service 
public class EcomService {

    // DI
    EcomRepository repository;
    ProductMapper mapper;
    public EcomService(EcomRepository repository, ProductMapper mapper){
        this.repository = repository;
        this.mapper = mapper;
    }

// POST
    // Create Single Product
    public ProductResponse createProduct(CreateProductRequest request){

        Product product = mapper.toProduct(request);
        Product savedProduct = repository.createProduct(product);
        return mapper.toResponse(savedProduct);
    }

// GET
    // Get all Products
    public List<ProductResponse> getProducts(){
        List<Product> products = repository.getProducts();
        return mapper.productsToResponse(products);
    }

    // Get Product by id
    public ProductResponse getProduct(int id){
        Product product = repository.findById(id);
        ProductResponse response = mapper.toResponse(product);
        return response;
    }

    // Get Product by name
    public List<ProductResponse> getProductByName(String name){
        List<Product> products = repository.getProductByName(name);

        List<ProductResponse> response = mapper.productsToResponse(products);
        return response;
    }

    // Get Product By Combination
    public ProductResponse getProductByCombination(int id, String name){
        Product product = repository.getProductByCombination(id, name);

        ProductResponse response = mapper.toResponse(product);
        return response;
    }

// PUT
    // Update Data By id
    public int updateProduct(int id, UpdateProductRequest request){

        Product productRequest = mapper.UPRtoProduct(request);
        int rowsAffected = repository.updateProduct(id, productRequest);

        return rowsAffected;
    }

    // Patch Data By id
    public ProductResponse patchProduct(int id, PatchProductRequest request){
        Product productRequest = mapper.PPRtoProduct(request);
        Product product = repository.patchProduct(id, productRequest);

        ProductResponse response = mapper.toResponse(product);
        return response;
    }

// DELETE
    // Delete Data
    public int deleteProduct(int id){
        return repository.deleteProduct(id);
    }
}
