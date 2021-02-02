package M1.OO_Prog.TDs.tempWater;

import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

public class Water extends Temperature {
    public String getState(){
        if (getTemperature() <= 0)
            return "Ice";
        else if (getTemperature() < 100)
            return "Liquid";
        else
            return "Vapour";
    }
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("temperature ?");
        Water eau = new Water();
        eau.setTemperature(in.nextDouble());
        System.out.println(eau.getState());
    }
}
