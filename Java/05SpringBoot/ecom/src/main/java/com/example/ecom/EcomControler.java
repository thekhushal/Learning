package com.example.ecom;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController 
public class EcomControler {

    // DI
    EcomService service;
    public EcomControler(EcomService service){
        this.service = service;
    }

    // Post 1 Product
    @PostMapping("/product")
    public String createProduct(@RequestBody Product product){
        return service.createProduct(product);
    }

    // Post List of product
    @PostMapping ("/product/bulk")
    public String createProduct(@RequestBody List<Product> productList){
        return service.createProduct(productList);
    }

    // Get all Product
    @GetMapping(value = "/product")
    public List<Product> getProducts(){
        return service.getProducts();
    }

    // Get Product by id
    @GetMapping ("/product/{id}")
    public Product getProduct(@PathVariable int id){
        return service.getProduct(id);
    }

    // Get product by name
    @GetMapping(value = "/product", params = "name")
    public Product geProduct(@RequestParam String name){
        return service.getProductByName(name);
    }

    // Get product by Combination (name and id)
    @GetMapping (value = "/product/{id}", params = "name")
    public Product getProductByCombination(
        @PathVariable int id, 
        @RequestParam String name
    ){
        return service.getProductByCombination(id, name);
    }

    // Update Data
    @PutMapping ("/product/{id}")
    public String updateProduct(
        @PathVariable int id, 
        @RequestBody Product product
    ){
        return service.updateProduct(id, product);
    }
    
}
