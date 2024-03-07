package programmers.level3.java;

import java.util.Arrays;

class Solution {
    public int solution(int[] stones, int k) {
        int smallest = Arrays.stream(stones).max().getAsInt();

        for (int i = 0; i < stones.length - k + 1; i++) {
            int max = Arrays.stream(stones, i, i + k).max().getAsInt();
            smallest = Math.min(smallest, max);
        }

        return smallest;
    }
}
