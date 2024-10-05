public class Part3 {
    public boolean twoOccurrences(String a, String b) {
        int occurenceCount = 0;
        while (true) {
            int indexOfStringA = b.indexOf(a);
            if(indexOfStringA != -1) {
                occurenceCount++;
                b = b.substring(indexOfStringA + a.length());
            }
            
            if (occurenceCount > 1 || indexOfStringA == -1) {
                break;
            }
        }
        
        return occurenceCount > 1;
    }
    
    public String lastPart(String a, String b) {
        int indexOfA = b.indexOf(a);
        if(indexOfA != -1) {
            return b.substring(indexOfA + a.length());
        }
        
        return b;
    }
    
    public void testingTwoOccurences() {
        String strA = "b";
        String strB = "banana";
        
        System.out.println("Two Occurences " + twoOccurrences(strA, strB));
        System.out.println("Last Part " + lastPart(strA, strB));
    }
    
    public static void main (String[] args) {
        Part3 p3 = new Part3();
        
        p3.testingTwoOccurences();
    }
}
