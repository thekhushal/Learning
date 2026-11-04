package com.example.ecom.service;

import java.util.Date;

import javax.crypto.SecretKey;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;

@Service
public class JwtService {

    // DI
    private final SecretKey signingKey;
    private final long expirationMs;

    public JwtService(
            @Value("${jwt.secret}") String secret,
            @Value("${jwt.expiration-ms:900000}") long expirationMs) {

        this.signingKey = Keys.hmacShaKeyFor(
            Decoders.BASE64.decode(secret)
        );

        this.expirationMs = expirationMs;
    }

    // Generate Token
    public String generateToken(UserDetails userDetails) {

        Date issuedAt = new Date();
        Date expiration = new Date(
            issuedAt.getTime() + expirationMs
        );

        return Jwts.builder()
            .subject(userDetails.getUsername())
            .issuedAt(issuedAt)
            .expiration(expiration)
            .signWith(signingKey)
            .compact();
    }

    // Getter for expirationMs
    public long getexpirationMs(){
        return expirationMs;
    }

    // to extract username
    public String extractUsername(String token) {
        return extractAllClaims(token).getSubject();
    }

    // boolean check to confirm token validity
    public boolean isTokenValid(
            String token,
            UserDetails userDetails) {

        String username = extractUsername(token);

        return username.equals(userDetails.getUsername());
    }

    // extract all claims 
    private Claims extractAllClaims(String token) {

        return Jwts.parser()
            .verifyWith(signingKey)
            .build()
            .parseSignedClaims(token)
            .getPayload();
    }
}