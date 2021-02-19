package M1.OO_Prog.TDs.shapes;

public class Pave extends Shape {
    private double length;
    private double height;
    private double depth;

    public Pave(double paveLength, double paveHeight, double paveDepth, String thisMaterial){
        super(thisMaterial);
        this.length = paveLength;
        this.height = paveHeight;
        this.depth = paveDepth;
    }

    @Override
    public double getVolume() {
        return this.length * this.height * this.depth;
    }

    public String toString(){
        return "Pave, Volume: " + getVolume();
    }

}
