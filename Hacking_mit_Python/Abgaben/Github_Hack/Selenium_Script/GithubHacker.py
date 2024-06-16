import subprocess
from github import Github
import os

# Ihr GitHub-Token hier einfügen
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'


def clone_repository(repo_url, clone_path):
    subprocess.run(['git', 'clone', repo_url, clone_path], check=True)


def scan_repository_with_trufflehog(repo_path):
    result = subprocess.run(['trufflehog', 'filesystem', '--json', repo_path], capture_output=True, text=True)
    return result.stdout


def main():
    github = Github(GITHUB_TOKEN)
    organization = github.get_organization('YOUR_ORGANIZATION_NAME')
    repos = organization.get_repos()

    for repo in repos:
        print(f"Scanning repository: {repo.full_name}")
        clone_path = f"./temp/{repo.name}"
        clone_repository(repo.clone_url, clone_path)

        scan_results = scan_repository_with_trufflehog(clone_path)
        if scan_results:
            print(f"Secrets found in {repo.full_name}:\n{scan_results}")
        else:
            print(f"No secrets found in {repo.full_name}.")

        # Repository löschen nach dem Scannen
        subprocess.run(['rm', '-rf', clone_path], check=True)


if __name__ == "__main__":
    if not os.path.exists("./temp"):
        os.makedirs("./temp")
    main()