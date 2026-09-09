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

    // Creating Product
    public String createProduct(Product product){
        return repository.saveProduct(product);
    }

    // Retriving Product
    public List<Product> getProducts(){
        return repository.getProducts();
    }

    // get Product by id
    public Product getProduct(int id){
        return repository.getProduct(id);
    }

    // get Product by name
    public Product getProductByName(String name){
        return repository.getProductByName(name);
    }

    // getProductByCombination
    public Product getProductByCombination(int id, String name){
        return repository.getProductByCombination(id, name);
    }
}
