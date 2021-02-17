package M1.OO_Prog.Helsinki.CreatingClasses;

public class Person {
    // private means variables are hidden inside the object, encapsulation
    private String name;
    private int age;
    private int weight;
    private int height;

    public Person(String initialName){
        this.age = 0;
        this.weight = 0;
        this.height = 0;
        this.name = initialName;
    }
    // "this" sets the instance variable age of the newly created object    

    public String toString(){
        return this.name + ", age " + this.age + " years, my body mass index is " + this.bodyMassIndex();
    }
    // public; intended to be visible to the public
    // void; does not return a value

    // static; method does not belong to an object 
    // thus cannot be used to access any variables that belong to 
    // objects

    public void setHeight(int newHeight){
        this.height = newHeight;
    }

    public void setWeight(int newWeight){
        this.weight = newWeight;
    }

    public void growOlder(){
        if (this.age < 30){
            this.age = this.age + 1;  
        }    
    }

    public int returnAge(){
        return this.age;
    }

    public boolean ofLegalAge(){
        return this.age >= 18;
    }

    public String getName(){
        return this.name;
    }

    public int getAge(){
        return this.age;
    }

    public double bodyMassIndex(){
        double heightPerHundred = this.height/100.0;
        return this.weight / (heightPerHundred * heightPerHundred);
    }

}
