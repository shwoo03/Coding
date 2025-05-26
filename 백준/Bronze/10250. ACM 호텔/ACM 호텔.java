import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;





// ACM 호텔에서 각 층에 W개 방이 있고 H층이라고 하자
// 낮은 층일 수록 선호하고 그 다음은 호수를 본다.
// 층 수는 N % H 하면 되고 방 번호는 N // H + 1 하면 된다. (N%H==0)이면 N//H만 하면 됨

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i = 0; i < T; i++){
            int H = sc.nextInt();
            int W = sc.nextInt();
            int N = sc.nextInt();
            int floor;
            int room;

            if (N % H == 0) {
                floor = H;
                room = N / H;
            } else {
                floor = N % H;
                room = N / H + 1;
            }

            out.println(floor * 100 + room);
        }

        sc.close();
    }
}