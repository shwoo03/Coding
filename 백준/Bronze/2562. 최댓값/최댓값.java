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

        ArrayList<Integer> list_num = new ArrayList<>();
        for(int i = 0; i < 9; i++){
            int num = sc.nextInt();
            list_num.add(num);
        }

        int max = list_num.get(0);
        int max_index = 0;

        for(int i = 1; i < 9; i++){
            if(max < list_num.get(i)) {
                max = list_num.get(i);
                max_index = i;
            }
        }

        out.println(max);
        out.println(max_index + 1);

        sc.close();
    }
}