import java.util.Scanner;
import static java.lang.System.out;
import java.io.*;


public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if(a == b && b == c && c == a){
            out.println(10000+(a * 1000));
        }
        else if((a == b) || (b == c) || (c == a)){
            if(a == b){
                out.println(1000+(a*100));
            }
            else if(b == c){
                out.println(1000+(b*100));
            }
            else{
                out.println(1000+a*100);
            }
        }
        else{
            if((a > b) && (a > c)){
                out.println(a*100);
            }
            else if((b > a) && (b > c)){
                out.println(b*100);
            }
            else{
                out.println(c*100);
            }
        }
    }
}