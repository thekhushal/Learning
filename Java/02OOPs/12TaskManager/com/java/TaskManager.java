package com.java;
import java.util.ArrayList;
import com.java.Task;
import com.java.TaskStatus;

public class TaskManager {
    public ArrayList<Task> tasks = new ArrayList<>();

    // 0
    public void addTask(String title){
        Task task = new Task(title);
        tasks.add(task);
    }
    
    // 1
    public void updateTask(int id, String newTitle){
        Task task = tasks.stream().filter(t -> t.getID() == id).findFirst().orElse(null);
        task.title = newTitle;
    }

    // 2
    public void updateStatus(int id, int newStatus){
        Task task = tasks.stream().filter(t -> t.getID() == id).findFirst().orElse(null);
        if (newStatus == 0){
            task.status = TaskStatus.PENDING;
        } else if (newStatus == 1){
            task.status = TaskStatus.COMPLETED;
        } else if (newStatus == 2){
            task.status = TaskStatus.IN_PROGRESS;
        } else{
            System.out.println("Invalid Input");
        }
    }

    // 3
    public void deleteTask(int id){
        Task task = tasks.stream().filter(t -> t.getID() == id).findFirst().orElse(null);
        tasks.remove(task);
    }

    // 4
    public void viewTasks(){
        System.out.println("You'r requested task list: \nID");
        for (Task task: tasks){
            System.out.println(task.id + "\tTitle : " + task.title + "\n\tStatus: " + task.status);
        }
    }

    // 5
    public void findTask(int id){
        Task task = tasks.stream().filter(t -> t.getID() == id).findFirst().orElse(null);

        System.out.println(task.id + "\t" + task.title + "\n\t" + task.status);
    }
    

    

}
