import requests
import json
import os

# Constants
REPO_1 = 'Raghav1729/BHTwitter'  # First GitHub repo
REPO_2 = 'Raghav1729/uYouPlus'    # Second GitHub repo
ALTSORE_JSON_PATH = 'altsore.json'  # Path to your altsore JSON file

def get_latest_release(repo):
    """Fetch the latest release from a GitHub repository."""
    url = f'https://api.github.com/repos/{repo}/releases/latest'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching releases from {repo}: {response.status_code}")
        return None

def update_altsore_json(new_data):
    """Update the altsore JSON file."""
    if os.path.exists(ALTSORE_JSON_PATH):
        with open(ALTSORE_JSON_PATH, 'r') as file:
            altsore_data = json.load(file)
    else:
        altsore_data = []

    # Check if the release already exists
    for release in new_data:
        if not any(r['tag_name'] == release['tag_name'] for r in altsore_data):
            altsore_data.append(release)
    
    # Save the updated data back to the JSON file
    with open(ALTSORE_JSON_PATH, 'w') as file:
        json.dump(altsore_data, file, indent=4)

def main():
    """Main function to update altsore JSON based on GitHub releases."""
    new_releases = []
    
    # Get latest releases from both repositories
    for repo in [REPO_1, REPO_2]:
        release = get_latest_release(repo)
        if release:
            new_releases.append(release)
    
    # Update the altsore JSON with new releases
    if new_releases:
        update_altsore_json(new_releases)
        print("altsore.json has been updated.")
    else:
        print("No new releases to update.")

if __name__ == '__main__':
    main()
