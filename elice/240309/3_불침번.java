import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        int[] dp = new int[n + 1];

        int answer = dfs(n, 0, dp);
        System.out.println(answer);
    }

    private static int dfs(int n, int index, int[] dp) {
        if (n == index) {
            return 1;
        }

        if (dp[index] != 0) {
            return dp[index];
        }

        int result = 0;
        result += dfs(n, index + 1, dp);
        if (n - index >= 2) {
            result += dfs(n, index + 2, dp);
        }

        dp[index] = result;
        return result;
    }

    private static int count(int n) {
        int[] dp = new int[n + 1];

        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
}