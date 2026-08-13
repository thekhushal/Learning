package com.equalityHashSets;

import java.util.*;
public class Main {
    public static void main(String[] args) {
        HashSet<Books> books = new HashSet<>();

        Books b1 = new Books("Harry Potter", "J.K. Rowling");
        Books b2 = new Books("The Hobbit", "J.R.R. Tolkien");
        Books b3 = new Books("Harry Potter", "J.K. Rowling");
        Books b4 = new Books("1984", "George Orwell");

        books.addAll(List.of(b1, b2, b3, b4));

        System.out.println(books);
        System.out.println(books.size());
    }
}

class Books {
    String title;
    String author;

    Books(String title, String author){
        this.title = title;
        this.author = author;
    }
    
    @Override
    public boolean equals(Object obj){
        if (!(obj instanceof Books)){ // checks if obj is an instance of Books
            return false;
        }

        Books other = (Books) obj;
        return title.equals(other.title) && author.equals(other.author);
    }

    @Override
    public int hashCode(){
        return Objects.hash(author, title);
    }

}

/*
Two Book objects should be considered equal when both their title and author are the same.

Then:

    Override equals().
    Override hashCode() consistently.
    Create a HashSet<Book>.
    Add these books:
    "Harry Potter", "J.K. Rowling"
    "The Hobbit", "J.R.R. Tolkien"
    "Harry Potter", "J.K. Rowling"
    "1984", "George Orwell"
    Print the set.
    Print its size.

The duplicate Harry Potter should not result in two books in the set.

Use the same pattern we just learned.
*/