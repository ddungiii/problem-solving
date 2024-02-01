package programmers.level2.java;

import java.util.ArrayDeque;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) {
            return cities.length * 5;
        }

        ArrayDeque<String> cache = new ArrayDeque<String>();
        int takenTime = 0;

        for (String _city : cities) {
            String city = _city.toLowerCase();
            if (cache.contains(city)) {
                cache.remove(city);
                cache.add(city);
                takenTime += 1;
            } else {
                if (cache.size() == cacheSize) {
                    cache.pop();
                }
                cache.add(city);
                takenTime += 5;
            }
        }

        return takenTime;
    }
}