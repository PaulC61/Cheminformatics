package M1.OO_Prog.TDs.shapes;

public class Material {
    private String name;

    public Material(String materialName){
        this.name = materialName;

    }

    public double getDensity() {
        if (this.name == "Wood"){
            return 24.00;
        } else if (this.name == "Metal"){
            return 53.00;
        } else if(this.name == "Plastic"){
            return 16.00;
        } else{
            return 0.00;
        }
    }

    



}
