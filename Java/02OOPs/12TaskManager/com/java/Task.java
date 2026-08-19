package com.java;

public class Task {
    private static int task_counter = 0;

    public int id;
    public String title;
    public TaskStatus status;

    public Task(String title){
        this.id = ++task_counter;
        this.title = title;
        this.status = TaskStatus.PENDING;
    }

    public int getID(){
        return id;
    }
}
