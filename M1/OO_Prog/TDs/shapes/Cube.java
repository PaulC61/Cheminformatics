package M1.OO_Prog.TDs.shapes;

public class Cube extends Pave{

    public Cube(double paveLength, String material) {
        super(paveLength, paveLength, paveLength, material);
    }

    @Override
    public String toString(){
        return "Cube, voume: " + getVolume();
    }
}
