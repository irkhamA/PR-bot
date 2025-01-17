# GitHub Pull Request Automation Tool

This Python script automates the process of generating detailed pull request (PR) descriptions by combining GitHub API integration and OpenAI's GPT capabilities. The tool fetches code changes from a GitHub repository, summarizes the changes, and generates a professional PR description that can be directly used in your workflow.

---

## Features

1. **Fetch GitHub Code Changes:**

   - Retrieves commit differences between two branches using the GitHub API.
   - Summarizes changes, including file modifications, additions, deletions, and code diffs.

2. **Save Changes Locally:**

   - Code-level changes are saved in a plain text file (`code_changes.txt`).

3. **Generate PR Descriptions with AI:**

   - Uses OpenAI's GPT-4 to produce detailed and well-structured PR descriptions.
   - Descriptions include summaries, detailed changes, and suggestions for testing.

4. **Easy Integration:**
   - Outputs the PR description as a markdown file (`PR_description.md`) for direct usage in GitHub or other PR tools.

---

## Workflow Overview

1. **Input Environment Variables:**

   - Configure your GitHub and OpenAI API keys along with repository details in an `.env` file.

2. **Fetch Commit Changes:**

   - Compare two branches (e.g., a feature branch with the base branch) and fetch the code diffs.

3. **Process Changes:**

   - Save detailed code-level changes, including patch diffs, in a text file.

4. **Generate AI-Powered PR Description:**
   - Leverage OpenAI GPT to transform code changes into a professional and structured pull request description.

---

## Requirements

### 1. Software and Libraries

- **Python Version**: Python 3.8 or higher
- **Python Libraries**:
  - `requests`
  - `python-dotenv`

### 2. API Tokens

- **GitHub Token**: A personal access token with repository read permissions.
- **OpenAI API Key**: Access key for OpenAI GPT models.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install Required Libraries

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create an .env file in the project root with the following variables:

```plain text
GITHUB_TOKEN=<your_github_personal_access_token>
REPO_OWNER=<repository_owner>
REPO_NAME=<repository_name>
BRANCH_NAME=<feature_branch_name>
BASE_BRANCH=<base_branch_name>
OPENAI_API_KEY=<your_openai_api_key>
GITHUB_TOKEN: Personal access token for GitHub API.
REPO_OWNER: Username or organization name owning the repository.
REPO_NAME: Repository name.
BRANCH_NAME: Feature branch to compare changes from.
BASE_BRANCH: Base branch to compare changes against.
OPENAI_API_KEY: API key for OpenAI GPT models.
```

---

## Usage Instructions

### 1. Run the Script

Execute the script to fetch changes, process them, and generate the PR description:

```bash
python script_name.py
```

Replace script_name.py with the actual name of the script file.

### 2. Outputs

After running the script, the following files will be created:

code_changes.txt: A detailed summary of code changes.
PR_description.md: A professional PR description generated by OpenAI.

---

## GitHub Token Permissions

Ensure your GitHub token has the following permissions:

repo: To access private repositories.
read:org: To fetch data from organizational repositories (if needed).
