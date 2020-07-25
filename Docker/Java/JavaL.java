package source_code;

import java.io.*;
import java.io.File; 
import java.io.FileWriter; 
import java.io.PrintWriter; 
import java.util.Scanner;

public class JavaL{
    static boolean myEqual(String str1, String str2) 
{ 
    if (str1.length() != str2.length()) {
        return false;
    }
    int i =0;
    while (i < str1.length()) 
    { 
        if (str1.charAt(i) != str2.charAt(i)) 
            return false; 
        i++; 
    } 
    return true; 
}  

    public static void main(String[] args) {
          String s = null;
          String ans = "0000101001001100011000010111010001100101011011000111100100100000010010010010011101101101001000000110011001100101011001010110110001101001011011100110011100100000011011000110111101101110011001010110110001111001001011000010000000001010010010010010000001100001011011010010000001100111011001010111010001110100011010010110111001100111001000000110001001101111011100100110010101100100001000000110111101100110001000000111010001101111011100100111010001110101011100100110100101101110011001110010000001110000011100100110100101101101011000010111010001100101011100110010000001100001011011000110110000100000011011110110011000100000011101000110100001100101001000000111010001101001011011010110010100101110000010100000101001000001011101000010000001101100011001010110000101110011011101000010000001001001001001110110110100100000011001000110111101101001011011100110011100100000011101000110100001100101001000000111011101101111011100100110110001100100001000000110000100100000011001100110000101110110011011110111001000100000011011010111100100100000011100000111010101101110011010010111001101101000011010010110111001100111001000000111010001101000011001010110110100101110000010100000101001001010011101010111001101110100001000000111001001100101011011010110010101101101011000100110010101110010001000000111011101100101001000000110000101110010011001010010000001100111011011110110111101100100001011100010000001001110011011110111010000100000010000110111001001110101011001010110110000001010";

        try {
            // Create a stream to hold the output
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            PrintStream ps = new PrintStream(baos);
            // IMPORTANT: Save the old System.out!
            PrintStream old = System.out;
            // Tell Java to use your special stream
            System.setOut(ps);
            // Print some output: goes to your special stream
            Process p = Runtime.getRuntime().exec("java /opt/external/app.java");

            BufferedReader stdInput = new BufferedReader(new 
                    InputStreamReader(p.getInputStream()));

            BufferedReader stdError = new BufferedReader(new 
                    InputStreamReader(p.getErrorStream()));
            // read the output from the command
                // System.out.println("StdOut:\n");
                while ((s = stdInput.readLine()) != null) {
                    System.out.println(s);
                }
            // read any errors from the attempted command
                // System.out.println("StdErr:\n");
                while ((s = stdError.readLine()) != null) {
                    System.out.println(s);
            }
            // Put things back
            System.out.flush();
            System.setOut(old);
            // Show what happened
            String res = baos.toString();
            if (myEqual(res.substring(0,res.length()-1),ans)){
                File myObj = new File("/opt/state/game_state.json");
                Scanner myReader = new Scanner(myObj);

                String c = "";
               
                while (myReader.hasNextLine()) {
                    String data = myReader.nextLine();
                    if (data.contains("checkpoint")){
                     data = data.replace("ljava","intro_menu");
                    }
                    if (data.contains("Java")){
                        data = data.strip();
                        data = data.replace("\"Java\": false","\"Java\": true");
                    }
                    c += data;
                }
                myReader.close();
                FileWriter fileWriter = new FileWriter("/opt/state/game_state.json");
                PrintWriter printWriter = new PrintWriter(fileWriter);
                printWriter.print(c);
                printWriter.close();
                System.out.println("\u001b[2J\u001b[H");
                System.out.println("Diary: ");
                System.out.println(res);
                System.out.println("\u001b[1mDamn you did it, you must be patient, and dead inside.\u001b[0m");
                System.out.println("\u001b[38;5;118mCongrats!\u001b[0m");
                System.out.println("Also you thougth I would be dumb enough to use words for my private life. Ha!");
            } else {
                
                System.out.println(res);
                System.out.println("\u001b[1mNot Quite!\u001b[0m");
            }
        }
        catch (IOException e) {
            System.out.println("exception happened - here's what I know: ");
            e.printStackTrace();
            System.exit(-1);
        }
    }

}