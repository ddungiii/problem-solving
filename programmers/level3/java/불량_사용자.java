package programmers.level3.java;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(String[] user_id, String[] banned_id) {
        ArrayDeque<ArrayList<String>> candidates = new ArrayDeque<>();
        // 1. for banned_id, find user_id using regex
        for (String ban : banned_id) {
            ArrayList<String> candidate = new ArrayList<String>();

            for (String user : user_id) {
                if (isCandidate(user, ban)) {
                    candidate.add(user);
                }
            }

            candidates.add(candidate);
        }

        // 2. get combination numbers.
        return this.getPossibleCases(candidates, new ArrayList<>());
    }

    private boolean isCandidate(String user, String ban) {
        ban = ban.replaceAll("\\*", ".");
        return user.matches(ban);
    }

    private int getPossibleCases(ArrayDeque<ArrayList<String>> cur, ArrayList<String> acc) {
        System.out.print(cur);
        System.out.println(acc);
        if (cur.size() == 0) {
            return 1;
        }
        int total = 0;
        for (ArrayList<String> list : cur) {
            total += list.size();
        }
        if (total == 0) {
            return 1;
        }

        int result = 0;
        ArrayList<String> target = cur.pop();

        for (String name : target) {
            ArrayDeque<ArrayList<String>> new_cur = new ArrayDeque<>(cur);
            for (List<String> list : new_cur) {
                list.remove(name);
            }

            ArrayList<String> new_acc = new ArrayList<>(acc);
            if (new_acc.contains(name)) {
                continue;
            }

            new_acc.add(name);
            result += this.getPossibleCases(new_cur, new_acc);
        }

        return result;
    }
}