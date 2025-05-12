import java.util.Scanner;
import static java.lang.System.out;
import java.io.*;


public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int total = sc.nextInt();
        int num = sc.nextInt();
        int result = 0;

        for(int i = 0; i < num; i++){
            int price = sc.nextInt();
            int x = sc.nextInt();
            result += price * x;
        }

        if(result == total){
            out.println("Yes");
        }else{
            out.println("No");
        }
    }
}