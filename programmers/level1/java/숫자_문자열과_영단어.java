package java;

import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int solution(String s) {
        HashMap<String, Character> word2Num = new HashMap<>();
        word2Num.put("zero", '0');
        word2Num.put("one", '1');
        word2Num.put("two", '2');
        word2Num.put("three", '3');
        word2Num.put("four", '4');
        word2Num.put("five", '5');
        word2Num.put("six", '6');
        word2Num.put("seven", '7');
        word2Num.put("eight", '8');
        word2Num.put("nine", '9');

        ArrayList<Character> answerList = new ArrayList<>();

        ArrayList<Character> word = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                StringBuilder word_str = new StringBuilder();
                for (char w : word) {
                    word_str.append(w);
                }
                String str = word_str.toString();
                if (word_str.length() > 0 && word2Num.containsKey(str)) {
                    answerList.add(word2Num.get(word_str.toString()));
                    word.clear();
                }

                answerList.add(c);
            } else {
                word.add(c);

                StringBuilder word_str = new StringBuilder();
                for (char w : word) {
                    word_str.append(w);
                }
                String str = word_str.toString();
                if (word_str.length() > 0 && word2Num.containsKey(str)) {
                    answerList.add(word2Num.get(word_str.toString()));
                    word.clear();
                }
            }
        }

        StringBuilder answer = new StringBuilder();
        for (char a : answerList) {
            answer.append(a);
        }

        return Integer.parseInt(answer.toString());
    }
}