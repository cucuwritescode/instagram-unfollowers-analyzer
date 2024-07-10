import os
import json

def load_json(file_path):
    print(f"Loading file from: {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_usernames(data):
    usernames = set()
    for item in data:
        if 'string_list_data' in item:
            usernames.add(item['string_list_data'][0]['value'])
    return usernames

def compare_following_and_followers(following_file, followers_file):
    following_data = load_json(following_file)
    followers_data = load_json(followers_file)

    # Inspect JSON structure
    print(f"Following data structure: {following_data}")
    print(f"Followers data structure: {followers_data}")

    if not following_data or not followers_data:
        print("One or both of the JSON files could not be loaded.")
        return

    following_usernames = extract_usernames(following_data)
    followers_usernames = extract_usernames(followers_data)

    non_followers = list(following_usernames - followers_usernames)
    print(f"Users who don't follow back: {non_followers}")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")

# Paths to your JSON files
following_file = os.path.join(current_dir, 'following.json')
followers_file = os.path.join(current_dir, 'followers_1.json')

print(f"Following file path: {following_file}")
print(f"Followers file path: {followers_file}")

compare_following_and_followers(following_file, followers_file)