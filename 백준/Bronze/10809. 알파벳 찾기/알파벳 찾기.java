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

        String word = sc.next();
        int[] alpha = new int[26];

        for(int i = 0; i < 26; i++){
            alpha[i] = -1;
        }

        for(int i = 0; i < word.length(); i++){
            int index = (int)word.charAt(i) - 'a';
            if(alpha[index] == -1){
                alpha[index] = i;
            }else{
                continue;
            }
        }

        for(int num: alpha){
            out.print(num + " ");
        }

        sc.close();
    }
}