import json
with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

with open('pending_follow_requests.json') as file:
    pending = json.load(file)


#list of followers
follower_list = []
count_1 = 0
for follower in followers_json["relationships_followers"]:
    follower_list.append(follower["string_list_data"][0]["value"])
    count_1 += 1

#list of following
following_list = []
count_2 = 0
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])
    count_2 += 1

#followers who i dont follow back (follower but not following)
i_dont_follow = []
count_3 = 0
for follower in follower_list:
    if not follower in following_list:
        i_dont_follow.append(follower)
        count_3 += 1

#following who don't follow back (following but now follower)
not_follow_back = []
count_4 = 0
for following in following_list:
    if not following in follower_list:
        not_follow_back.append(following)
        count_4 += 1

#pending follow request
pending_list = []
count_5 = 0
for account in pending["relationships_follow_requests_sent"]:
    pending_list.append(account["string_list_data"][0]["value"])
    count_5 += 1

#function to print a list
def print_list(l):
    print("")
    for i in l:
        print(i)
    print("")
    return


lists = {"1" : follower_list, "2" : following_list, "3" : i_dont_follow, "4" : not_follow_back, "5" : pending_list}
while True:
    print("\n1: list of followers (%s)"%(count_1))
    print("2: list of following (%s)"%(count_2))
    print("3: followers who i don't follow back (%s)"%(count_3))
    print("4: following who don't follow back (%s)"%(count_4))
    print("5: still haven't accepted my follow request (%s)\n"%(count_5))

    value = str(input("pick a list: "))
    #convert str to ascii value and check if in range 1-5
    if not ord(value) in range(49,54):
        break
    print_list(lists[value])

    go = str(input("continue(y/n)? "))
    if not go == "y":
        break