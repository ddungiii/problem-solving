package programmers.level2.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    double[] discounts = { 0.1, 0.2, 0.3, 0.4 };
    ArrayList<double[]> cases = new ArrayList<>();

    public int[] solution(int[][] users, int[] emoticons) {
        ArrayList<int[]> answers = new ArrayList<>();

        // 1. Create All Possible Discount Case in Emoticons.
        getAllCases(emoticons, 0, "");

        // 2. Calculate Subscibers, Profits.
        for (double[] discountCase : cases) {
            int[] result = new int[2]; // { subscribers, profit }

            for (int[] user : users) {
                int userRate = user[0];
                int userBudget = user[1];

                int buy = 0;
                for (int i = 0; i < discountCase.length; i++) {
                    double discount = discountCase[i];
                    if (discount * 100 >= userRate) {
                        buy += emoticons[i] * (1 - discount);
                    }
                }

                if (buy >= userBudget) {
                    result[0]++;
                } else {
                    result[1] += buy;
                }
            }

            answers.add(result);
        }

        // 3. Sort subscribers, profits.
        answers.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                int compare1 = Integer.compare(o1[0], o2[0]);
                if (compare1 != 0) {
                    return -compare1;
                }

                int compare2 = Integer.compare(o1[1], o2[1]);
                if (compare2 != 0) {
                    return -compare2;
                }

                return 0;
            }
        });

        return answers.get(0);
    }

    private void getAllCases(int[] emoticons, int index, String str) {
        if (index == emoticons.length) {
            double[] discountCase = Arrays.stream(str.split(",")).mapToDouble(x -> Double.parseDouble(x)).toArray();
            cases.add(discountCase);
            return;
        }

        for (double discount : discounts) {
            getAllCases(emoticons, index + 1, str.length() > 0 ? str + "," + discount : str + discount);
        }
    }

    private void printIntArray(int[] array) {
        for (int a : array) {
            System.out.print(a + " ");
        }
        System.out.println();
    }

    private void printDoubleArray(double[] array) {
        for (double a : array) {
            System.out.print(a + " ");
        }
        System.out.println();
    }
}