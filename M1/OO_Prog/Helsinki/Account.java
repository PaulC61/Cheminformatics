package M1.OO_Prog.Helsinki;

public class Account {
    private int amount;
    private String name;

    public int deposit(int addAmount){
        amount = amount + addAmount;
        return amount;
    }

    public int withdraw(int rmvAmount){
        amount = amount - rmvAmount;
        return amount;
    }

    public int balance(){
        return this.amount;
    }

    public String getName(){
        return this.name;
    }

    public void transfer(int trnsAmount, Account recAccount){
        amount = amount - trnsAmount;
        recAccount.deposit(trnsAmount);
    }

    public Account (String inName, int inAmount){
        name = inName;
        amount = inAmount;

    }

}
