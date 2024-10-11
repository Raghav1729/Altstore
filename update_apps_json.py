import requests
import json

# Define the repositories
REPOSITORIES = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

# Prepare the updated base structure for apps.json
APPS_JSON_STRUCTURE = {
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
    "apps": [],
    "userinfo": {},
    "news": []
}

def get_releases(repo):
    """Fetch releases from a repository."""
    url = f"https://api.github.com/repos/{repo}/releases"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching releases for {repo}: {e}")
        return []

def create_app_data(repo, releases):
    """Create app data structure from repository and releases."""
    app_data = {
        "developerName": repo.split('/')[0],
        "tintColor": "#5CA399",
        "screenshotURLs": [],
        "versions": [],
    }

    if repo == "Raghav1729/uYouPlus":
        app_data.update({
            "name": "YouTube",
            "bundleIdentifier": "com.google.ios.youtube",
            "iconURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/uYou.png",
            "screenshots": [
                {"imageURL": f"https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus{i}.jpeg"}
                for i in range(1, 7)
            ],
            "localizedDescription": "Watch videos, subscribe to channels, and access personalized content with the enhanced YouTube experience.",
            "subtitle": "Watch, create, and share your favorite content.",
            "appPermissions": {
                "entitlements": [
                    {"name": "com.apple.developer.associated-domains"},
                    {"name": "aps-environment"},
                    {"name": "com.apple.developer.usernotifications.communication"},
                    {"name": "com.apple.developer.usernotifications.time-sensitive"},
                    {"name": "com.apple.developer.applesignin"},
                    {"name": "com.apple.security.application-groups"},
                    {"name": "keychain-access-groups"},
                    {"name": "com.apple.developer.networking.wifi-info"}
                ],
                "privacy": [
                    {"name": "Bluetooth", "usageDescription": "Bluetooth access is used for connecting to external devices."},
                    {"name": "Camera", "usageDescription": "Camera access is needed for recording and uploading videos."},
                    {"name": "Microphone", "usageDescription": "Microphone access is required for voiceovers and comments."},
                    {"name": "Location", "usageDescription": "Location data is used to provide personalized content."},
                    {"name": "Photo Library", "usageDescription": "Access to your photo library is required to upload photos and videos."},
                    {"name": "Contacts", "usageDescription": "YouTube accesses your contacts to suggest friends."}
                ]
            }
        })
    
    elif repo == "Raghav1729/BHTwitter":
        app_data.update({
            "name": "X",
            "bundleIdentifier": "com.atebits.Tweetie2",
            "iconURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/BHTwitter.jpg",
            "screenshots": [
                {"imageURL": f"https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter{i}.png"}
                for i in range(1, 5)
            ],
            "localizedDescription": "Stay updated with real-time conversations, news, and trending topics on the X platform.",
            "subtitle": "Real-time social media and microblogging platform.",
            "appPermissions": {
                "entitlements": [
                    {"name": "com.apple.developer.devicecheck.ap-pattest-environment"},
                    {"name": "com.apple.developer.associated-domains"},
                    {"name": "com.apple.developer.replace-plugin"},
                    {"name": "com.apple.developer.usernotifications.communication"},
                    {"name": "com.apple.developer.usernotifications.time-sensitive"},
                    {"name": "aps-environment"},
                    {"name": "com.apple.developer.applesignin"},
                    {"name": "com.apple.security.application-groups"},
                    {"name": "keychain-access-groups"},
                    {"name": "com.apple.developer.networking.wifi-info"}
                ],
                "privacy": [
                    {"name": "Bluetooth", "usageDescription": "Bluetooth access is used for connecting to external devices."},
                    {"name": "Contacts", "usageDescription": "Twitter accesses your contacts to connect you with friends."},
                    {"name": "Face ID", "usageDescription": "Face ID is required for secure logins."},
                    {"name": "Location", "usageDescription": "Location data is used to provide personalized experiences."},
                    {"name": "Microphone", "usageDescription": "Microphone access is needed for voice tweets."},
                    {"name": "Camera", "usageDescription": "Camera access is used for sharing images."}
                ]
            }
        })

    # Add the releases to the app data
    for release in releases:
        version_info = {
            "version": release["tag_name"].lstrip("v").split('-')[1] if repo == "Raghav1729/BHTwitter" else release["tag_name"].lstrip("v").split('-')[0],
            "date": release["published_at"],
            "localizedDescription": release.get("body", ""),  # Use get to avoid KeyError
            "downloadURL": release["assets"][0]["browser_download_url"],
            "size": release["assets"][0]["size"]
        }
        app_data["versions"].append(version_info)

    return app_data

# Populate the apps array
for repo in REPOSITORIES:
    releases = get_releases(repo)
    app_data = create_app_data(repo, releases)
    APPS_JSON_STRUCTURE["apps"].append(app_data)

# Write to apps.json file
with open("apps.json", "w") as f:
    json.dump(APPS_JSON_STRUCTURE, f, indent=4)

print("apps.json has been generated successfully.")
