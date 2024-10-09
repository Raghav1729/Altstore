import requests
import json

# Define the repositories with their corresponding bundle identifiers
repositories = {
    "Raghav1729/BHTwitter": "com.google.ios.youtube",
    "Raghav1729/uYouPlus": "com.atebits.Tweetie2"
}

# Prepare the updated base structure for apps.json
apps_json_structure = {
    "name": "Raghav Repository",  # Updated repository name
    "identifier": "com.google.ios.youtube",  # Identifier for the repository
    "apiVersion": "v2",
    "subtitle": "A collection of apps for iOS.",  # Updated subtitle
    "description": "This source is an automatically kept up-to-date source, powered by GitHub Actions, the Python altparse library, and the support of independent developers. In here, you'll find anything from community maintained forks of Delta Emulator to tiny Mac utilities that no one's ever heard of. If you have an app you'd like to see here, please use our website to reach out!",
    "iconURL": "https://example.com/icon.png",  # Placeholder for icon image
    "headerURL": "https://example.com/header.png",  # Placeholder for header image
    "website": "https://example.com",  # Updated website link
    "tintColor": "#5CA399",  # Color for tinting
    "featuredApps": [
        "com.google.ios.youtube",
        "com.atebits.Tweetie2"
    ],
    "apps": [],  # This will be populated dynamically
    "userinfo": {},  # Placeholder for user info
    "news": []  # Placeholder for news updates
}

# Function to get releases from a repository
def get_releases(repo):
    url = f"https://api.github.com/repos/{repo}/releases"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching releases for {repo}: {e}")
        return []

# Fetch releases and build the apps section
for repo, bundle_id in repositories.items():
    releases = get_releases(repo)
    
    # Create an app entry for each repository
    app_data = {
        "name": repo.split('/')[-1],  # Use the repo name as the app name
        "bundleIdentifier": bundle_id,  # Set the bundle identifier from the dictionary
        "developerName": repo.split('/')[0],  # Get the developer name from the repo
        "localizedDescription": f"Latest updates for {repo.split('/')[-1]}.",  # Descriptive text for the app
        "iconURL": "https://example.com/default_icon.png",  # Generic icon URL
        "tintColor": "#5CA399",  # This can also be customized
        "screenshotURLs": [
            "https://example.com/screenshot1.png",
            "https://example.com/screenshot2.png",
        ],  # Placeholder for screenshots
        "versions": [],  # List to hold version details
        "subtitle": "Latest release information",  # Subtitle for the app
    }

    # Add version details for each release
    for release in releases:
        for asset in release.get("assets", []):
            version_data = {
                "version": asset["name"].split('_')[1],  # Extract version from asset name
                "date": release["published_at"],  # Release date
                "localizedDescription": release["body"],  # Description from release notes
                "minOSVersion": "14.0",  # Minimum OS version required
                "downloadURL": asset["browser_download_url"],  # Download link for the asset
                "size": asset["size"],  # Size of the asset
            }
            app_data["versions"].append(version_data)  # Append version data to app_data

    # Append the app data to the apps list
    apps_json_structure["apps"].append(app_data)

# Write the updated structure to apps.json
with open('apps.json', 'w') as f:
    json.dump(apps_json_structure, f, indent=4)

print("apps.json updated successfully!")
