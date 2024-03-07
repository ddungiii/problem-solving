package programmers.level2.java;

import java.util.Arrays;
import java.util.Comparator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new NaturalComparator());

        return files;
    }
}

class NaturalComparator implements Comparator<String> {
    private String[] parseFile(String file) {
        String[] parts = new String[3];

        // Use regex to split the file name into HEAD, NUMBER, and TAIL parts
        String regex = "(\\D+)(\\d{1,5})(.*)";
        Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(file);

        if (matcher.find()) {
            parts[0] = matcher.group(1); // HEAD
            parts[1] = matcher.group(2); // NUMBER
            parts[2] = matcher.group(3); // TAIL
        }

        return parts;
    }

    @Override
    public int compare(String o1, String o2) {
        String[] parsed1 = parseFile(o1);
        String[] parsed2 = parseFile(o2);

        String head1 = parsed1[0].toLowerCase();
        String head2 = parsed2[0].toLowerCase();
        if (head1.compareTo(head2) != 0) {
            return head1.compareTo(head2);
        }

        int num1 = Integer.parseInt(parsed1[1]);
        int num2 = Integer.parseInt(parsed2[1]);
        System.out.println(num1);
        System.out.println(num2);

        return Integer.compare(num1, num2);
    }
}
