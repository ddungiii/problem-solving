package programmers.level3.java;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Path {
    int start;
    int end;
    int length;

    public Path(int start, int end, int length) {
        this.start = start;
        this.end = end;
        this.length = length;
    }
}

class Solution {
    public int[] solution(String[] gems) {
        // 1. Get unique size
        Set<String> uniqueGems = new HashSet<>(Arrays.asList(gems));
        int uniqueSize = uniqueGems.size();

        // 2. Loop
        Set<String> set = new HashSet<>();
        Path shortestPath = new Path(0, gems.length - 1, gems.length);

        for (int i = 0; i < gems.length; i++) {
            Path path = new Path(i, gems.length - 1, gems.length - i);

            for (int j = i; j < gems.length; j++) {
                set.add(gems[j]);
                path.length = j - i + 1;

                if (path.length >= shortestPath.length) {
                    set.clear();
                    break;
                }

                if (set.size() == uniqueSize) {
                    path.end = j;

                    if (path.length < shortestPath.length) {
                        shortestPath = path;
                    }

                    set.clear();
                    break;
                }
            }

        }

        return new int[] { shortestPath.start + 1, shortestPath.end + 1 };
    }
}
