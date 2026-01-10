def process(usernames):
    valid_users=[]
    for i in usernames:
        if len(i)<4:
            print("too short!")
            continue
        if i=="ANONYMOUS":
            print("threat detected")
            break
        if i=="":
            print("empty!")
            continue
        valid_users.append(i)
        print("new user added")
    return valid_users
usernames=["MIMI", "BOB", "OZWALD","ANONYMOUS",""]
filtered_usernames=process(usernames)
print(filtered_usernames)