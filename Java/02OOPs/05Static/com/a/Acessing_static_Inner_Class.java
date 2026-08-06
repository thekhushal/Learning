package com.code.a;

public class Acessing_static_Inner_Class {

    static class InnerClass{
        String name;

        // Constructor
        public InnerClass(String name){
            this.name = name;
        }
    }

    public static void main(String[] args) {
        InnerClass t = new InnerClass("Khushal");
        InnerClass b = new InnerClass("sharma");

        System.out.println(t.name);
        System.out.println(b.name);
    }
}



// public class InnerClasses {

//     static class InnerClass {
//         String name;
//         public InnerClass(String name) {
//             this.name = name;
//         }

//         // @Override
//         // public String toString() {
//         //     return name;
//         // }
//     }
// }

