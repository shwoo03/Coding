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

        boolean[] list_student = new boolean[31];
        for(int i = 0; i < 28; i ++){
            int index = sc.nextInt();
            list_student[index] = true;
        }

        for(int i = 1; i < 31; i++){
            if(list_student[i] == false){
                out.println(i);
            }
        }

        sc.close();
    }
}

