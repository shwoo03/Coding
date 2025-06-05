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

        int y = sc.nextInt();

        if( (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0)){
            out.println(1);
        }else{
            out.println(0);
        }

        sc.close();
    }
}