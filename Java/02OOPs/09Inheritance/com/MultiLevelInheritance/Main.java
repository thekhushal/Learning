package com.MultiLevelInheritance;

class Animal{
    void eat(){
        System.out.println("We eat");
    }
}

class Dog extends Animal{
    void sound(){
        System.out.println("Bark");
    }
}

class Husky extends Dog{
    void Looks(){
        System.out.println("Looks Damnnn...");
    }
}

class Shero extends Husky{
    private String owoner_name = "Khushal";
    String getowoner_name(){
        return owoner_name;
    }
}

public class Main {
    public static void main(String[] args) {
        Shero shero = new Shero();
        shero.eat();
        shero.sound();
        shero.Looks();
        System.out.println(shero.getowoner_name());
    }
}
