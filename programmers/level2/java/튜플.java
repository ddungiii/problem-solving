package programmers.level2.java;

import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    ArrayList<Character> seperators = new ArrayList<>(Arrays.asList('{', '}', ','));

    public int[] solution(String s) {
        ArrayList<Integer> answer = new ArrayList<Integer>();

        for (int i = 0; i < s.length(); i++) {
            if (this.seperators.contains(s.charAt(i))) {
                continue;
            }

            int[] result = this.extractNumber(s, i);
            if (!answer.contains(result[0])) {
                answer.add(result[0]);
            }
            i = result[1];
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    private int[] extractNumber(String s, int start) {
        int end = start;
        for (int i = start + 1; i < s.length(); i++) {
            if (this.seperators.contains(s.charAt(i))) {
                break;
            }

            end = i;
        }

        String numberString = s.substring(start, end + 1);
        int number = Integer.parseInt(numberString);

        int[] result = { number, end };
        return result;
    }
}
