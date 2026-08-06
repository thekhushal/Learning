package com.code;
class UserInfo{
    public String name = "Khushal"; // Public - accessible everywhere
    private int Salary = 0; // Private - only accessible inside this class
}
public class AccessModifiers {
    public static void main(String[] args) {
        UserInfo data = new UserInfo();

        System.out.println(data.name);
        // System.out.println(data.Salary); //error: Salary has private access in UserInfo
    }

    
}
