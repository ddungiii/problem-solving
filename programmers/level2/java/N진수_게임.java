package programmers.level2.java;

class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder str = new StringBuilder();
        StringBuilder myStr = new StringBuilder();

        p -= 1; // zero indexing
        int myIndex = p;

        for (int i = 0; myStr.length() < t; i++) {
            String newStr = Integer.toString(i, n).toUpperCase();
            str.append(newStr);

            if (str.length() > myIndex) {
                myStr.append(str.charAt(myIndex));
                myIndex += m;
            }
        }

        return myStr.toString();
    }
}
