package M1.OO_Prog.Helsinki.CreatingClasses;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Person ada = new Person("Ada");
        Person antti = new Person("Antti");
        Person martin = new Person("Martin");

        ada.printPerson();
        antti.printPerson();
        martin.printPerson();

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

        ada.printPerson();

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
            ada.printPerson();
        }

        if (martin.ofLegalAge()){
            System.out.println(martin.getName() + " is of legal age.");
        } else {
            System.out.println(martin.getName() + " is underage.");
        }


    }
}
