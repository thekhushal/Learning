package com.Practice;

public class Main {
    public static void main(String[] args) {
        
        Second s = new Second();

    
    // Trying to access private attribute of second without get set
    // System.out.println(s.a);

    // Trying out get and set method to access private attributes
        s.setnum(50);

        System.out.println(s.geta());

        System.out.println(s.getb());

        System.out.println(s.sum(30)+ " = " +s.geta() + "+"+ s.getc());

        System.out.println(s.getb());
    // Trying to access private attribute of second via protected methods insted of public

        System.out.println(s.multi(5));
        

    }
}


class Second{
    private int a = 10;
    private int b;
    private int c;

    public int geta(){
        return a;
    }

    public void setnum(int num){
        this.b = num;
    }

    public int getb(){
        return b;
    }

    public int getc(){
        return c;
    }

    public int sum(){
        return a+b;
    }
    public int sum(int n){
        this.c = n;
        return a+c;
    }

    protected int multi(){
        return a*b;
    }
    protected int multi(int n){
        this.c = n;
        return a*c;
    }
}
