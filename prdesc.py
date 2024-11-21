import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path=".env")

# Fetch values from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
BRANCH_NAME = os.getenv("BRANCH_NAME")
BASE_BRANCH = os.getenv("BASE_BRANCH")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API Configuration
API_URL = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

def fetch_commit_changes(owner, repo, branch_name, base_branch, token):
    """Fetch commit changes from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/compare/{base_branch}...{branch_name}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

    return response.json()

def save_code_level_changes(changes, filename="code_changes.txt"):
    """Save code-level changes to a text file."""
    with open(filename, "w") as file:
        for file_change in changes['files']:
            file.write(f"File: {file_change['filename']}\n")
            file.write(f"Additions: {file_change['additions']}, Deletions: {file_change['deletions']}, Changes: {file_change['changes']}\n")
            file.write(f"Status: {file_change['status']}\n")
            if 'patch' in file_change:
                file.write("Code Diff:\n")
                file.write(file_change['patch'] + "\n")
            else:
                file.write("No code-level changes available for this file.\n")
            file.write("-" * 40 + "\n")
    print(f"Code-level changes saved to {filename}")

def get_gpt_response(messages, model="gpt-4-turbo"):
    """Send a chat message to OpenAI API and retrieve the response."""
    response = requests.post(
        API_URL,
        headers=headers,
        json={"model": model, "messages": messages, "temperature": 0.7, "max_tokens": 1500}
    )
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Error:", response.status_code, response.json())
        return None

def generate_pr_description(code_changes_file="code_changes.txt", output_file="PR_description.md"):
    """Generate a PR description from the code changes."""
    try:
        with open(code_changes_file, "r") as file:
            code_changes = file.read()
    except FileNotFoundError:
        print(f"Error: File '{code_changes_file}' not found.")
        return

    messages = [
        {"role": "system", "content": "You are a professional assistant skilled in software development."},
        {"role": "user", "content": f"Generate a detailed pull request description based on the following changes:\n\n{code_changes}"}
    ]

    response = get_gpt_response(messages)
    if response:
        with open(output_file, "w") as file:
            file.write(response)
        print(f"Pull request description saved to {output_file}")
    else:
        print("Failed to generate the PR description.")

# Main Script
if __name__ == "__main__":
    # Fetch changes from GitHub
    changes = fetch_commit_changes(REPO_OWNER, REPO_NAME, BRANCH_NAME, BASE_BRANCH, GITHUB_TOKEN)
    if changes:
        save_code_level_changes(changes)
        generate_pr_description()
