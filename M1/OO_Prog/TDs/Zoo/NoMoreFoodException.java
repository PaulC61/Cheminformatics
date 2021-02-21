package M1.OO_Prog.TDs.Zoo;

public class NoMoreFoodException extends ZooException {
    public NoMoreFoodException(Animal animal){
        super("can't find food for " + animal.description);
    }
    
}
