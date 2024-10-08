import os
import requests
import json

# GitHub repositories to fetch releases from
REPOSITORIES = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

# GitHub API URL for releases
GITHUB_API_URL = "https://api.github.com/repos/{repo}/releases"

# JSON file to be updated (assume it's located at the root of the repository)
ALTSTORE_JSON_PATH = "altstore_source.json"

def fetch_latest_releases():
    """
    Fetches the latest releases from the GitHub repositories.
    """
    releases = []
    for repo in REPOSITORIES:
        response = requests.get(GITHUB_API_URL.format(repo=repo))
        if response.status_code == 200:
            releases.append(response.json())
        else:
            print(f"Error fetching release for {repo}: {response.status_code} - {response.text}")
    return releases

def update_altstore_json(releases):
    """
    Updates the altstore source JSON file with the latest release data from multiple repositories.
    """
    with open(ALTSTORE_JSON_PATH, 'r') as file:
        altstore_data = json.load(file)

    for release_data in releases:
        for release in release_data:
            version = release['tag_name']
            release_notes = release['body']
            download_url = release['assets'][0]['browser_download_url']

            # Update JSON as per your needs (e.g., appending new releases)
            altstore_data.append({
                'version': version,
                'notes': release_notes,
                'url': download_url
            })

    # Write the updated JSON back to the file
    with open(ALTSTORE_JSON_PATH, 'w') as file:
        json.dump(altstore_data, file, indent=4)

    print(f"AltStore source JSON updated with {len(releases)} releases")

if __name__ == "__main__":
    try:
        latest_releases = fetch_latest_releases()
        update_altstore_json(latest_releases)
    except Exception as e:
        print(f"Error: {e}")
