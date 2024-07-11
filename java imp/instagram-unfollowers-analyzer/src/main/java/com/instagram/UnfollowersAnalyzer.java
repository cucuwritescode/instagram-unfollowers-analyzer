package com.instagram;

import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class UnfollowersAnalyzer {
    public List<String> findNonFollowers(List<String> followers, List<String> followings) {
        Set<String> followerSet = new HashSet<>(followers);
        List<String> nonFollowers = new ArrayList<>();
        for (String following : followings) {
            if (!followerSet.contains(following)) {
                nonFollowers.add(following);
            }
        }
        return nonFollowers;
    }
}