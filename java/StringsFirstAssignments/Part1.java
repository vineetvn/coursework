public class Part1 {
    public String findSimpleGene (String dna) {
        int startCodonIndex = dna.toLowerCase().indexOf("ATG".toLowerCase());
        if (startCodonIndex == -1) {
            return "";
        }
    
        int stopCodonIndex = dna.toLowerCase().indexOf("TAA".toLowerCase(), startCodonIndex + 3);
        if (stopCodonIndex == -1) {
            return "";
        }
        
        
        String simpleGene = dna.substring(startCodonIndex+3, stopCodonIndex);
        if (simpleGene.length() % 3 == 0) {
            return simpleGene;
        }
        
        return "";
    }
    
    public void testSimpleGene () {
        String dna = "AAATGCCCTAACTAGATTAAGAAACC";
        String simpleGene = findSimpleGene(dna);
        if(simpleGene == "") {
            System.out.println("No gene found");
        }
        System.out.println("Gene Found " + simpleGene);
    }
    
    public static void main (String[] args) {
        Part1 p1 = new Part1();
        
        p1.testSimpleGene();
    }
}
