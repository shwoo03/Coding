import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());

        for(int i = 0; i < T; i++){
            String ox = sc.nextLine().trim();
            int score = 0;
            int inc_num = 1;

            for(int j = 0; j < ox.length(); j++){
                if(ox.charAt(j) == 'O'){
                    score += inc_num++;
                }
                else{
                    inc_num = 1;
                }
            }

            out.println(score);
        }

        sc.close();
    }
}