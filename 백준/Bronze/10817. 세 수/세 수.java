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

        int[] num_list = new int[3];
        for(int i = 0; i < 3; i++){
            num_list[i] = sc.nextInt();
        }

        Arrays.sort(num_list);
        out.println(num_list[1]);

        sc.close();
    }
}

