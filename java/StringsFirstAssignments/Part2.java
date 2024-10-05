public class Part2 {
    public String findSimpleGene (String dna, int startCodonIndex, int stopCodonIndex) {
        String simpleGene = dna.substring(startCodonIndex+3, stopCodonIndex);
        if (simpleGene.length() % 3 == 0) {
            return simpleGene;
        }
        
        return "";
    }
    
    public void testSimpleGene () {
        String dna = "atgtgatagagttaagttaa";
        int startCodonIndex = dna.toLowerCase().indexOf("ATG".toLowerCase());
        if (startCodonIndex == -1) {
            System.out.println("No gene found");
        }
    
        int stopCodonIndex = dna.toLowerCase().indexOf("TAA".toLowerCase(), startCodonIndex + 3);
        if (stopCodonIndex == -1) {
            System.out.println("No gene found");
        }
        String simpleGene = findSimpleGene(dna,startCodonIndex, stopCodonIndex);
        if(simpleGene == "") {
            System.out.println("No gene found");
        }
        System.out.println(simpleGene);
    }
    
    public static void main (String[] args) {
        Part1 p1 = new Part1();
        
        p1.testSimpleGene();
    }
}
