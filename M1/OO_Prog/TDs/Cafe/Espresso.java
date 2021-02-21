package M1.OO_Prog.TDs.Cafe;

public class Espresso extends Drink {
    
    public Espresso(){
        this.description = "Espresso";
    }

    @Override
    public double price(){
        return 0.75;
    }
}
