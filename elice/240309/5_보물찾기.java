import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        solution.solve(args);
    }

}

class Solution {
    HashSet<String> treasures = new HashSet<>();
    char[] directions = { 'D', 'U', 'L', 'R' };

    public void solve(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        String path = sc.nextLine();
        String[] map = new String[N];

        int startR = 0;
        int startC = 0;
        for (int i = 0; i < N; i++) {
            map[i] = sc.nextLine();

            int indexC = map[i].indexOf("S");
            if (indexC != -1) {
                startR = i + 1;
                startC = indexC + 1;
            }
        }

        findTreasures(path, 0, map, startR, startC, N);

        int x = 0;
        int y = 0;
        for (String treasure : treasures) {
            String[] position = treasure.split(" ");
            x ^= Integer.parseInt(position[0]);
            y ^= Integer.parseInt(position[1]);
        }

        System.out.println(x + " " + y);
    }

    private void findTreasures(String path, int index, String[] map, int r, int c, int N) {
        if (r < 1 || c < 1 || r > N || c > N || map[r - 1].charAt(c - 1) == '#') {
            return;
        }

        if (path.length() == index) {
            treasures.add(r + " " + c);
            return;
        }

        char ch = path.charAt(index);
        if (ch == 'D') {
            findTreasures(path, index + 1, map, r + 1, c, N);
        } else if (ch == 'U') {
            findTreasures(path, index + 1, map, r - 1, c, N);
        } else if (ch == 'L') {
            findTreasures(path, index + 1, map, r, c - 1, N);
        } else if (ch == 'R') {
            findTreasures(path, index + 1, map, r, c + 1, N);
        } else {
            for (char direction : directions) {
                StringBuilder stringBuilder = new StringBuilder(path);
                stringBuilder.setCharAt(index, direction);
                findTreasures(stringBuilder.toString(), index, map, r, c, N);
            }

        }

    }
}