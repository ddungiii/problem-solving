import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().split(" ")).mapToInt(x -> Integer.parseInt(x)).toArray();
        int n = nums[0];
        int m = nums[1];

        HashMap<String, ArrayList<String>> map = new HashMap<>();
        ArrayList<ArrayList<String>> cluster = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String[] pair = sc.nextLine().split(" ");

            String computer1 = pair[0];
            String computer2 = pair[1];

            ArrayList<String> group1 = map.get(computer1);
            ArrayList<String> group2 = map.get(computer2);

            if (group1 != null && group2 == null) {
                group1.add(computer2);
                map.put(computer2, group1);
                continue;
            } else if (group1 == null & group2 != null) {
                group2.add(computer1);
                map.put(computer1, group2);
                continue;
            } else if (group1 != null && group2 != null) {
                for (String mergeComputer : group2) {
                    if (!group1.contains(mergeComputer)) {
                        group1.add(mergeComputer);
                        map.put(mergeComputer, group1);
                    }
                }
                continue;
            }

            ArrayList<String> newGroup = new ArrayList<>();
            newGroup.add(computer1);
            newGroup.add(computer2);

            map.put(computer1, newGroup);
            map.put(computer2, newGroup);

            cluster.add(newGroup);
        }

        int largest = 0;
        for (ArrayList<String> group : cluster) {
            int size = group.size();
            if (size > largest) {
                largest = size;
            }
        }

        System.out.println(largest);
    }
}