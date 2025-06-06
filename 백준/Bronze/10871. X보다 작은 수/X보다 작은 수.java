import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;

// x보다 작은 수
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] array_num = new int[n];
        for(int i = 0; i < n; i++){
            array_num[i] = sc.nextInt();
        }

        for(int i = 0; i < n; i++){
            if(array_num[i] < x){
                out.print(array_num[i] + " ");
            }
        }


        sc.close();
    }
}