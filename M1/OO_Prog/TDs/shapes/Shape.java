package M1.OO_Prog.TDs.shapes;

public class Shape extends Material implements Volume  {
    String materialType;

    public Shape(String materialType) {
        super(materialType);
        this.materialType = materialType;
    }

	@Override
    public double getVolume() {
        // TODO Auto-generated method stub
        return 0;
    }
    
    public double getWeight(){
        return getVolume() * getDensity();
    }

}
