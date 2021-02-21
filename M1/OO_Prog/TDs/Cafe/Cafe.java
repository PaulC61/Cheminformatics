package M1.OO_Prog.TDs.Cafe;

public class Cafe {

    public static void main(String[] args){
        Drink drink1 = new Espresso();
        Drink drink2 = new Sumatra();

        drink1 = new Caramel(drink1);
        drink2 = new Milk(drink1);

        System.out.println(drink1.getDescription() + " " + drink1.price());

        System.out.println(drink2.getDescription() + " " + drink2.price());


    }
    
}
