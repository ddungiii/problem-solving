package programmers.level3.java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

class Solution {

    public int[] solution(String[] gems) {
        // 1. Get size
        int size = new HashSet<>(Arrays.asList(gems)).size();

        // 2. Two pointer
        Map<String, Integer> map = new HashMap<>();
        int[] answer = new int[2];
        answer[0] = 1;
        answer[1] = gems.length;

        int shortest = gems.length;
        int start = 0;

        for (int end = 0; end < gems.length; end++) {
            map.put(gems[end], map.getOrDefault(gems[end], 0) + 1);

            while (map.size() < size) {
                end++;
                map.put(gems[end], map.getOrDefault(gems[end], 0) + 1);
            }

            while (start < end && map.get(gems[start]) > 1) {
                map.put(gems[start], map.get(gems[start]) - 1);
                start++;
            }

            if (end - start + 1 < shortest) {
                shortest = end - start + 1;
                answer[0] = start + 1;
                answer[1] = end + 1;
            }
        }

        return answer;
    }
}
