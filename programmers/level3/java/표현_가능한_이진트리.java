package programmers.level3.java;

class Solution {
    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            if (canTree(numbers[i])) {
                answer[i] = 1;
            }
        }

        return answer;
    }

    private boolean canTree(long number) {
        String str = Long.toBinaryString(number);

        // Fill leading zeros for FULL binary tree.
        long depth = getDepth(str.length());
        while (str.length() != Math.pow(2, depth) - 1) {
            str = "0" + str;
        }

        return check(str, false);
    }

    private boolean check(String tree, boolean shouldEmpty) {
        if (tree.length() == 0) {
            return true;
        }

        if (shouldEmpty && tree.contains("1")) {
            return false;
        }
        int root = tree.length() / 2;
        boolean rootEmpty = tree.charAt(root) == '0';

        boolean left = check(tree.substring(0, root), rootEmpty);
        boolean right = check(tree.substring(root + 1, tree.length()), rootEmpty);

        return left && right;
    }

    private long getDepth(int length) {
        long depth = 0;
        while (length > 0) {
            length /= 2;
            depth++;
        }

        return depth;
    }
}