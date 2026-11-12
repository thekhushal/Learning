package com.example.ecom.security;

import java.io.IOException;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import org.springframework.security.authentication.AuthenticationException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import io.jsonwebtoken.JwtException;

import com.example.ecom.service.JwtService;

@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtService jwtService;
    private final UserDetailsService userDetailsService;

    public JwtAuthenticationFilter(
            JwtService jwtService,
            UserDetailsService userDetailsService) {

        this.jwtService = jwtService;
        this.userDetailsService = userDetailsService;
    }

    @Override
    protected void doFilterInternal(
            HttpServletRequest request,
            HttpServletResponse response,
            FilterChain filterChain)
            throws ServletException, IOException {

        // 1. Extract Authorization header
        String authHeader = request.getHeader("Authorization");

        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            filterChain.doFilter(request, response);
            return;
        }

        // 2. Do not overwrite existing authentication
        if (SecurityContextHolder.getContext().getAuthentication() != null) {
            filterChain.doFilter(request, response);
            return;
        }

        // 3. Extract JWT
        String token = authHeader.substring(7);

        try {

            // 4. Extract username
            String username = jwtService.extractUsername(token);

            if (username == null || username.isBlank()) {
                filterChain.doFilter(request, response);
                return;
            }

            // 5. Load user
            UserDetails userDetails =
                    userDetailsService.loadUserByUsername(username);

            // 6. Validate token
            if (!jwtService.isTokenValid(token, userDetails)) {
                filterChain.doFilter(request, response);
                return;
            }

            // 7. Create authenticated object
            UsernamePasswordAuthenticationToken authToken =
                    new UsernamePasswordAuthenticationToken(
                            userDetails,
                            null,
                            userDetails.getAuthorities()
                    );

            authToken.setDetails(
                    new WebAuthenticationDetailsSource().buildDetails(request)
            );

            // 8. Establish authentication
            SecurityContext context =
                    SecurityContextHolder.createEmptyContext();

            context.setAuthentication(authToken);
            SecurityContextHolder.setContext(context);

        } catch (JwtException | IllegalArgumentException | AuthenticationException ex) {

            SecurityContextHolder.clearContext();
        }

        // 9. Continue filter chain
        filterChain.doFilter(request, response);
    }
}