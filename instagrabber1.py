import instaloader

L = instaloader.Instaloader()
L.login("aashavskiy", "mung-czech-FIST")

profile = instaloader.Profile.from_username(L.context, "your_username")

with open("followers.csv", "w") as f:
    f.write("id,username,full_name\n")
    for follower in profile.get_followers():
        f.write(f"{follower.userid},{follower.username},{follower.full_name}\n")
