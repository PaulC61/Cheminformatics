package M1.OO_Prog.Helsinki.CreatingClasses;

import java.util.ArrayList;
import java.util.List;

public class Statistics {
    private int count;
    private List<Integer> inputs;

    public Statistics(){
        this.count = 0;
        this.inputs = new ArrayList<>();
    }

    public void addNumber(int number){
        this.count++;
        this.inputs.add(number);
    }

    public int getCount(){
        return this.count;
    }

    public List<Integer> getInputs(){
        return this.inputs;
    }
}
