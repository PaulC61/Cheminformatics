package M1.OO_Prog.TDs.Cafe;

public class Chocolat extends DecorativeIngredient {
    Drink drink;

    public Chocolat(Drink drinkIn){
        this.drink = drinkIn;
    }


    @Override
    public String getDescription() {
        return "Chocolate, " + drink.getDescription() ;
    }

    @Override
    public double price() { 
        return 0.20 + drink.price();
    }
    
}
