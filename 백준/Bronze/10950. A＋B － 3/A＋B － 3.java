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

        int T = sc.nextInt();
        for(int i = 0; i < T; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            out.println(x+y);
        }


        sc.close();
    }
}