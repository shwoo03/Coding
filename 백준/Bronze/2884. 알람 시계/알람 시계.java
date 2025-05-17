import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;



public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();
        int total_m = (h * 60) + m - 45;

        if(total_m < 0){
            total_m += 1440;
        }

        h = total_m / 60;
        total_m = total_m % 60;
        m = total_m;

        out.printf("%d %d",h, m);

        sc.close();
    }
}