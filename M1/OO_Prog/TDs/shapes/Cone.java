package M1.OO_Prog.TDs.shapes;

public class Cone extends Cylinder {

    public Cone(double cylRadius, double cylHeight, String material) {
        super(cylRadius, cylHeight, material);
    }

    @Override
    public double getVolume(){
        double three = 3;
        return super.getVolume()/three;
    }

    @Override
    public String toString(){
        return "Cone: volume " + getVolume();
    }
    
}
