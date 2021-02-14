package M1.OO_Prog.Helsinki.CreatingClasses;

public class Person {
    // private means variables are hidden inside the object, encapsulation
    private String name;
    private int age;

    public Person(String initialName){
        this.age = 0;
        this.name = initialName;
    }
    // "this" sets the instance variable age of the newly created object    

    public void printPerson(){
        System.out.println(this.name + ", age " + this.age + " years");
    }
    // public; intended to be visible to the public
    // void; does not return a value

    // static; method does not belong to an object 
    // thus cannot be used to access any variables that belong to 
    // objects

    public void growOlder(){
        this.age = this.age + 1;    
    }

}
