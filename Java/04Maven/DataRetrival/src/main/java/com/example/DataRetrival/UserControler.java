package com.example.DataRetrival;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController 
public class UserControler {
    private UserService service;

    public UserControler(UserService service){
        this.service = service;
    }

    // @GetMapping("/user")
    // public List<User> getUser(){
    //     return service.getUser();
    // }

    @PostMapping("/user")
    public String createUser(@RequestBody User user){
        return service.createUser(user);
    }

    @GetMapping("/user/{id}")
    public String getUser(@PathVariable int id){
        return service.getUser(id);
    }

    @GetMapping("/user")
    public String getUser(@RequestParam String name){
        return service.getUser(name);
    }
}
