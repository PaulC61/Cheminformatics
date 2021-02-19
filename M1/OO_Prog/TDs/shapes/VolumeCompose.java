package M1.OO_Prog.TDs.shapes;

import java.util.List;

public class VolumeCompose implements Volume {
    private List<Volume> elements;

    public VolumeCompose(List<Volume> volElements){
        this.elements = volElements;

    }

    @Override
    public double getVolume() {
        double currentVol = 0;
        for(int i=0; i < this.elements.size(); i++){
            currentVol = currentVol + this.elements.get(i).getVolume();
        }
        return currentVol;
    }

    
}
