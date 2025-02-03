# GitHub User Activity CLI

A simple command-line tool to fetch and display recent activity of a GitHub user.

This tool allows you to see the latest activities (like pushes, issues, stars, etc.) of any GitHub user directly in your terminal.

---

## 🚀 Features

- Fetch and display recent activity of a GitHub user.
- Supports various types of events, such as:
  - **Push events** (commits to repositories)
  - **Issue events** (open, close, or comment on issues)
  - **Star events** (star repositories)
- Easy-to-use CLI interface.
- Error handling for invalid usernames and network issues.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/XIUXIU25/github_user_activity.git
cd github_user_activity
```
### 2. Run the Script
Make sure you have Python 3 installed, then run the script with the following command:
```sh
python github_activity.py <github-username>
```

## 📋 Example Output
🔹 Recent Activity for kamranahmedse:

📌 Pushed commits to kamranahmedse/developer-roadmap
🐞 Opened an issue in kamranahmedse/developer-roadmap
⭐ Starred kamranahmedse/developer-roadmap

##⚠️ Error Handling
If the GitHub username is not found, you'll see:
```sh
❌ Error: User not found.
```

If the API rate limit is exceeded, the message will be:
```sh
⚠️ API rate limit exceeded. Try again later.
```

In case of network issues, the message will be:
```sh
🚫 Network error. Please check your connection.
```

## 📝 License
This project is licensed under the MIT License.