# Instagram-Follower-Tracker
#### Must be done on a desktop ####
This program takes in your personal instagram data and sorts them into 5 unique lists:
* Followers
* Following
* Users who you don't follow back
* Users who don't follow you back
* Users who still haven't accepted your follow request

Here's how to use it:

1. Login to Instagram and download your data in the `JSON` format. 
    1. Navigate to `Settings` and click `Security and privacy`.
    1. Scroll down to `Data download` and click `Request download`. 
    1. Select 'JSON' as your format and click `Request download`. 
    1. You'll be sent an email titled **Your Instagram Data** (takes about 5 minutes).
    1. Click `Download information`.
2. Open the folder and click on the folder titled `followers_and_following`. Find these 3 files in the folder: `followers.json` `following.json` and `pending_follow_requests.json`.
3. Create a new folder somewhere on your computer (i.e. on your `C Drive`) and copy those 3 files into this new folder.
4. Open this new folder in an IDE (i.e. VS Code or Replit) and also add a new file titled `main.py`. Copy the code in this repository's `main.py` and paste it in your `main.py`.
5. Run main.py and choose which list you want to access.
