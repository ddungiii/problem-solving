package programmers.level2.java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

class Solution {
    private int makeInteger(double similarity) {
        System.out.println(similarity);
        return (int) (similarity * 65536);
    }

    private String makeString(char a, char b) {
        StringBuilder sb = new StringBuilder();
        sb.append(a);
        sb.append(b);

        return sb.toString();
    }

    private List<String> makeTwoGram(String str) {
        List<String> twoGram = new ArrayList<>();
        for (int i = 0; i < str.length() - 1; i++) {
            char a = str.charAt(i);
            char b = str.charAt(i + 1);

            if (!Character.isLetter(a) || !Character.isLetter(b)) {
                continue;
            }

            String s = this.makeString(a, b);
            twoGram.add(s.toLowerCase());
        }

        return twoGram;
    }

    private HashMap<String, Integer> makeCounter(List<String> list) {
        HashMap<String, Integer> hashMap = new HashMap<>();

        for (String e : list) {
            hashMap.put(e, hashMap.getOrDefault(e, 0) + 1);
        }
        return hashMap;
    }

    private double calcSimilarity(List<String> twoGram1, List<String> twoGram2) {
        System.out.println(twoGram1);
        System.out.println(twoGram2);
        if (twoGram1.size() == 0 && twoGram2.size() == 0) {
            return 1;
        }

        HashMap<String, Integer> counter1 = this.makeCounter(twoGram1);
        HashMap<String, Integer> counter2 = this.makeCounter(twoGram2);

        int and = 0;
        int or = 0;
        HashMap<String, Integer> orHashMap = new HashMap<>();

        // Calculate And
        for (Entry<String, Integer> entry : counter1.entrySet()) {
            String key = entry.getKey();
            if (counter2.containsKey(key)) {
                and += Math.min(entry.getValue(), counter2.get(key));
                orHashMap.put(key, Math.max(entry.getValue(), counter2.get(key)));
            }
        }

        // Calculate Or
        for (Entry<String, Integer> entry : counter2.entrySet()) {
            String key = entry.getKey();
            if (!orHashMap.containsKey(key)) {
                orHashMap.put(key, entry.getValue());
            }
        }
        for (Entry<String, Integer> entry : counter1.entrySet()) {
            String key = entry.getKey();
            if (!orHashMap.containsKey(key)) {
                orHashMap.put(key, entry.getValue());
            }
        }
        or += orHashMap.values().stream().mapToInt(Integer::intValue).sum();
        System.out.println(and);
        System.out.println(or);

        return (double) and / (double) or;
    }

    public int solution(String str1, String str2) {
        List<String> twoGram1 = this.makeTwoGram(str1);
        List<String> twoGram2 = this.makeTwoGram(str2);

        double similarity = this.calcSimilarity(twoGram1, twoGram2);
        return makeInteger(similarity);
    }
}