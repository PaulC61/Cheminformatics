package M1.OO_Prog.Helsinki.CreatingClasses;

public class Multiplier {
    private int number;

    public Multiplier(int multNumber){
        this.number = multNumber;
    }

    public int multiply(int inputNumber){
        return inputNumber * this.number;
    }
    
}
