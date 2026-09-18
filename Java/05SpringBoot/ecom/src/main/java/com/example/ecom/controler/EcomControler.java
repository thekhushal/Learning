package com.example.ecom.controler;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.ecom.Product;
import com.example.ecom.dto.CreateProductRequest;
import com.example.ecom.dto.ProductResponse;
import com.example.ecom.service.EcomService;

import jakarta.validation.Valid;

@RestController 
public class EcomControler {

    // DI
    EcomService service;
    public EcomControler(EcomService service){
        this.service = service;
    }

    // Create 1 Product
    @PostMapping("/product")
    public ProductResponse createProduct
    (
        @Valid 
        @RequestBody CreateProductRequest request
    ){
                
        return service.createProduct(request);
    }

    // Create List of product
    @PostMapping ("/product/bulk")
    public String createProduct(@RequestBody List<Product> productList){
        return service.createProduct(productList);
    }

    // Get all Product
    @GetMapping(value = "/product")
    public List<ProductResponse> getProducts(){
        return service.getProducts();
    }

    // Get Product by id
    @GetMapping ("/product/{id}")
    public ProductResponse getProduct(@PathVariable int id){
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
    
    // Patch Data
    @PatchMapping ("/product/{id}")
    public String patchProduct(
        @PathVariable int id,
        @RequestBody Product product
    ){
        return service.patchProduct(id, product);
    }

    // Delete Data
    @DeleteMapping ("/product/{id}")
    public String deleteProduct(@PathVariable int id ){
        return service.deleteProduct(id);
    }
}
