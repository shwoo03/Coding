import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String words = sc.nextLine();
        words = words.trim();

        if(words.isEmpty()){
            out.println(0);
        }
        else{
            String[] words_list = words.split(" ");
            out.println(words_list.length);
        }

        sc.close();
    }
}