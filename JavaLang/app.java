/** So heres the deal, I would give a fun example but this is java,
there is no fun, they are solely materialisic, and think that everything is an object.
Yes... even women. 
Those are a few reasons why I don't hang here.

But you have to help me.
I lost a file in one of those void containers and I dont want to come near here to get it out.

I need you to print the contents of the file located in: @param /opt/lost/notmydiary.txt
*/
package external;

import java.io.File; 
import java.util.Scanner;
import java.io.*;
// import stuff here probably some objects
public class app{
        public static void main(String[] args) {
        try{
        // write code using objects here
        File myObj = new File("/opt/lost/notmydiary.txt");
        Scanner myReader = new Scanner(myObj);

        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            System.out.print(data);
        }
        myReader.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }  
    }
}
