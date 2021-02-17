package M1.OO_Prog.Helsinki.CreatingClasses;

public class DecreasingCounter {
    private int value;

    public DecreasingCounter(int initialValue){
        this.value = initialValue;
    }

    public void printValue(){
        System.out.println("value: " + this.value);
    }

    public void decrement(){
        if(this.value>0){
            this.value = this.value - 1;
        }    
    }

    public void reset(){
        this.value = 0;
    }

}
