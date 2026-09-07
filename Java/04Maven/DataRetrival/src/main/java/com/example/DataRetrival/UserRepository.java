package com.example.DataRetrival;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

@Repository 
public class UserRepository {
    User user;

    public List<User> getUser(){
        List<User> users = new ArrayList<>();

        users.add(new User(1, "Khushal"));
        users.add(new User(2, "HeHe"));
        users.add(new User(3, "HaHa"));
        return users;
    }

    public String saveUser(User user){
        System.out.println("Saving" + user.getName());
        return "Saving " + user.getName();
    }

    public String getUser(int id){
        return switch(id){
            case 1 -> "a";
            case 2 -> "b";
            case 3 -> "c";
            case 4 -> "d";
            default -> "hehe";
        };
    }

    public String getUser(String name){
        return switch (name) {
            case "a" -> name + "-> 1";
            case "b" -> name + "-> 2";
            case "c" -> name + "-> 3";
            default -> "Maybe not today";
        };
    }
}

