package java;

import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    int DAY_OF_MONTH = 28;

    public int[] solution(String today, String[] terms, String[] privacies) {
        // 1. create terms map.
        // key: term, value: number of day of months.
        HashMap<String, Integer> termMap = new HashMap<>();
        for (String term : terms) {
            String[] list = term.split(" ");
            termMap.put(list[0], Integer.parseInt(list[1]) * DAY_OF_MONTH);
        }

        // 2. loop privacies, and check condition
        int todayInt = dateToInt(today);

        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < privacies.length; i++) {
            String privacy = privacies[i];

            String[] list = privacy.split(" ");
            String date = list[0];
            String term = list[1];

            int dateInt = dateToInt(date);
            int expireDateInt = dateInt + termMap.get(term);

            if (todayInt >= expireDateInt) {
                answer.add(i + 1);
            }

        }

        return answer.stream().mapToInt(x -> x).toArray();
    }

    /**
     * ex) "2021.05.02" -> day
     */
    private int dateToInt(String date) {
        String[] splited = date.split("\\.");
        int year = Integer.parseInt(splited[0]);
        int month = Integer.parseInt(splited[1]);
        int day = Integer.parseInt(splited[2]);

        month += year * 12;
        day += month * DAY_OF_MONTH;

        return day;
    }
}