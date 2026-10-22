package com.example.ecom.repository;

import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.example.ecom.User;

@Repository 
public class UserRepository {
    // JDBC
    private final JdbcTemplate jdbcTemplate;

    // DI
    UserRepository(JdbcTemplate jdbcTemplate){
        this.jdbcTemplate = jdbcTemplate;
    }

    // Row Mapper
    private final RowMapper<User> UserRowMapper = (rs, rowNum) -> {
        User user = new User();

        user.setId((long) rs.getInt("id"));
        user.setUsername(rs.getString("username"));
        user.setEmail(rs.getString("email"));
        user.setPassword(rs.getString("password"));
        user.setEnabled(rs.getBoolean("enabled"));
        user.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
        user.setUpdatedAt(rs.getTimestamp("updated_at").toLocalDateTime());

        return user;
    };

    public User loadUserByUsername(String username){
        String sql = """
            SELECT * 
            FROM users
            WHERE username = ?;""";
        return jdbcTemplate.queryForObject(sql, UserRowMapper, username);
    }

    public List<User> getUser(){
        String sql = """
            SELECT 
                *
            FROM users;
        """;
        // return "Haa haaa!!!!!";
        return jdbcTemplate.query(sql, UserRowMapper);
    }
}
