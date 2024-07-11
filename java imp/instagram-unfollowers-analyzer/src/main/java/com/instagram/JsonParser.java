package com.instagram;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class JsonParser {
    public List<String> parseJson(String filePath, String outerKey) {
        Gson gson = new Gson();
        List<String> data = new ArrayList<>();
        try (FileReader reader = new FileReader(filePath)) {
            JsonObject jsonObject = gson.fromJson(reader, JsonObject.class);
            JsonArray outerArray = jsonObject.getAsJsonArray(outerKey);
            for (JsonElement element : outerArray) {
                JsonArray stringListData = element.getAsJsonObject().getAsJsonArray("string_list_data");
                for (JsonElement stringElement : stringListData) {
                    String value = stringElement.getAsJsonObject().get("value").getAsString();
                    data.add(value);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return data;
    }
}