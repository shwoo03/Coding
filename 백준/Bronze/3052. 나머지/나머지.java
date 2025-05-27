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

        int[] num_list = new int[42];
        for(int i = 0; i < 10; i ++){
            int num = sc.nextInt();
            num_list[num % 42] += 1;
        }

        int result = 0;
        for(int i = 0; i < 42; i++){
            if(num_list[i] != 0){
                result += 1;
            }
        }

        out.println(result);

        sc.close();
    }
}