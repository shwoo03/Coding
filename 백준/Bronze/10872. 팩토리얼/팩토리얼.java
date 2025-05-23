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

        int N = sc.nextInt();
        int result = 1;

        for(int i = 1;  i < N+1; i++){
            result *= i;
        }

        out.println(result);

        sc.close();
    }
}

