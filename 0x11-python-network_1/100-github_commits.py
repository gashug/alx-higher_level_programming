#!/usr/bin/python3
"""
This script lists the 10 most recent commits of a GitHub repository using the GitHub API.
It takes two arguments: the repository name and the owner name.

Usage: ./100-github_commits.py <repository name> <owner name>
"""

import requests
import sys

def get_commits(owner, repo):
    """
    Fetch the commits of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        list: A list of commits.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Error: Unable to fetch commits. Status code {response.status_code}")
        sys.exit(1)

def main():
    """
    Main function to list the 10 most recent commits.
    """
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits = get_commits(owner_name, repo_name)
    
    if len(commits) < 10:
        print(f"Warning: There are less than 10 commits in the repository.")
    
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    main()
