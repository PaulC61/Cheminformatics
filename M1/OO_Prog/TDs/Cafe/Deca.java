package M1.OO_Prog.TDs.Cafe;

public class Deca extends Drink {
    
    public Deca(){
        this.description = "Decaf";
    }

    @Override
    public double price(){
        return 1.05;
    }
}
