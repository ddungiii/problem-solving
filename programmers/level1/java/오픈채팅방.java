package java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<String> solution(String[] record) {
        HashMap<String, String> usernameMap = new HashMap<>();
        HashMap<String, String> actionMap = new HashMap<>();
        actionMap.put("Enter", "들어왔습니다.");
        actionMap.put("Leave", "나갔습니다.");
        List<String> answer = new ArrayList<>();

        for (String rr : record) {
            String[] message = rr.split(" ");
            String action = message[0];
            String userid = message[1];
            if (action.equals("Leave")) {
                continue;
            }
            String username = message[2];

            usernameMap.put(userid, username);
        }

        for (String rr : record) {
            String[] message = rr.split(" ");
            String action = message[0];
            String userid = message[1];
            if (action.equals("Change")) {
                continue;
            }

            answer.add(usernameMap.get(userid) + "님이 " + actionMap.get(action));
        }

        return answer;
    }
}
