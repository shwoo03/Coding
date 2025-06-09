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

        while(true){
            int a = sc.nextInt();
            int b = sc.nextInt();

            if( (a == 0) && (b == 0)){
                break;
            }
            else{
                out.println(a+b);
            }
        }


        sc.close();
    }
}