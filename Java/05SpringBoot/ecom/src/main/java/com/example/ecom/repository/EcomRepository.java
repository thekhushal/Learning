package com.example.ecom.repository;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.example.ecom.Product;
import com.example.ecom.dto.ProductResponse;

@Repository 
public class EcomRepository {
    // Product product;

    // creating a list of products
    List<Product> products = new ArrayList<>();
    int nextid = 1;

    // Create Product
    public Product saveProduct(Product product){
        product.setId(nextid);
        nextid++;

        products.add(product);
        return product;
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
    public Product updateProduct(int id, Product product){
        for (Product p: products){
            if (p.getId() == id){
                p.setName(product.getName());
                p.setDescription(product.getDescription());
                p.setCategory(product.getCategory());
                p.setBrand(product.getBrand());
                p.setPrice(product.getPrice());
                p.setStockQuantity(product.getStockQuantity());
                p.setAvailable(product.getAvailable());
                p.setSku(product.getSku());
                p.setManufacturer(product.getManufacturer());
                p.setColor(product.getColor());
                p.setWarranty(product.getWarranty());
                return p;
            }
        }
        return null ;
    }

    // Patch product
    public String patchProduct(int id, Product request){
        for (Product product : products){
            if (product.getId() == id){
                // set operations
                if (request.getName() != null){
                    product.setName(request.getName());
                }
                if (request.getPrice() != null){
                    product.setPrice(request.getPrice());
                }
                if (request.getCategory() != null){
                    product.setCategory(request.getCategory());
                }
            }
        }
        return "Patch Update Sucessfull ";
    }

    // Delete Product
    public String deleteProduct(int id){

        for (int i = 0; i<products.size(); i++){
            if (products.get(i).getId() == id){
                products.remove(i);
            }
        }
        return "Deleted product sucessfully";
    }
}
