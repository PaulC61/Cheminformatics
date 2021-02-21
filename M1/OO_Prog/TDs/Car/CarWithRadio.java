package M1.OO_Prog.TDs.Car;

import java.util.List;

public class CarWithRadio extends Car {
    protected Radio[] carRadios;

    public CarWithRadio(Radio[] radios){
        this.carRadios = radios;
    }

    public String playMusic(){
        StringBuffer blareMusic = new StringBuffer();
        blareMusic.append("Radio's playing in car: ");
        for (Radio carRadio : carRadios){
            blareMusic.append(carRadio.playMusic());
            blareMusic.append(",");
        }
        return blareMusic.toString();
    }


}


