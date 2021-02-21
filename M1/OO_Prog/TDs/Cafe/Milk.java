package M1.OO_Prog.TDs.Cafe;

public class Milk extends DecorativeIngredient {
    Drink drink;

    public Milk(Drink drinkIn){
        this.drink = drinkIn;

    }

    @Override
    public String getDescription() {
        return "Milk, " + drink.getDescription();
    }

    @Override
    public double price() {
        return 0.4 + drink.price();
    }

    
}
