package M1.OO_Prog.Helsinki.CreatingClasses;

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
    
    }
}
