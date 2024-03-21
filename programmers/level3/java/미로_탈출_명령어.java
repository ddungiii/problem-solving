package programmers.level3.java;

class Solution {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        int distanceC = r - x;
        int distanceR = c - y;
        int distance = Math.abs(distanceR) + Math.abs(distanceC);

        // 1. Check is Possible or not
        if (isImpossible(distance, k)) {
            return "impossible";
        }

        // 2. Get Shortest Path
        StringBuilder path = new StringBuilder();
        while (distanceR != 0 || distanceC != 0) {
            if (distanceC > 0) {
                path.append("d");
                distanceC--;
            }
            if (distanceR < 0) {
                path.append("l");
                distanceR++;
            }
            if (distanceR > 0) {
                path.append("r");
                distanceR--;
            }
            if (distanceC < 0) {
                path.append("u");
                distanceC++;
            }
        }

        // 3. Add extra path
        while (k - distance > 0) {
            distance += 2;
            if (r != n) {
                path.append("du");
            } else if (c != 1) {
                path.append("lr");
            } else if (c != m) {
                path.append("rl");
            } else {
                path.append("ud");
            }
        }

        return path.toString();
    }

    private boolean isImpossible(int distance, int k) {
        return (k - distance) % 2 != 0;
    }
}