package com.example.ecom.repository;

import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.example.ecom.entity.User;

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

    public boolean existsByUsernameOrEmail(
        String username, String email) 
        {

        String sql = """
            SELECT EXISTS (
                SELECT 1
                FROM users
                WHERE username = ? OR email = ?
            )
            """;

        Boolean exists = jdbcTemplate.queryForObject(
            sql, Boolean.class, username, email
        );

        return Boolean.TRUE.equals(exists);
    }

    public Long createUser(
            String username,
            String email,
            String passwordHash) {

        String sql = """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
            RETURNING id
            """;

        return jdbcTemplate.queryForObject(
            sql,
            Long.class,
            username,
            email,
            passwordHash
        );
    }
}
