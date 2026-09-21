package com.example.ecom.repository;

import java.util.ArrayList;
import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.example.ecom.Product;

@Repository 
public class EcomRepository {

    // JDBC
    private final JdbcTemplate jdbcTemplate;

    // DI
    EcomRepository(JdbcTemplate jdbcTemplate){
        this.jdbcTemplate = jdbcTemplate;
    }

    // Row Mapper
    private final RowMapper<Product> productRowMapper = (rs, rowNum) -> {

        Product product = new Product();

        product.setId(rs.getInt("id"));
        product.setName(rs.getString("name"));
        product.setDescription(rs.getString("description"));
        product.setCategory(rs.getString("category"));
        product.setBrand(rs.getString("brand"));

        product.setPrice(rs.getInt("price"));
        product.setStockQuantity(rs.getInt("stock_quantity"));

        product.setAvailable(rs.getBoolean("available"));

        product.setRating(rs.getDouble("rating"));
        product.setReviewCount(rs.getInt("review_count"));

        product.setSku(rs.getString("sku"));
        product.setManufacturer(rs.getString("manufacturer"));

        product.setColor(rs.getString("color"));
        product.setWarranty(rs.getString("warranty"));

        return product;
    };

// Get Queries ON DB
    // Get all products FROM DB 
    public List<Product> getProducts() {

        String sql = """
                SELECT
                    *
                FROM products;
                """;

        return jdbcTemplate.query(
            sql,
            productRowMapper
        );
    }

    // Get 1 product by id FROM DB
    public Product findById(Integer id) {

        String sql = """
                SELECT
                    id,
                    name,
                    description,
                    category,
                    brand,
                    price,
                    stock_quantity,
                    available,
                    rating,
                    review_count,
                    sku,
                    manufacturer,
                    color,
                    warranty
                FROM products
                WHERE id = ?
                """;

        return jdbcTemplate.queryForObject(
            sql,
            productRowMapper,
            id
        );
    }
    
    // Get products by name FROM DB
    public List<Product> getProductByName(String name){
        String sql = """
                select * from Products
                where name = ?;
                """;

        List<Product> products = jdbcTemplate.query(
            sql,
            productRowMapper,
            name
        );

        return products;
    }


// Post Queries ON DB
    // Adding a product to DB
    public Product crateProduct(Product product){

        String sql = """
            INSERT INTO 
            """;
        Product savedProduct;
        return savedProduct;
    }
    // --------------------------------------------
    // creating a list of products
    List<Product> products = new ArrayList<>();
    int nextid = 1;

    // Create Product
    // public Product saveProduct(Product product){
    //     product.setId(nextid);
    //     nextid++;

    //     products.add(product);
    //     return product;
    // }

    // Get all Products
    // public List<Product> getProducts() {
    //     return products;
    // }

    // Get product by id
    // public Product getProduct(int id){
    //     for(Product p : products){
    //         if (p.getId() == id){
    //             return p;
    //         }
    //     }
    //     return null;
    // }

    // Get products by name
    // public Product getProductByName(String name){
    //     for (Product p : products){
    //         if (p.getName().equals(name)){
    //             return p;
    //         }
    //     }
    //     return null;
    // }

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
    public Product patchProduct(int id, Product request){
        for (Product product : products){
            if (product.getId() == id){
                // set operations
                if (request.getName() != null){
                    product.setName(request.getName());
                }
                if (request.getDescription() != null){
                    product.setDescription(request.getDescription());
                }
                if (request.getCategory() != null){
                    product.setCategory(request.getCategory());
                }
                if (request.getBrand() != null){
                    product.setBrand(request.getBrand());
                }
                if (request.getPrice() != null){
                    product.setPrice(request.getPrice());
                }
                if (request.getStockQuantity() != null){
                    product.setStockQuantity(request.getStockQuantity());
                }
                if (request.getAvailable() != null){
                    product.setAvailable(request.getAvailable());
                }
                if (request.getSku() != null){
                    product.setSku(request.getSku());
                }
                if (request.getManufacturer() != null){
                    product.setManufacturer(request.getManufacturer());
                }
                if (request.getColor() != null){
                    product.setColor(request.getColor());
                }
                if (request.getWarranty() != null){
                    product.setWarranty(request.getWarranty());
                }
                return product;
            }
        }
        return null;
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
