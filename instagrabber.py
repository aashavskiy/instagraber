import instaloader
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SESSION_FILE = f"{USERNAME}_session"

L = instaloader.Instaloader()

session_loaded = False

# Try to load existing session
if os.path.exists(SESSION_FILE):
    try:
        L.load_session_from_file(USERNAME, SESSION_FILE)
        print("✅ Session loaded.")
        session_loaded = True
    except Exception as e:
        print(f"⚠️ Failed to load session: {e}")

# If no session, log in and save it
if not session_loaded:
    print("🔐 Logging in...")
    try:
        L.login(USERNAME, PASSWORD)
    except instaloader.TwoFactorAuthRequiredException:
        code = input("Enter 2FA code: ")
        L.two_factor_login(code)
    L.save_session_to_file(SESSION_FILE)
    print("💾 Session saved.")

# Fetch and save followers
profile = instaloader.Profile.from_username(L.context, USERNAME)

with open("followers.csv", "w") as f:
    f.write("id,username,full_name\n")
    for follower in profile.get_followers():
        f.write(f"{follower.userid},{follower.username},{follower.full_name}\n")

print("✅ Followers saved to followers.csv")
