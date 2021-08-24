import java.util.ArrayList;
import java.util.Scanner;

public class KattisSolution {

    // Løs oppgaven i denne metoden og output svaret med System.out.println()!
    public static void solution(String[] lines) {
    }



    // Setup, leser inn hver linje til et array
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> linesList = new ArrayList<>();

        while (scan.hasNext()) {
            linesList.add(scan.nextLine());
        }

        String[] lines = new String[linesList.size()];

        for (int i = 0; i < lines.length; i++) {
            lines[i] = linesList.get(i);
        }

        solution(lines);

        scan.close();
    }
}
