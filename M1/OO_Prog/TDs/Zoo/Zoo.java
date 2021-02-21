package M1.OO_Prog.TDs.Zoo;

public class Zoo {
    Animal[] allAnimals;

    public Zoo(Animal... animalsIn){
        allAnimals = animalsIn;
    }


    public static void main(String[] Args)  {
        Zoo zoo = new Zoo(new Monkey(), new Lion(), new Elephant());
        zoo.feedAll(new Banana(), new Fish(), new Carrot());
        
    }

    public void feed(Animal animal, Food... foods) throws ZooException {
        for(int i = 0; i < foods.length; i++)
            if (foods[i] != null && animal.likes(foods[i])){
                animal.eats(foods[i]);
                foods[i] = null;
                return;
            }
            throw new NoMoreFoodException(animal);
        
    }

    public void feedAll(Food... allFood) {
        for(Animal theAnimal : allAnimals){
            try{
                feed(theAnimal, allFood);
            }catch (ZooException e){
                System.err.println(e.getMessage());
            }
        }
    }

    // public String feedAll(Food... allFood) throws ZooException{
    //     StringBuffer letThemEat = new StringBuffer();
    //     for (int i = 0; i < allFood.length; i++){
    //         for (Animal theAnimal : allAnimals){
    //             if (theAnimal.likes(allFood[i]) && allFood != null){
    //                 letThemEat.append("\n" + theAnimal.eats(allFood[i]));
    //                 allFood[i] = null;
    //             }
    //         }
    //     }
    //     return letThemEat.toString();
    //     throw new NoMoreFoodException();
    // }


}
