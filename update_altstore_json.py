import requests
import json
from github import Github

# Constants
REPOSITORIES = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

GITHUB_TOKEN = 'your_github_token_here'  # Set your GitHub token
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}
BASE_URL = "https://api.github.com/repos/"
APPS_JSON_PATH = "apps.json"

def fetch_latest_releases(repo):
    url = f"{BASE_URL}{repo}/releases/latest"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return None

def create_apps_json():
    apps_data = {
        "name": "Quantum Source",
        "identifier": "com.quarksources.quantumsource",
        "apiVersion": "v2",
        "subtitle": "Contains all of your favorite emulators, games, jailbreaks, utilities, and more.",
        "description": "This source is an automatically kept up-to-date source, powered by GitHub Actions, the Python altparse library, and the support of independent developers. In here, you'll find anything from community maintained forks of Delta Emulator, to tiny Mac utilities that no one's ever heard of. If you have an app you'd like to see here, please use our website to reach out!",
        "iconURL": "https://quarksources.github.io/assets/ElementQ-Circled.png",
        "headerURL": "https://quarksources.github.io/assets/quantumsource.png",
        "website": "https://quarksources.github.io/",
        "tintColor": "#343a40",
        "featuredApps": [],
        "apps": [],
        "userinfo": {}
    }

    for repo in REPOSITORIES:
        release_info = fetch_latest_releases(repo)
        if release_info:
            app_data = {
                "name": repo.split("/")[-1],
                "bundleIdentifier": f"com.raghav1729.{repo.split('/')[-1].lower()}",
                "developerName": "Raghav1729",
                "subtitle": f"Latest version of {repo.split('/')[-1]}.",
                "localizedDescription": release_info['body'],
                "iconURL": release_info['assets'][0]['browser_download_url'] if release_info['assets'] else "",
                "tintColor": "#5CA399",  # Default tint color
                "screenshotURLs": [],  # Add your screenshot URLs here
                "versions": [
                    {
                        "absoluteVersion": release_info['tag_name'],
                        "version": release_info['tag_name'],
                        "buildVersion": "1",  # Modify as needed
                        "date": release_info['published_at'],
                        "localizedDescription": release_info['body'],
                        "downloadURL": release_info['assets'][0]['url'] if release_info['assets'] else "",
                        "size": release_info['assets'][0]['size'] if release_info['assets'] else 0,
                        "sha256": ""  # Add your SHA256 here if available
                    }
                ],
                "appPermissions": {
                    "entitlements": [],
                    "privacy": []
                },
                "appID": f"com.raghav1729.{repo.split('/')[-1].lower()}"
            }
            apps_data['apps'].append(app_data)

    with open(APPS_JSON_PATH, 'w') as json_file:
        json.dump(apps_data, json_file, indent=4)

if __name__ == "__main__":
    create_apps_json()
