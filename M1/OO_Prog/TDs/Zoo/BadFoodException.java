package M1.OO_Prog.TDs.Zoo;

public class BadFoodException extends ZooException {
    public BadFoodException(Animal animal, Food food){
        super(food + " is bad for " + animal);
    }
}
