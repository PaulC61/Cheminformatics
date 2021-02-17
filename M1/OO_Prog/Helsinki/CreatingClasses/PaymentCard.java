package M1.OO_Prog.Helsinki.CreatingClasses;

public class PaymentCard {
    private double balance;

    public PaymentCard(double openingBalance){
        this.balance = openingBalance;
    }

    public String toString(){
        return "Balance: " + this.balance;
    }

    public void eatAffordably(){
        if (this.balance >= 2.60){
            this.balance = this.balance - 2.60;
        }
    }

    public void eatHeartily(){
        if (this.balance >= 4.60){
            this.balance = this.balance - 4.60;
        }
    }

    public void addMoney(double amount){
        if (this.balance + amount >= 150){
            this.balance = 150.0;
        } else {
            this.balance = this.balance + amount;
        }
    }
    
}
