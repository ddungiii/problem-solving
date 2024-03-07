package programmers.level3.java;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    Set<String> set = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        dfs(user_id, banned_id, 0, "");
        return set.size();
    }

    private void dfs(String[] user_id, String[] banned_id, int idx, String str) {
        if (idx == banned_id.length) {
            // base condition
            char[] c = str.toCharArray();
            Arrays.sort(c);
            set.add(new String(c));
            return;
        }

        for (int i = 0; i < user_id.length; i++) {
            if (this.isCandidate(user_id[i], banned_id[idx]) && !str.contains(i + "")) {
                dfs(user_id, banned_id, idx + 1, str + i);
            }
        }
    }

    private boolean isCandidate(String user, String ban) {
        ban = ban.replaceAll("\\*", ".");
        return user.matches(ban);
    }

}