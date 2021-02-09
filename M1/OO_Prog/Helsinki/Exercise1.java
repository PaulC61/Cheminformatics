package M1.OO_Prog.Helsinki;

public class Exercise1 {
    public static void main(String[] args){
        Account myAccount = new Account("My account", 0);
        Account mattsAccount = new Account("Matt's account", 1000);

        mattsAccount.transfer(100, myAccount);

        System.out.println("After transfer");

        System.out.println("My account balance = " + myAccount.balance());
        System.out.println("Matt's account balance = " + mattsAccount.balance());

    }
    
}
