# Instagram-Follower-Tracker
#### Must be done on a desktop ####
This program takes in your personal instagram data and sorts them into 5 unique lists:
* followers
* following
* users who you don't follow back
* users who don't follow you back
* users who still haven't accepted your follow request

Here's how to use it:

1. Login to Instagram and download your data in the `JSON` format. 
    1. Navigate to `Settings` and click `Security and privacy`.
    1. Scroll down to `Data download` and click `Request download`. 
    1. Select 'JSON' as your format and click `Request download`. 
    1. You'll be sent an email titled **Your Instagram Data** (takes about 5 minutes).
    1. Click `Download information`.
2. Open the folder and click on the folder titled `followers_and_following`. Find these 3 files in the folder: `followers.json` `following.json` and `pending_follow_requests.json`.
3. Create a new folder somewhere on your computer (i.e. on your `C Drive`) and copy those 3 files into this new folder.
5. Open this new folder in VSCode and create a new file inside called "main.py", and copy into it the code of this repos main.py

6. Run main.py
