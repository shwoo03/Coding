import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;



// 상수
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();
        String reverse_a = new StringBuilder(a).reverse().toString();
        String reverse_b = new StringBuilder(b).reverse().toString();

        int int_a = Integer.parseInt(reverse_a);
        int int_b = Integer.parseInt(reverse_b);

        if(int_a > int_b){
            out.print(int_a);
        }
        else{
            out.print(int_b);
        }


        sc.close();
    }
}