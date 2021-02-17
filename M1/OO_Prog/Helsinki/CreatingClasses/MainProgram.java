package M1.OO_Prog.Helsinki.CreatingClasses;

public class MainProgram {
    public static void main(String[] args){
        PaymentCard card = new PaymentCard(5);
        System.out.println(card);

        card.eatAffordably();
        System.out.println(card);

        card.eatAffordably();
        System.out.println(card);

        card.eatHeartily();
        System.out.println(card);

    }
}
