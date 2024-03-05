package java;

import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        ArrayList<String> answer = new ArrayList<String>();

        for (int i = 0; i < arr1.length; i++) {
            HashMap<Integer, Boolean> b1 = this.intToBinary(n, arr1[i]);
            HashMap<Integer, Boolean> b2 = this.intToBinary(n, arr2[i]);

            String merged = this.mergeBinaries(b1, b2, n);
            answer.add(merged);
        }

        return answer.toArray(new String[0]);
    }

    private HashMap<Integer, Boolean> intToBinary(int n, int map) {
        HashMap<Integer, Boolean> binary = new HashMap<>();

        String binaryString = Integer.toBinaryString(map);
        for (int i = 0; i < binaryString.length(); i++) {
            char bit = binaryString.charAt(binaryString.length() - i - 1);
            int bitInt = Integer.parseInt(String.valueOf(bit));
            if (bitInt > 0) {
                binary.put(i, true);
            }
        }

        return binary;
    }

    private String mergeBinaries(HashMap<Integer, Boolean> b1, HashMap<Integer, Boolean> b2, int n) {
        StringBuilder merged = new StringBuilder();

        for (int i = n - 1; i >= 0; i--) {
            boolean n1 = b1.getOrDefault(i, false);
            boolean n2 = b2.getOrDefault(i, false);

            if (n1 || n2) {
                merged.append("#");
            } else {
                merged.append(" ");
            }
        }

        return merged.toString();
    }
}