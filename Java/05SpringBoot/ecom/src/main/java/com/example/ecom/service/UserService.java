package com.example.ecom.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.ecom.entity.User;
import com.example.ecom.repository.UserRepository;

@Service 
public class UserService {
    // DI
    @Autowired 
    private UserRepository repository;

    // Get all users
    public List<User> getUser(){
        return repository.getUser();
    }

    // By username
    public User loadByUsername(String username){
        return repository.loadUserByUsername(username);
    }
}
