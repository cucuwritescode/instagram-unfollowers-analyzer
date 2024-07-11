## Instagram Unfollowers Analyzer
<img width="536" alt="Screenshot 2024-07-10 at 22 20 29" src="https://github.com/cucuwritescode/instagram-unfollowers-analyzer/assets/63936029/0b8f8529-8a5b-4cae-99e5-36072f81aa86">

## Description
-  A simple Python tool that helps you identify which users you follow on Instagram do not follow you back. By analyzing the JSON data provided by Instagram’s data export tool, the script compares your list of followers and followings to generate a list of non-followers. This tool provides a simple and reliable way to manage your Instagram connections without relying on third-party apps or services that may steal your data.

## Video Demonstration
[Watch on YouTube](https://www.youtube.com/watch?v=cvJhd_C2ihA)

## Fundamental functionality
- **Load Instagram Data:** Import JSON files containing your followers and followings data.
- **Compare Lists:** Efficiently compare the lists to identify users who don't follow you back.
- **Output Results:** Display the list of non-followers in the console.

## Requirements for use
- ** Download your Instagram data (in JSON format) from Instagram's data export tool [here](https://www.instagram.com/download/request/).
- **Python 3.x
- **JSON data files exported from Instagram (These files might take a few hours to receive from Meta)

1. Clone the repository:
   ```sh
   git clone https://github.com/cucuwritescode/instagram-unfollowers-analyzer.git
   cd instagram-unfollowers
2. Install required dependencies
   ```sh
   pip3 install PyQt5 simpleaudio
3. Place your personal JSON data files (followers.json and followings.json) in the project directory.
4. Update the file paths in the compare_followers.py script to point to your JSON files if necessary.
5. Run the Application!
