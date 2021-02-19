package M1.OO_Prog.TDs.shapes;

public class Main {
    
    public static void main(String[] args){
        Cube paulsCube = new Cube(12, "Wood");

        paulsCube.getVolume();

        System.out.println(paulsCube.toString());

        Cylinder paulsCylinder = new Cylinder(4, 10, "Plastic");

        System.out.println(paulsCylinder.toString());
        

    }



    
}
