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

    // Get Products By Combination of two fields

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

// PATCH Queries on DB: 
    // Patch data on id
    public Product patchProduct(int id, Product productRequest){
        StringBuilder sql = new StringBuilder("UPDATE products SET ");
        List<Object> params = new ArrayList<>();

        if (productRequest.getName() != null){
            sql.append("name = ?, ");
            params.add(productRequest.getName());
        }
        if (productRequest.getDescription() != null){
            sql.append("description = ?, ");
            params.add(productRequest.getDescription());
        }
        if (productRequest.getCategory() != null){
            sql.append("category = ?, ");
            params.add(productRequest.getCategory());
        }
        if (productRequest.getBrand() != null){
            sql.append("brand = ?, ");
            params.add(productRequest.getBrand());
        }
        if (productRequest.getPrice() != null){
            sql.append("price = ?, ");
            params.add(productRequest.getPrice());
        }
        if (productRequest.getStockQuantity() != null){
            sql.append("stock_quantity = ?, ");
            params.add(productRequest.getStockQuantity());
        }
        if (productRequest.getAvailable() != null){
            sql.append("available = ?, ");
            params.add(productRequest.getAvailable());
        }
        if (productRequest.getRating() != null){
            sql.append("rating = ?, ");
            params.add(productRequest.getRating());
        }
        if (productRequest.getReviewCount() != null){
            sql.append("review_count = ?, ");
            params.add(productRequest.getReviewCount());
        }
        if (productRequest.getSku() != null){
            sql.append("sku = ?, ");
            params.add(productRequest.getSku());
        }
        if (productRequest.getManufacturer() != null){
            sql.append("manufacturer = ?, "); 
            params.add(productRequest.getManufacturer());
        }
        if (productRequest.getColor() != null){
            sql.append("color = ?, ");
            params.add(productRequest.getColor());
        }
        if (productRequest.getWarranty() != null){
            sql.append("warranty = ?, ");
            params.add(productRequest.getWarranty());
        }

        sql.setLength(sql.length() - 2); // Remove the last comma and space

        sql.append(" WHERE id = ?");
        params.add(id);
        
        jdbcTemplate.update(sql.toString(), params.toArray());

        return findById(id);

    }

// DELETE Queries on DB:
    // Delete Product
    public int deleteProduct(int id){
        String sql = """
            DELETE FROM products WHERE id = ?
        """;

        return jdbcTemplate.update(sql, id);
    }

}
