import requests
import json

# Define the repositories and their respective bundle identifiers
repositories = {
    "Raghav1729/BHTwitter": "com.raghav1729.bhtwitter",
    "Raghav1729/uYouPlus": "com.raghav1729.uYouPlus"
}

# Prepare the base structure for apps.json
apps_json_structure = {
    "name": "Raghav Sources",
    "identifier": "com.google.ios.youtube",  # Keeping the identifier as requested
    "apiVersion": "v2",
    "subtitle": "Contains all of build by me",
    "description": "This source is an automatically kept up-to-date source, powered by GitHub Actions, the Python altparse library, and the support of independent developers. In here, you'll find anything from community maintained forks of Delta Emulator, to tiny Mac utilities that no one's ever heard of. If you have an app you'd like to see here, please use our website to reach out!",
    "iconURL": "",  # Removed generic icon URL
    "headerURL": "",  # Removed generic header URL
    "website": "",  # Removed generic website URL
    "tintColor": "#343a40",
    "featuredApps": [
        "com.raghav1729.bhtwitter",  # Updated bundle identifier for BHTwitter
        "com.raghav1729.uYouPlus",    # Updated bundle identifier for uYouPlus
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
for repo, bundle_identifier in repositories.items():
    releases = get_releases(repo)
    
    # Create an app entry for each repository
    app_data = {
        "name": repo.split('/')[-1],  # Use the repo name as the app name
        "bundleIdentifier": bundle_identifier,  # Set the specific bundle identifier
        "developerName": repo.split('/')[0],
        "subtitle": "Latest release information",
        "localizedDescription": f"Latest releases for {repo.split('/')[-1]}.",
        "iconURL": "",  # Removed generic icon URL
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
