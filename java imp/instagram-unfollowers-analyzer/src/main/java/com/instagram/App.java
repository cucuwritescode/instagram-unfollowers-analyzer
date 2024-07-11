package com.instagram;

import java.util.List;

public class App {
    public static void main(String[] args) {
        // Paths to the JSON files
        String followersPath = "src/main/resources/followers.json";
        String followingsPath = "src/main/resources/following.json";

        // Parse JSON data
        JsonParser parser = new JsonParser();
        List<String> followers = parser.parseJson(followersPath, "text_post_app_text_post_app_followers");
        List<String> followings = parser.parseJson(followingsPath, "text_post_app_text_post_app_following");

        // Analyze non-followers
        UnfollowersAnalyzer analyzer = new UnfollowersAnalyzer();
        List<String> nonFollowers = analyzer.findNonFollowers(followers, followings);

        // Output the result
        System.out.println("Non-followers:");
        for (String nonFollower : nonFollowers) {
            System.out.println(nonFollower);
        }
    }
}