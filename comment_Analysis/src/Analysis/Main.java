package Analysis;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static List<String> readFileInList(String fileName) {

        List<String> lines = Collections.emptyList();
        try {
            lines = Files.readAllLines(Paths.get(fileName), StandardCharsets.UTF_8);
        }
        catch (IOException e) {
            // do something
            e.printStackTrace();
        }
        return lines;
    }

    public static void main(String[] args) {
        try {
            String prefix = "'{\n" +
                    "        \"text\":";
            String postfix = "\"features\": {\n" +
                    "        \"sentiment\": {\n" +
                    "        },\n" +
                    "        \"emotion\": true\n" +
                    "        }\n" +
                    "        }\n" +
                    "        }' \\";
            String PassToBash;
            List<String> CSVPass = new ArrayList<String>();
            CSVPass = readFileInList("Private.txt");
            String[] commands = new String[4];
            commands[0] = "watson.sh";
            commands[1] = CSVPass.get(0);
            commands[3] = CSVPass.get(1);
            CSVPass = readFileInList("CSVfile");

            for (int i = 0; i < CSVPass.size(); i++) {
                PassToBash = prefix + CSVPass.get(i) + "\",\n" + postfix;
                commands[2] = PassToBash;
                Process process = Runtime.getRuntime().exec(commands, null);

                //need to run bash file
            }
        }catch (Exception e){
            System.out.println(e.getMessage());
        }





    }
}
