package M1.OO_Prog.TDs.shapes;

import java.lang.Math;

public class Cylinder extends Shape {
    private double radius;
    private double height;

    public Cylinder(double cylRadius, double cylHeight, String material){
        super(material);
        this.radius = cylRadius;
        this.height = cylHeight;
    }

    @Override
    public double getVolume() {
        return Math.pow(this.radius,2) * height * Math.PI;
    }

    @Override
    public String toString(){
        return "Cylinder: volume " + getVolume() + ", weight " + getWeight();
    }
    
}
