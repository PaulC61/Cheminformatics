package M1.OO_Prog.Helsinki.CreatingClasses;

import java.math.BigDecimal;
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

    public int sum(){
        int currentSum = 0;
        for(int i=0; i<inputs.size(); i++){
            currentSum = currentSum + inputs.get(i);
        }
        return currentSum;
    }

    public int sumEven(){
        int currentEvenSum = 0;
        for(int i = 0; i<inputs.size(); i++){
            if (inputs.get(i)%2 == 0){
                currentEvenSum = currentEvenSum + inputs.get(i);
            }
        }
        return currentEvenSum;
    }

    public int sumOdd(){
        int currentOddSum = 0;
        for(int i = 0; i<inputs.size(); i++){
            if (inputs.get(i)%2 != 0){
                currentOddSum = currentOddSum + inputs.get(i);
            }
        }
        return currentOddSum;
    }

    public double average(){
        double size = inputs.size();
        return this.sum()/size;
    }

}
