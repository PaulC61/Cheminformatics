package M1.OO_Prog.TDs.Cafe;

public abstract class Drink {
    String description = "Unknown drink";

    public String getDescription(){
        return this.description;
    }

    public abstract double price();
}
