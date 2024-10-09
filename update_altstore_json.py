import requests
import json
import os

# Paths
json_file_path = 'apps.json'

# App information template
app_template = {
    "beta": False,
    "bundleIdentifier": "",
    "developerName": "",
    "category": "photo-video",
    "META": {"repoName": ""},
    "contact": {"web": ""},
    "downloadURL": "",
    "iconURL": "",
    "localizedDescription": "",
    "name": "",
    "screenshotURLs": [],
    "size": 0,
    "minOSVersion": "",
    "appPermissions": {"entitlements": [], "privacy": []},
    "subtitle": "",
    "tintColor": "",
    "version": "",
    "versionDate": "",
    "versionDescription": ""
}

# Helper function to update or add an app entry
def update_app_entry(apps, new_entry):
    for app in apps:
        if app['bundleIdentifier'] == new_entry['bundleIdentifier']:
            app.update(new_entry)
            return
    apps.append(new_entry)

# Function to fetch the latest release from GitHub
def get_latest_release(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching release for {repo}: {response.status_code}")
        return None

# Fetch latest releases for the two repositories
repos = {
    "uYouPlus": "Raghav1729/uYouPlus",  # Updated project reference
    "BHTwitter": "Raghav1729/BHTwitter"
}

apps = []
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as f:
        apps = json.load(f).get("apps", [])

for app_name, repo in repos.items():
    release = get_latest_release(repo)
    if release:
        new_app = app_template.copy()
        new_app.update({
            "name": app_name,
            "bundleIdentifier": f"com.{app_name.lower()}",
            "developerName": "arichornlover & Various Contributors",
            "downloadURL": release['assets'][0]['browser_download_url'] if release['assets'] else "",
            "version": release['tag_name'],
            "versionDate": release['published_at'],
            "versionDescription": release['body'],
            "iconURL": f"https://raw.githubusercontent.com/{repo}/master/icon.png",  # Adjust icon URL
            "subtitle": f"{app_name} is a tweak for the YouTube app.",
        })
        update_app_entry(apps, new_app)

# Save updated apps.json
output_data = {
    "apps": apps,
    "identifier": "com.uyouplusextra.source",
    "name": "uYouPlusExtra Source",
    "sourceURL": "https://raw.githubusercontent.com/arichornlover/arichornlover.github.io/main/apps.json",
    "website": "https://github.com/arichornlover/uYouEnhanced",
    "news": [],
    "userInfo": {}
}

with open(json_file_path, 'w') as f:
    json.dump(output_data, f, indent=4)

print(f"Updated {json_file_path}")
