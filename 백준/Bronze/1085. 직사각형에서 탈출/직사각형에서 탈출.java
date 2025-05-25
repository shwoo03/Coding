import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import static java.lang.System.out;
import java.io.*;


// x,y 에 있을 때 각 변이 좌표축에 평행하고 왼쪽 아래가 0,0 오른쪽이 w,h일때
// 직사각형 경계로 가는 최솟값 구하기
// 각 x,y축을 빼서 최소값을 구하면 된다.

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();

        int x_min = Math.min((x), (w - x));
        int y_min = Math.min((y), (h - y));

        if(x_min < y_min){
            out.println(x_min);
        }else{
            out.println(y_min);
        }

        sc.close();
    }
}