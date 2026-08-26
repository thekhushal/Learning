package com.example.demo;

import org.springframework.stereotype.Repository;

@UserRepository
public class UserRepository {
    public void saveUser(){
        System.out.println("User saved");
    }
}
