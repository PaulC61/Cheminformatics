package M1.OO_Prog.TDs.Cafe;

public class Caramel extends DecorativeIngredient {
    Drink drink;

    public Caramel(Drink drinkIn){
        this.drink = drinkIn;
    }

    @Override
    public String getDescription() {
        return "Caramel, " + drink.getDescription();
    }

    @Override
    public double price() {
        return 0.60 + drink.price();
    }

    
    
}
