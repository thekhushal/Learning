package com.example.demo;

import org.springframework.stereotype.Service;import com.example.demo.UserRepository;

public class UserService {
    UserRepository repository;

    public UserService(UserRepository repository){
        this.repository = repository;
    }

    public createUser(){
        repository.saveUser();
    }
}
