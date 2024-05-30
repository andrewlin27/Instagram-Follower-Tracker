import json

with open('followers_1.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

with open('pending_follow_requests.json') as file:
    pending = json.load(file)


follower_set = set()
for follower in followers_json:
    follower_set.add(follower["string_list_data"][0]["value"])


following_set = set()
for following in following_json["relationships_following"]:
    following_set.add(following["string_list_data"][0]["value"])

# follower but not following
i_dont_follow = follower_set.difference(following_set)

# following but now follower
not_follow_back = following_set.difference(follower_set)

pending_list = []
for account in pending["relationships_follow_requests_sent"]:
    pending_list.append(account["string_list_data"][0]["value"])


def print_list(l):
    print("")
    for item in l:
        print(item)
    print("")


lists = {"1" : follower_set, "2" : following_set, "3" : i_dont_follow, "4" : not_follow_back, "5" : pending_list}

while True:
    print(f"\n1: list of followers ({len(follower_set)})")
    print(f"2: list of following ({len(following_set)})")
    print(f"3: followers who i don't follow back ({len(i_dont_follow)})")
    print(f"4: following who don't follow back ({len(not_follow_back)})")
    print(f"5: still haven't accepted my follow request ({len(pending_list)})\n")

    val = input("pick a list (type q to quit): ")
    
    if val == 'q':
        break

    print_list(lists[val])