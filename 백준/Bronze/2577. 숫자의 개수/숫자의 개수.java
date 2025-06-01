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

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int result = a * b * c;
        String str_result = Integer.toString(result);
        int[] result_list = new int[10];

        for(int i = 0; i < str_result.length(); i++){
            int index = str_result.charAt(i) - '0';
            result_list[index] += 1;
        }

        for(int num: result_list){
            out.println(num);
        }

        sc.close();
    }
}