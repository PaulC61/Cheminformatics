import javax.lang.model.util.ElementScanner6;

public class EauChaudeS {
    static final double ZERO_K = -273.15;
    static double pointFusion = 0;
    static double pointEbulition = 100;
    double temp;

    String etat() {
        if (temp <=EauChaudeS.pointFusion)
            return "glacon";
        else if (this.temp < pointEbulition)
            return "liquide";
        else
            return "vapeur";

    }

    public static void main(String[] args){
        EauChaudeS eau1 = new EauChaudeS();
        EauChaudeS eau2 = new EauChaudeS();

        eau1.temp = 25; eau2.temp = -5;
        System.out.println(eau1.etat());
        System.out.println(eau2.etat());
    }

}