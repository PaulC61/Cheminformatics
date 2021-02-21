package M1.OO_Prog.TDs.Car;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Driver {
    public static void main(String[] args) {
        Radio boseBT = new Radio();
        Radio nVidia = new Radio();

        List<Radio> radios = Arrays.asList(boseBT, nVidia);

        CarWithRadio thisCar = new CarWithRadio(radios);

        System.out.println(thisCar.playMusic());
    }
    
}
