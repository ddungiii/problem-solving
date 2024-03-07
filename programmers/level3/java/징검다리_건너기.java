package programmers.level3.java;

import java.util.Arrays;

class Solution {
    public int solution(int[] stones, int k) {
        // 1. Find number of people using binary search (parametic search)
        int max = Arrays.stream(stones).max().getAsInt();
        int min = Arrays.stream(stones).min().getAsInt();

        // 2. Check the number is OK. (can cross the stones)
        while (min < max) {
            int mid = (max + min + 1) / 2;

            if (canCross(stones, k, mid)) {
                min = mid;
            } else {
                max = mid - 1;
            }
        }

        return max;
    }

    private boolean canCross(int[] stones, int k, int n) {
        int count = 0;
        for (int stone : stones) {
            if (stone - n < 0) {
                count++;
            } else {
                count = 0;
            }

            if (count == k) {
                return false;
            }
        }

        return true;
    }
}
