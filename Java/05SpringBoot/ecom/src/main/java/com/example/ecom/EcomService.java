package com.example.ecom;

import java.util.List;

import org.springframework.stereotype.Service;

@Service 
public class EcomService {

    // DI
    EcomRepository repository;
    public EcomService(EcomRepository repository){
        this.repository = repository;
    }

    // Post Single Product
    public String createProduct(Product product){
        return repository.saveProduct(product);
    }

    // Post Multiple Products
    public String createProduct(List<Product> productList){
        for (Product product: productList){
            repository.saveProduct(product);
        }
        return "Products saved sucessfully";
    }

    // Get all Products
    public List<Product> getProducts(){
        return repository.getProducts();
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
