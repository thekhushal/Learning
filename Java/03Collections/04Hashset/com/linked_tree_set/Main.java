    package com.linked_tree_set;

    import java.util.HashSet;
    import java.util.LinkedHashSet;
    import java.util.Set;
    import java.util.TreeSet;

    public class Main {

        public static void main(String[] args) {
            
            Set<Integer> hash = new HashSet<>();
            Set<Integer> linked = new LinkedHashSet<>();
            Set<Integer> tree = new TreeSet<>();

            int[] nums = {50, 20, 40, 20, 10, 50, 30};

            for (int num : nums){
                hash.add(num);
                linked.add(num);
                tree.add(num);
            }

            System.out.println("The HashSet: " + hash);
            System.out.println("The LinkedSet: " + linked);
            System.out.println("The TreeSet: " + tree);

            System.out.println("---------------------------------\n");
            System.out.println("Size of HashSet: " + hash.size());
            System.out.println("Size of LinkedSet: " + linked.size());
            System.out.println("Size of TreeSet: " + tree.size());

            System.out.println("-------------------------\n");
            System.out.println("First Element of TreeSet: " + ((TreeSet<Integer>) tree).first());
            System.out.println("Last Element of TreeSet: " + ((TreeSet<Integer>) tree).last());
        }

}

/*
Then print:

    All three sets.
    The size of each set.
    The first element of the TreeSet.
    The last element of the TreeSet.
*/