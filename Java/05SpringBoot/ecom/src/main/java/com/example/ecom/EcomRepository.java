package com.example.ecom;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

@Repository 
public class EcomRepository {
    // Product product;

    // creating a list of products
    List<Product> products = new ArrayList<>();
    int nextid = 1;

    // Post Product
    public String saveProduct(Product product){
        product.setId(nextid);
        nextid++;

        products.add(product);
        return "Product created sucessfully";
    }

    // Get all Products
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

    // Get Product By Combination
    public Product getProductByCombination(int id, String name){
        for (Product p : products){
            if (p.getId() == id & p.getName().equals(name)){
                return  p;
            }
        }
        return null;
    }

    // Update product
    public String updateProduct(int id, Product product){
        for (Product p: products){
            if (p.getId() == id){
                p.setName(product.getName());
                p.setCategory(product.getCategory());
                p.setPrice(product.getPrice());
            }
        }
        return "Product updated sucessfully";
    }

    // Patch product
    public String patchProduct(int id, Product request){
        for (Product product : products){
            if (product.getId() == id){
                // set operations
                if (request.getName() != null){
                    product.setName(request.getName());
                }
                if (request.getPrice() != 0){
                    product.setPrice(request.getPrice());
                }
                if (request.getCategory() != null){
                    product.setCategory(request.getCategory());
                }
            }
        }
        return "Patch Update Sucessfull ";
    }
}
