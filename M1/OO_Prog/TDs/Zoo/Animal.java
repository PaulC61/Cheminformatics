package M1.OO_Prog.TDs.Zoo;

public abstract class Animal {
    String description = "Unknown animal";

    public abstract boolean likes(Food food);

    public void eats(Food food) throws BadFoodException {
        if (likes(food)){
            System.out.println(description + " eats " + food.description); 
        }else{
            throw new BadFoodException(this, food);
        }
    }

}
