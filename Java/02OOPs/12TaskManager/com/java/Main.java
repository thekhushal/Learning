package com.java;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static TaskManager taskManager = new TaskManager();

    public static void main(String[] args) {

        Boolean tf = true;
        while (tf){
            showMenu();

            System.out.print("Choose an Option from menu: ");
            int option = sc.nextInt();
            sc.nextLine();

            switch (option) {
                case 0: // Add Task
                    addTask();                   
                    break;

                case 1: // update task ON id
                    updateTask();
                    break;
                
                case 2: // update status ON id
                    updateStatus();
                    break;

                case 3: // delete task ON id
                    deleteTask();
                    break;

                case 4: // View Task
                    viewTasks();
                    break;

                case 5: // Find Task
                    findTask();
                    break;

                case 9:
                    tf = false;
                    break;

                default:
                    System.out.println("Invalid input, please pick correct option:");
                    break;
            }
        }
    }
    
    // Menu
    private static void showMenu(){
        System.out.println("===============================");
        System.out.println("||0 -> Add Task               ||");
        System.out.println("||1 -> Update Task            ||");
        System.out.println("||2 -> Update Status          ||");
        System.out.println("||3 -> Delete Task            ||");
        System.out.println("||4 -> View Task              ||");
        System.out.println("||5 -> Find Task (via {id})   ||");
        System.out.println("||9 -> Exit                   ||");
        System.out.println("==============================="); 

    }


    // 0
    private static void addTask(){
        System.out.print("What's the task: ");
        String title = sc.nextLine();
        taskManager.addTask(title); 
    }

    // 1
    private static void updateTask(){
        System.out.print("Update Task id: ");
        int id = sc.nextInt(); 

        System.out.print("New title: ");
        String newTitle = sc.nextLine(); // Initialized new title
        sc.nextLine();

        taskManager.updateTask(id, newTitle); // Called the function
    }

    // 2
    private static void updateStatus(){
        System.out.print("Update status of task id: ");
        int id = sc.nextInt();

        System.out.print("0 - PENDING \n 1 - COMPLETED \n 2 - IN-PROGRESS\nCurrent status: ");
        int newStatus = sc.nextInt();

        taskManager.updateStatus(id, newStatus);
    }

    // 3
    private static void deleteTask(){
        System.out.print("Which Task (id): ");
        int id = sc.nextInt();

        taskManager.deleteTask(id);
    }

    // 4
    private static void viewTasks(){
        taskManager.viewTasks();
    }

    //5
    private static void findTask(){
        System.out.println("Display Task id: ");
        int id = sc.nextInt();

        taskManager.findTask(id);
    }
}


