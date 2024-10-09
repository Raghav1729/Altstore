import requests
import json

# List of repositories to fetch releases from
REPOSITORIES = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

# Base URL for the GitHub API
GITHUB_API_URL = "https://api.github.com/repos/"

# Function to fetch the latest release for a given repository
def fetch_latest_release(repo):
    response = requests.get(f"{GITHUB_API_URL}{repo}/releases/latest")
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Function to construct the apps.json structure
def create_apps_json():
    apps_data = {
        "name": "Quantum Source",
        "identifier": "com.quarksources.quantumsource",
        "apiVersion": "v2",
        "subtitle": "Contains all of your favorite emulators, games, jailbreaks, utilities, and more.",
        "description": "This source is an automatically kept up-to-date source, powered by GitHub Actions, the Python altparse library, and the support of independent developers. In here, you'll find anything from community maintained forks of Delta Emulator to tiny Mac utilities that no one's ever heard of. If you have an app you'd like to see here, please use our website to reach out!",
        "iconURL": "https://quarksources.github.io/assets/ElementQ-Circled.png",
        "headerURL": "https://quarksources.github.io/assets/quantumsource.png",
        "website": "https://quarksources.github.io/",
        "tintColor": "#343a40",
        "featuredApps": [
            "com.litritt.ignited",
            "com.example.mame4ios",
        ],
        "apps": [],
        "userinfo": {}
    }

    for repo in REPOSITORIES:
        latest_release = fetch_latest_release(repo)

        app_info = {
            "name": latest_release["name"],
            "bundleIdentifier": latest_release["id"],
            "developerName": repo.split("/")[0],
            "subtitle": latest_release["tag_name"],
            "localizedDescription": latest_release["body"],
            "iconURL": latest_release["assets"][0]["browser_download_url"] if latest_release["assets"] else "",
            "tintColor": "#5CA399",  # Default tint color
            "screenshotURLs": [asset["browser_download_url"] for asset in latest_release["assets"]],
            "versions": [
                {
                    "absoluteVersion": latest_release["tag_name"],
                    "version": latest_release["tag_name"],
                    "buildVersion": "1",
                    "date": latest_release["published_at"],
                    "localizedDescription": latest_release["body"],
                    "downloadURL": latest_release["assets"][0]["browser_download_url"],
                    "size": latest_release["assets"][0]["size"],
                    "sha256": latest_release["assets"][0]["sha256"] if "sha256" in latest_release["assets"][0] else ""
                }
            ],
            "appPermissions": {
                "entitlements": [],
                "privacy": []
            },
            "appID": latest_release["id"]
        }

        apps_data["apps"].append(app_info)

    return apps_data

# Function to save the apps.json to a file
def save_apps_json(data):
    with open("apps.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

# Main function to execute the script
def main():
    apps_json_data = create_apps_json()
    save_apps_json(apps_json_data)

if __name__ == "__main__":
    main()
