import sys
import json
import urllib.request

# GitHub API URL
GITHUB_API_URL = "https://api.github.com/users/{}/events"

def fetch_github_activity(username):
    url = GITHUB_API_URL.format(username)
    
    try:
        # Make API request
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        if not data:
            print(f"No recent activity found for {username}.")
            return
        
        # Process activity data
        print(f"\n🔹 Recent Activity for {username}:\n")
        for event in data[:5]:  # Show only the latest 5 events
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            
            if event_type == "PushEvent":
                print(f"📌 Pushed commits to {repo_name}")
            elif event_type == "IssuesEvent":
                action = event["payload"]["action"]
                print(f"🐞 {action.capitalize()} an issue in {repo_name}")
            elif event_type == "WatchEvent":
                print(f"⭐ Starred {repo_name}")
            else:
                print(f"📄 {event_type} in {repo_name}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ Error: User not found.")
        elif e.code == 403:
            print("⚠️ API rate limit exceeded. Try again later.")
        else:
            print(f"❌ HTTP Error: {e.code}")
    except urllib.error.URLError:
        print("🚫 Network error. Please check your connection.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Main CLI execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    fetch_github_activity(username)

