import requests
import json

# Define the repositories to fetch app releases from
repositories = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

# Prepare the base structure for the apps.json file
apps_json_structure = {
    "name": "Raghav Repository",  # Name of the repository
    "identifier": "com.google.ios.youtube",  # Main identifier for the repo
    "apiVersion": "v2",  # Version of the API
    "subtitle": "A collection of apps for iOS.",  # Subtitle for the repository
    "description": (
        "This repository contains a curated selection of iOS applications, "
        "including social media clients and utility apps, kept up-to-date through "
        "GitHub Actions and contributions from independent developers."
    ),
    "iconURL": "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png",  # Icon URL for the repository
    "website": "https://github.com/Raghav1729",  # Link to the repository
    "tintColor": "#5CA399",  # Tint color for the apps
    "featuredApps": [
        "com.google.ios.youtube",  # Featured app identifier
        "com.atebits.Tweetie2"  # Another featured app identifier
    ],
    "apps": [],  # This will be populated with app data dynamically
    "userinfo": {},  # Placeholder for user information
    "news": []  # Placeholder for news updates
}

# Function to get releases from a specified repository
def get_releases(repo):
    url = f"https://api.github.com/repos/{repo}/releases"  # Construct the GitHub API URL for releases
    try:
        response = requests.get(url)  # Make a request to the GitHub API
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response if successful
    except requests.RequestException as e:
        print(f"Error fetching releases for {repo}: {e}")  # Print any errors encountered
        return []  # Return an empty list in case of an error

# Function to create app data from repository releases
def create_app_data(repo, releases):
    app_data = {
        "developerName": repo.split('/')[0],  # Get the developer name from the repo
        "localizedDescription": f"Latest updates for {repo.split('/')[-1]}.",  # Descriptive text for the app
        "tintColor": "#5CA399",  # Tint color for the app
        "screenshotURLs": [],  # Placeholder for screenshots
        "versions": [],  # List to hold version details
        "subtitle": "Latest release information",  # Subtitle for the app
    }

    # Assign name, bundle ID, icon URL, and screenshot URLs based on the repository
    if repo == "Raghav1729/uYouPlus":
        app_data["name"] = "YouTube"  # Set name for uYouPlus
        app_data["bundleIdentifier"] = "com.google.ios.youtube"  # Set bundle ID for uYouPlus
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/uYou.png"  # Updated icon URL for uYouPlus
        app_data["screenshotURLs"] = [  # Screenshots for uYouPlus
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus1.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus2.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus3.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus4.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus5.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus6.jpeg"
        ]
    elif repo == "Raghav1729/BHTwitter":
        app_data["name"] = "X"  # Set name for BHTwitter
        app_data["bundleIdentifier"] = "com.atebits.Tweetie2"  # Set bundle ID for BHTwitter
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/BHTwitter.jpg"  # Updated icon URL for BHTwitter
        app_data["screenshotURLs"] = [  # Screenshots for BHTwitter
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter1.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter2.png", 
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter3.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter4.png"
        ]

    # Add version details for each release
    for release in releases:
        if not release.get("assets"):  # Skip if there are no assets
            continue

        # Create version data using the release information
        version_data = {
            "version": (
                release["tag_name"].lstrip("v").split('-')[1] if repo == "Raghav1729/BHTwitter" 
                else release["tag_name"].lstrip("v").split('-')[0]
            ),  # Remove 'v' and extract version; use index 1 for BHTwitter and index 0 for uYouPlus
            "date": release["published_at"],  # Release date
            "localizedDescription": release["body"] or f"Latest updates for {repo.split('/')[-1]}.",  # Fallback description if body is empty
            "minOSVersion": "14.0",  # Minimum OS version required
            "downloadURL": release["assets"][0]["browser_download_url"],  # Download link for the first asset
            "size": release["assets"][0]["size"],  # Size of the first asset
        }
        app_data["versions"].append(version_data)  # Append version data to app_data

    return app_data  # Return the created app data

# Fetch releases and build the apps section
for repo in repositories:
    releases = get_releases(repo)  # Get releases for the current repository
    app_data = create_app_data(repo, releases)  # Create app data from the releases
    apps_json_structure["apps"].append(app_data)  # Append the app data to the apps list

# Write the updated structure to apps.json
with open('apps.json', 'w') as f:
    json.dump(apps_json_structure, f, indent=4)  # Save the JSON structure to apps.json

print("apps.json updated successfully!")  # Confirmation message
