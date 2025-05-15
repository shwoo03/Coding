import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import static java.lang.System.out;
import java.io.*;



public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String input = sc.next();
        int[] alpha = new int[26];

        for(int i = 0; i < input.length(); i++){
            alpha[(int)input.charAt(i) - 'a'] += 1;
        }

        for(int i = 0; i < 26; i++){
            out.printf("%d ",alpha[i]);
        }

    }
}