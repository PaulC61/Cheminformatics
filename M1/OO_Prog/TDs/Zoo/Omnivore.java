package M1.OO_Prog.TDs.Zoo;

public class Omnivore extends Animal {

    @Override
    public boolean likes(Food food) {
        return food.isPlant || food.isMeat;
    }
    
}
