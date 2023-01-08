import json
with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

with open('pending_follow_requests.json') as file:
    pending = json.load(file)

#pending follow request
pending_list = []
for account in pending["relationships_follow_requests_sent"]:
    pending_list.append(account["string_list_data"][0]["value"])

#list of following
following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

#list of followers
follower_list = []
for follower in followers_json["relationships_followers"]:
    follower_list.append(follower["string_list_data"][0]["value"])

#following who don't follow back (following but now follower)
not_follow_back = []
for following in following_list:
    if not following in follower_list:
        not_follow_back.append(following)

#followers who i dont follow back (follower but not following)
i_dont_follow = []
for follower in follower_list:
    if not follower in following_list:
        i_dont_follow.append(follower)


#function to print a list
def print_list(l):
    for i in l:
        print(i)
    print("")
    return


while True:
    print("\n1: list of followers\n2: list of following\n3: followers who i don't follow back\n4: following who don't follow back\n5: still haven't accepted my follow request\n")
    lists = {"1" : follower_list, "2" : following_list, "3" : i_dont_follow, "4" : not_follow_back, "5" : pending_list}

    value = str(input("pick a list: "))
    #convert str to ascii value and check if in range 1-5
    if not ord(value) in range(49,54):
        break
    print_list(lists[value])

    go = str(input("continue(y/n)? "))
    if not go == "y":
        break