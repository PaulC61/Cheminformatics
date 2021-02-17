package M1.OO_Prog.Helsinki.CreatingClasses;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Person ada = new Person("Ada");
        Person martin = new Person("Martin");

        Whistle duckWhistle = new Whistle("Kvaak");
        Whistle roosterWhistle = new Whistle("Peef");

        duckWhistle.sound();
        roosterWhistle.sound();
        duckWhistle.sound();

        Door alexander = new Door();

        alexander.knock();
        alexander.knock();

        Product banana = new Product("Banana", 1.1, 13);

        banana.printProduct();
        
        ada.growOlder();
        ada.growOlder();


        martin.growOlder();

        DecreasingCounter counter = new DecreasingCounter(10);

        counter.printValue();
        counter.decrement();
        counter.printValue();
        
        Debt mortgage = new Debt(120000.0, 1.20);
        mortgage.printBalance();
        mortgage.waitOneYear();
        mortgage.printBalance();

        int years = 0;
        while (years < 20) {
            mortgage.waitOneYear();
            years = years + 1;
        }

        mortgage.printBalance();

        Teacher teacher = new Teacher();
        int grading = teacher.grade();
        System.out.println("The grade received is " + grading);

        Teacher first = new Teacher();
        Teacher second = new Teacher();
        Teacher third = new Teacher();

        double average = (first.grade() + second.grade()+ third.grade())/3;

        System.out.println("Grading average " + average);

        int combined = ada.returnAge() + martin.returnAge();
        System.out.println("Ada's age " + ada.returnAge());
        System.out.println("Martin's age " + martin.returnAge());
        System.out.println("Ada and Martin's combined age " + combined);

        Song garden = new Song("In The Garden", 10910);
        System.out.println("The song " + garden.name() + " has a length of " + garden.length() + " seconds.");

        Film chipmunks = new Film("Alvin and the Chipmunks: The Squeakquel",0);

        Scanner reader = new Scanner(System.in);

        System.out.println("How old are you?");
        int age = Integer.valueOf(reader.nextLine());

        if (age>=chipmunks.ageRating()){
            System.out.println("You may watch the film " + chipmunks.name());
        } else {
            System.out.println("You may not watch the film " + chipmunks.name());
        }


        int i = 0;
        while (i<30){
            ada.growOlder();
            i = i + 1;
        }

        if (ada.ofLegalAge()){
            System.out.println(ada.getName() + " is of legal age.");
            
        } else {
            System.out.println(ada.getName() + " is underage.");
          
        }

        if (martin.ofLegalAge()){
            System.out.println(martin.getName() + " is of legal age.");
        } else {
            System.out.println(martin.getName() + " is underage.");
        }

        Gauge g = new Gauge();

        while(!g.full()){
            System.out.println("Not full! Value: " + g.value());
            g.increase();
        }

        System.out.println("Full! Value: " + g.value());
        g.decrease();
        System.out.println("Not full! Value: " + g.value());

        System.out.println(ada);
        System.out.println(martin);

        Agent clarke = new Agent ("Paul","Clarke");

        clarke.toString();
        System.out.println(clarke);

        Agent ionic = new Agent("Ionic","Bond");
        System.out.println(ionic);

        ada.setHeight(180);
        ada.setWeight(86);

        martin.setHeight(173);
        martin.setWeight(71);
        System.out.println(ada.getName() + ", body mass index is " + ada.bodyMassIndex());
        System.out.println(martin.getName() + ", body mass index is " + martin.bodyMassIndex());

        Multiplier multiplyByThree = new Multiplier(3);
        System.out.println("multiplyByThree.multiply(2): " + multiplyByThree.multiply(2));

        Statistics statistics = new Statistics();
        statistics.addNumber(3);
        statistics.addNumber(5);
        System.out.println("Count: "+ statistics.getCount());
    }
}
