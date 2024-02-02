package programmers.level2.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] solution(String s) {
        ArrayList<Integer> answer = new ArrayList<Integer>();

        String trimmed = s.substring(2, s.length() - 2);
        String[] splited = trimmed.split("\\},\\{");

        ArrayList<int[]> sets = new ArrayList<>();
        for (String setString : splited) {
            String[] elements = setString.split(",");
            int[] intArray = Arrays.stream(elements).mapToInt(Integer::parseInt).toArray();
            sets.add(intArray);
        }

        sets.sort(Comparator.comparingInt(arr -> arr.length));

        for (int[] set : sets) {
            for (int num : set) {
                if (!answer.contains(num)) {
                    answer.add(num);
                }
            }
        }

        return answer.stream().mapToInt(x -> x).toArray();
    }
}
