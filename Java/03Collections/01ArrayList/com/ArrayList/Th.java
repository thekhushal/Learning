package com.ArrayList;

public final class Th {

    private Th() {
    }

    public static String ordinal(int number) {

        int lastTwo = number % 100;

        if (lastTwo >= 11 && lastTwo <= 13) {
            return number + "th";
        }

        switch (number % 10) {
            case 1:
                return number + "st";
            case 2:
                return number + "nd";
            case 3:
                return number + "rd";
            default:
                return number + "th";
        }
    }
}