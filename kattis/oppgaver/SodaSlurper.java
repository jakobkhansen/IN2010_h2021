import java.util.ArrayList;
import java.util.Scanner;

public class SodaSlurper {

    // Denne metoden løser SodaSlurper
    public static void solution(String[] lines) {
        // Del opp første linjen i deler basert på space
        String[] input = lines[0].split(" ");

        // Les inn alle tallene i variabler
        int emptyBottles = Integer.parseInt(input[0]);
        int bottlesFound = Integer.parseInt(input[1]);
        int bottlePrice = Integer.parseInt(input[2]);

        // Det har ingenting å si om man starter med bottles eller om man finner de i
        // løpet av dagen, summen er totalen flasker du har ved start uansett
        int current = emptyBottles + bottlesFound;

        // Teller for hvor mange flasker vi har kjøpt
        int bought = 0;

        // Løkke som kjøper så mange flasker vi kan
        while (current >= bottlePrice) {

            // Trekker fra antall tomflasker for å kjøpe en ny flaske
            current -= bottlePrice;

            // Kjøper en ny flaske
            bought++;

            // Drikker brusen og får en ny tomflaske
            current++;
        }

        // Outputter resultatet
        System.out.println(bought);
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

