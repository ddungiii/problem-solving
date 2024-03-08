package programmers.level2.java;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        return findDistance(deliveries, pickups, cap) * 2;
    }

    private long findDistance(int[] deliveries, int[] pickups, int cap) {
        long distance = 0;

        int d = 0;
        int p = 0;
        for (int i = deliveries.length - 1; i >= 0; i--) {
            d += deliveries[i];
            p += pickups[i];
            while (d > 0 || p > 0) {
                distance += i + 1;
                d -= cap;
                p -= cap;
            }
        }
        return distance;
    }
}
