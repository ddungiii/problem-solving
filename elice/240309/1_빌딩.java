import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        int[] buildings = Arrays.stream(sc.nextLine().split(" ")).mapToInt(i -> Integer.parseInt(i)).toArray();

        // left
        int count = 0;
        int top = 0;
        for (int i = 0; i < n; i++) {
            if (buildings[i] > top) {
                top = buildings[i];
                count++;
            }
        }
        System.out.print(count + " ");

        // right
        count = 0;
        top = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (buildings[i] > top) {
                top = buildings[i];
                count++;
            }
        }
        System.out.print(count);
    }
}