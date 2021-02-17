package M1.OO_Prog.Helsinki.CreatingClasses;

public class Agent {
    private String firstName;
    private String secondName;

    public Agent(String agentFirstName, String agentSecondName){
        this.firstName = agentFirstName;
        this.secondName = agentSecondName;
    }
    
    public String toString(){
        return "My name is " + this.secondName + ", " + this.firstName + " " + this.secondName + ".";
    }

    

}
