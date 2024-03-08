package programmers.level2.java;

import java.util.Arrays;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        // long deliverDistance = findDistance(deliveries, cap);
        // long pickupsDistance = findDistance(pickups, cap);

        // return Math.max(deliverDistance, pickupsDistance) * 2;
        return findDistance(deliveries, pickups, cap) * 2;
    }

    private long findDistance(int[] deliveries, int[] pickups, int cap) {
        long distance = 0;
        long deliverSum = Arrays.stream(deliveries).sum();
        long pickupSum = Arrays.stream(pickups).sum();

        while (deliverSum > 0 || pickupSum > 0) {
            int dCap = cap;
            int pCap = cap;
            for (int i = deliveries.length - 1; i >= 0; i--) {
                if (deliveries[i] > 0 && dCap > 0) {
                    if (dCap == cap && pCap == cap) {
                        // first visit
                        distance += i + 1;
                    }

                    int remove = Math.min(deliveries[i], dCap);
                    deliveries[i] -= remove;
                    dCap -= remove;
                    deliverSum -= remove;
                }

                if (pickups[i] > 0 && pCap > 0) {
                    if (dCap == cap && pCap == cap) {
                        // first visit
                        distance += i + 1;
                    }

                    int remove = Math.min(pickups[i], pCap);
                    pickups[i] -= remove;
                    pCap -= remove;
                    pickupSum -= remove;
                }

                if (dCap == 0 && pCap == 0) {
                    break;
                }
            }
        }
        return distance;
    }
}

/**
 * 테스트 1 〉 통과 (1.14ms, 82.4MB)
 * 테스트 2 〉 통과 (0.86ms, 72MB)
 * 테스트 3 〉 실패 (1.89ms, 77.3MB)
 * 테스트 4 〉 실패 (1.09ms, 72.5MB)
 * 테스트 5 〉 실패 (1.09ms, 74.5MB)
 * 테스트 6 〉 통과 (1.21ms, 80.6MB)
 * 테스트 7 〉 실패 (4.89ms, 82.9MB)
 * 테스트 8 〉 통과 (9.16ms, 70.8MB)
 * 테스트 9 〉 실패 (11.69ms, 79.7MB)
 * 테스트 10 〉 실패 (10.66ms, 80.4MB)
 * 테스트 11 〉 실패 (12.96ms, 81.9MB)
 * 테스트 12 〉 실패 (8.56ms, 68.4MB)
 * 테스트 13 〉 실패 (6.42ms, 76.1MB)
 * 테스트 14 〉 통과 (14.55ms, 89.6MB)
 * 테스트 15 〉 실패 (95.28ms, 107MB)
 * 테스트 16 〉 실패 (시간 초과)
 * 테스트 17 〉 실패 (7253.77ms, 82.7MB)
 * 테스트 18 〉 실패 (1882.61ms, 101MB)
 * 테스트 19 〉 통과 (1298.74ms, 109MB)
 * 테스트 20 〉 실패 (394.87ms, 81.4MB)
 */