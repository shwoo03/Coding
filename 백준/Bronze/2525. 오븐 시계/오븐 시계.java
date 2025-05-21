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

        int h = sc.nextInt();
        int m = sc.nextInt();
        int need = sc.nextInt();

        int total_m = (h * 60) + m + need;
        h = total_m / 60;
        m = total_m % 60;
        if(h >= 24){
            h -= 24;
        }

        out.printf("%d %d", h, m);
        sc.close();
    }
}

