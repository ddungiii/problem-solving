package java;

import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            }

            if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                char l = stack.pop();
                if (l != '(') {
                    return false;
                }

            }
        }
        return stack.size() == 0;
    }
}
