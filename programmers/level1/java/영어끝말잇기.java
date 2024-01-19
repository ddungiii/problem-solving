package java;

import java.util.HashSet;

class Solution {
    public int[] solution(int n, String[] words) {
        HashSet<String> used = new HashSet<>();
        char lastchar = words[0].charAt(0);
        int who = 0;
        int turn = 0;

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (word.charAt(0) != lastchar || used.contains(word)) {
                who = i % n + 1;
                turn = (i / n) + 1;
                break;
            }

            used.add(word);
            lastchar = word.charAt(word.length() - 1);
        }

        int[] answer = { who, turn };
        return answer;
    }
}