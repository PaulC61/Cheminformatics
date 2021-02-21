package M1.OO_Prog.TDs.Zoo;

public class Carnivore extends Animal {

    @Override
    public boolean likes(Food food) {
        return food.isMeat;
    }
    
}
