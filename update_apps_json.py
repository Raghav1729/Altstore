import requests
import json

# Define the repositories
repositories = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

# Prepare the base structure for apps.json
apps_json_structure = {
    "name": "Raghav Sources",
    "identifier": "com.raghavsources.raghavsources",
    "apiVersion": "v2",
    "subtitle": "Contains all of your favorite emulators, games, jailbreaks, utilities, and more.",
    "description": "This source is an automatically kept up-to-date source, powered by GitHub Actions, the Python altparse library, and the support of independent developers. In here, you'll find anything from community maintained forks of Delta Emulator, to tiny Mac utilities that no one's ever heard of. If you have an app you'd like to see here, please use our website to reach out!",
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

# Function to get releases from a repository
def get_releases(repo):
    url = f"https://api.github.com/repos/{repo}/releases"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Fetch releases and build the apps section
for repo in repositories:
    releases = get_releases(repo)
    
    # Create an app entry for each repository
    app_data = {
        "name": repo.split('/')[-1],  # Use the repo name as the app name
        "bundleIdentifier": repo.lower().replace('/', '.'),
        "developerName": repo.split('/')[0],
        "subtitle": "Latest release information",
        "localizedDescription": f"Latest releases for {repo.split('/')[-1]}.",
        "iconURL": "https://github.com/" + repo + "/blob/main/icon.png?raw=true",  # Replace with actual icon URL if available
        "tintColor": "#5CA399",
        "screenshotURLs": [],
        "versions": [],
        "appPermissions": {
            "entitlements": [],
            "privacy": []
        },
        "appID": repo.lower().replace('/', '.')
    }

    # Add version details for each release
    for release in releases:
        for asset in release.get("assets", []):
            version_data = {
                "absoluteVersion": asset["name"],
                "version": asset["name"].split('_')[1],  # Modify to get the version if follows a specific pattern
                "buildVersion": "1",  # Modify this based on your versioning
                "date": release["published_at"],
                "localizedDescription": release["body"],
                "downloadURL": asset["browser_download_url"],
                "size": asset["size"],
                "sha256": "",  # Placeholder, compute SHA256 if needed
            }
            app_data["versions"].append(version_data)

    # Append the app data to the apps list
    apps_json_structure["apps"].append(app_data)

# Write the updated structure to apps.json
with open('apps.json', 'w') as f:
    json.dump(apps_json_structure, f, indent=4)

print("apps.json updated successfully!")
