package com.example.ecom.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.ecom.Product;
import com.example.ecom.dto.CreateProductRequest;
import com.example.ecom.dto.ProductResponse;
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

    // Create Single Product
    public ProductResponse createProduct(CreateProductRequest request){

        Product product = mapper.toProduct(request);
        Product savedProduct = repository.saveProduct(product);
        return mapper.toResponse(savedProduct);
    }

    // Post Multiple Products
    public String createProduct(List<Product> productList){
        for (Product product: productList){
            repository.saveProduct(product);
        }
        return "Products saved sucessfully";
    }

    // Get all Products
    public List<ProductResponse> getProducts(){
        List<Product> products = repository.getProducts();
        return mapper.productsToResponse(products);
    }

    // Get Product by id
    public Product getProduct(int id){
        return repository.getProduct(id);
    }

    // Get Product by name
    public Product getProductByName(String name){
        return repository.getProductByName(name);
    }

    // Get Product By Combination
    public Product getProductByCombination(int id, String name){
        return repository.getProductByCombination(id, name);
    }

    // Update Data
    public String updateProduct(int id, Product product){
        return repository.updateProduct(id, product);
    }

    // Patch Data
    public String patchProduct(int id, Product product){
        return repository.patchProduct(id, product);
    }

    // Delete Data
    public String deleteProduct(int id){
        return repository.deleteProduct(id);
    }
}
