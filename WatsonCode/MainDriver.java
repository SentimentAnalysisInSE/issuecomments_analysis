import java.io.*;
import java.util.*;
import java.nio.file.*;
class MainDriver {

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

    private void sendPost() throws Exception {

        HttpPost post = new HttpPost("readfromprivate");

        // add request parameter, form parameters
        List<NameValuePair> urlParameters = new ArrayList<>();
        urlParameters.add(new BasicNameValuePair("API", "abc"));

        post.setEntity(new UrlEncodedFormEntity(urlParameters));

        try (CloseableHttpClient httpClient = HttpClients.createDefault();
             CloseableHttpResponse response = httpClient.execute(post)) {

            System.out.println(EntityUtils.toString(response.getEntity()));
        }

    }

}

    public static void main(String[] args) {

        String CSVHolder;
        List<String> CSVPass = readFileInList("csvname");




    }
}
