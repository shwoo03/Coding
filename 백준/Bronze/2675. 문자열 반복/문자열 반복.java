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
            int len = sc.nextInt();
            String word = sc.next();

            for(int j = 0; j < word.length(); j++){
                char ch = word.charAt(j);

                for(int x = 0; x < len; x++){
                    out.print(ch);
                }
            }

            out.println();
        }

        sc.close();
    }
}