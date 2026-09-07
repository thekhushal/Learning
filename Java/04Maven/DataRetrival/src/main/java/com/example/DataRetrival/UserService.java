package com.example.DataRetrival;

import java.util.List;

import org.springframework.stereotype.Service;

@Service 
public class UserService {
    private UserRepository repository;

    public UserService(UserRepository repository){
        this.repository = repository;
    }

    public List<User> getUser(){
        return repository.getUser();
    }

    public String createUser(User user){
        return repository.saveUser(user) + "\nUser Created";
    }

    public String getUser(int id){
        return repository.getUser(id);
    }

    public String getUser(String name){
        return repository.getUser(name);
    }
}
