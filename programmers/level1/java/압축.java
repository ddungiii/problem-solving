package java;

import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int[] solution(String msg) {
        ArrayList<Integer> answer = new ArrayList<>();

        // 1. init dictionary.
        HashMap<String, Integer> dict = createDictionary();
        int next = 27;

        // 2. for string, find or insert.
        StringBuilder strBuilder = new StringBuilder();
        for (int i = 0; i < msg.length(); i++) {
            String before = strBuilder.toString();
            strBuilder.append(msg.charAt(i));
            String str = strBuilder.toString();

            if (dict.containsKey(str)) {
                if (i == msg.length() - 1) {
                    answer.add(dict.get(str));
                }
                continue;
            }
            answer.add(dict.get(before));

            dict.put(str, next);

            next++;
            i--;
            strBuilder.setLength(0);
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    private HashMap<String, Integer> createDictionary() {
        HashMap<String, Integer> dict = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            char c = (char) ('A' + i);
            dict.put(String.valueOf(c), i + 1);
        }
        return dict;
    }
}