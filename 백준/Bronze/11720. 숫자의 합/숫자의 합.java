import java.util.Scanner;
import static java.lang.System.out;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String num = sc.next();
        int sum = 0;

        for(int i = 0; i < n; i++){
            sum += num.charAt(i) - '0';
        }

        out.printf("%d", sum);

    }
}
