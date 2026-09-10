package com.example.ecom;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

@Repository 
public class EcomRepository {
    Product product;

    // creating a list of products
    List<Product> products = new ArrayList<>();
    int nextid = 1;
    
    // Create Product
    public String saveProduct(Product product){
        product.setId(nextid);
        nextid++;

        products.add(product);
        return "Product created sucessfully";
    }

    // Retriving Product
    public List<Product> getProducts() {
        return products;
    }

    // Get product by id
    public Product getProduct(int id){
        for(Product p : products){
            if (p.getId() == id){
                return p;
            }
        }
        return null;
    }

    // Get products by name
    public Product getProductByName(String name){
        for (Product p : products){
            if (p.getName().equals(name)){
                return p;
            }
        }
        return null;
    }

    // getProductByCombination
    public Product getProductByCombination(int id, String name){
        for (Product p : products){
            if (p.getId() == id & p.getName().equals(name)){
                return  p;
            }
        }
        return null;
    }
}
