import java.io.*;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;
 
public class tagTextToFile {
 
 public static void main(String[] args) throws IOException,
 ClassNotFoundException {
 
 String tagged;
 
 // Initialize the tagger
 MaxentTagger tagger = new MaxentTagger("taggers/english-left3words-distsim.tagger");
 
 // The sample string
 String sample = "i can man the controls of this machine";
 
 //The tagged string
 tagged = tagger.tagString(sample);
 
 //output the tagged sample string onto your console
 System.out.println(tagged);
 
 /* next we will pick up some sentences from a file input.txt and store the output of
 tagged sentences in another file output.txt. So make a file input.txt and write down
 some sentences separated by a new line */
 
 FileInputStream fstream = new FileInputStream("input.txt");
 DataInputStream in = new DataInputStream(fstream);
 BufferedReader br = new BufferedReader(new InputStreamReader(in));
 
 //we will now pick up sentences line by line from the file input.txt and store it in the string sample
 while((sample = br.readLine())!=null)
 {
 //tag the string
 tagged = tagger.tagString(sample);
 FileWriter q = new FileWriter("output.txt",true);
 BufferedWriter out =new BufferedWriter(q);
 //write it to the file output.txt
 out.write(tagged);
 out.newLine();
 out.close();
 }
 
}
 
}