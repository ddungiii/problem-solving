package java;

import java.util.ArrayList;
import java.util.Comparator;

class Tuple {

}

class Solution {
    public int[] solution(int N, int[] stages) {
        int peopleNum = stages.length;
        int[] peoples = new int[N + 1];
        for (int stage : stages) {
            peoples[stage - 1] += 1;
        }

        float[] failRates = new float[N];
        ArrayList<Integer> indices = new ArrayList<>();
        for (int i = 0; i < peoples.length - 1; i++) {
            indices.add(i + 1);
            failRates[i] = (float) peoples[i] / peopleNum;
            peopleNum -= peoples[i];
        }

        indices.sort(Comparator.comparingDouble(index -> -failRates[index - 1]));

        return indices.stream().mapToInt(Integer::intValue).toArray();
    }
}