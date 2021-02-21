package M1.OO_Prog.TDs.shapes;

import java.util.List;

public class VolumeCompose implements Volume {
    private Volume[] volumes;

    public void setVolumes(Volume[] volumes){
        this.volumes = volumes;
    }


    
    // public VolumeCompose(List<Volume> volElements){
    //     this.elements = volElements;
    // }

    @Override
    public double getVolume() {
        double currentVol = 0;
        for(Volume volume : volumes){
            currentVol = currentVol + volume.getVolume();
        }
        return currentVol;
    }

    @Override
    public String toString(){
        StringBuffer detail = new StringBuffer();
        for(Volume volume : volumes){
            detail.append(volume.toString());
            detail.append(",");
        }
    }

   

    
}
