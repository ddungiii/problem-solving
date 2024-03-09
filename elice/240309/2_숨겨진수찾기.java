import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        input = input.replaceAll("[a-zA-Z]", " ");

        String[] nums = input.split(" ");
        long answer = 0;
        for (String num : nums) {
            if (num.trim().isEmpty()) {
                continue;
            }

            answer += Long.parseLong(num);
        }

        System.out.println(answer);
    }
}