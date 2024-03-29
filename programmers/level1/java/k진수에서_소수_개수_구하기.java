package java;

class Solution {
    public int solution(int n, int k) {
        // 1. convert k based number
        String str = Integer.toString(n, k);

        // 2. split numbers by 0
        String[] list = str.split("0");

        // 3. check each number is Prime.
        int answer = 0;
        for (String numStr : list) {
            if (numStr.length() == 0) {
                continue;
            }
            long num = Long.parseLong(numStr);
            if (this.isPrime(num)) {
                answer++;
            }
        }
        return answer;
    }

    // private String toKString(int n, int k) {
    // StringBuilder str = new StringBuilder();

    // while (n > 0) {
    // int digit = n % k;
    // n /= k;

    // str.insert(0, digit);
    // }

    // return str.toString();
    // }

    private boolean isPrime(long n) {
        if (n == 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}