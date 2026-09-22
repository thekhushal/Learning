package com.example.ecom.repository;

import java.sql.PreparedStatement;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
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

// Get Queries ON DB:
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


// Post Queries ON DB:

    // Adding a product to DB
    public Product createProduct(Product product){

        String sql = """
            INSERT INTO products(
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
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """;
            
        KeyHolder keyHolder = new GeneratedKeyHolder();

        jdbcTemplate.update(connection -> {

            PreparedStatement statement = connection.prepareStatement(
                sql,
                new String[] { "id" }
            );

            statement.setString(1, product.getName());
            statement.setString(2, product.getDescription());
            statement.setString(3, product.getCategory());
            statement.setString(4, product.getBrand());

            statement.setObject(5, product.getPrice());
            statement.setObject(6, product.getStockQuantity());

            statement.setObject(7, product.getAvailable());

            statement.setObject(8, product.getRating());
            statement.setObject(9, product.getReviewCount());

            statement.setString(10, product.getSku());
            statement.setString(11, product.getManufacturer());
            statement.setString(12, product.getColor());
            statement.setString(13, product.getWarranty());

            return statement;

        }, keyHolder);

        Number generatedId = keyHolder.getKey();

        if (generatedId != null) {
            product.setId(generatedId.intValue());
        }

        return product;
    }

// Put Queries on DB:

    // Updating data in DB
    public int updateProduct(int id, Product product){
        String sql = """
            UPDATE products
            SET
                name = ?,
                description = ?,
                category = ?,
                brand = ?,  
                price = ?,
                stock_quantity = ?,
                available = ?,
                rating = ?,
                review_count = ?,
                sku = ?,
                manufacturer = ?,
                color = ?,
                warranty = ?
            WHERE id = ?
            """;
        
        return jdbcTemplate.update(
            sql, 
            product.getName(),
            product.getDescription(),
            product.getCategory(),
            product.getBrand(),
            product.getPrice(),
            product.getStockQuantity(),
            product.getAvailable(),
            product.getRating(), 
            product.getReviewCount(),
            product.getSku(),
            product.getManufacturer(),
            product.getColor(),
            product.getWarranty(),
            id
        );
    }
    
    // Delete Product
    public int deleteProduct(int id){
        String sql = """
            DELETE FROM products WHERE id = ?
        """;

        return jdbcTemplate.update(sql, id);
    }
    // --------------------------------------------
    // creating a list of products
    List<Product> products = new ArrayList<>();
    int nextid = 1;

    // Get Products By Combination of two fields

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
}
