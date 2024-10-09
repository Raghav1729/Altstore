import requests
import json

# Define the repositories with their corresponding bundle identifiers
repositories = {
    "Raghav1729/BHTwitter": "com.google.ios.youtube",
    "Raghav1729/uYouPlus": "com.atebits.Tweetie2"
}

# Prepare the updated base structure for apps.json
apps_json_structure = {
    "name": "Raghav Repository",
    "identifier": "com.google.ios.youtube",
    "apiVersion": "v2",
    "subtitle": "A collection of apps for iOS.",
    "description": (
        "This repository contains a curated selection of iOS applications, "
        "including social media clients and utility apps, kept up-to-date through "
        "GitHub Actions and contributions from independent developers."
    ),
    "iconURL": "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png",
    "website": "https://github.com/Raghav1729",
    "tintColor": "#5CA399",
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
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for {repo}: {http_err}")
    except requests.exceptions.ConnectionError:
        print(f"Connection error occurred for {repo}.")
    except requests.exceptions.Timeout:
        print(f"Timeout error occurred for {repo}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching releases for {repo}: {e}")
    return []  # Return an empty list on error

# Function to create app data from repository and releases
def create_app_data(repo, bundle_id, releases):
    app_data = {
        "name": repo.split('/')[-1],  # Use the repo name as the app name
        "bundleIdentifier": bundle_id,  # Set the bundle identifier from the dictionary
        "developerName": repo.split('/')[0],  # Get the developer name from the repo
        "localizedDescription": f"Latest updates for {repo.split('/')[-1]}.",  # Descriptive text for the app
        "tintColor": "#5CA399",  # This can also be customized
        "screenshotURLs": [],  # Placeholder for screenshots
        "versions": [],  # List to hold version details
        "subtitle": "Latest release information",  # Subtitle for the app
    }

    # Assign icon URL and screenshot URLs based on the repository
    if repo == "Raghav1729/uYouPlus":
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/uYou.png"
        app_data["screenshotURLs"] = [
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus1.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus2.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus3.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus4.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus5.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus6.jpeg"
        ]
    elif repo == "Raghav1729/BHTwitter":
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/BHTwitter.jpg"
        app_data["screenshotURLs"] = [
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter1.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter2.png", 
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter3.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter4.png"
        ]

    # Add version details for each release
    for release in releases:
        if not release.get("assets"):  # Skip if there are no assets
            continue

        version_data = {
            "version": release["tag_name"],  # Use the tag name as the version
            "date": release["published_at"],  # Release date
            "localizedDescription": release["body"] or f"Latest updates for {repo.split('/')[-1]}.",  # Fallback description
            "minOSVersion": "14.0",  # Minimum OS version required
            "downloadURL": release["assets"][0]["browser_download_url"],  # Download link for the first asset
            "size": release["assets"][0]["size"],  # Size of the first asset
        }
        app_data["versions"].append(version_data)  # Append version data to app_data

    return app_data  # Return the created app data

# Fetch releases and build the apps section
for repo, bundle_id in repositories.items():
    releases = get_releases(repo)
    app_data = create_app_data(repo, bundle_id, releases)  # Create app data
    apps_json_structure["apps"].append(app_data)  # Append the app data to the apps list

# Write the updated structure to apps.json
with open('apps.json', 'w') as f:
    json.dump(apps_json_structure, f, indent=4)

print("apps.json updated successfully!")
