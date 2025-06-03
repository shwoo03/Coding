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

        int[] arr = new int[5];
        for(int i = 0; i < 5; i++){
            arr[i] = sc.nextInt();
        }

        int sum = 0;
        for(int i = 0; i < 5; i++){
            sum += arr[i] * arr[i];
        }

        out.println(sum % 10);


        sc.close();
    }
}