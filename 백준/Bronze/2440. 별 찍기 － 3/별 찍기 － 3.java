import java.util.Scanner;
import static java.lang.System.out;
import java.io.*;



public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for(int i = 0; i < N; i++){
            for(int j = N; j > i; j--){
                out.print("*");
            }

            out.println();
        }
    }
}