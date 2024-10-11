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
        "screenshotURLs": [],
        "tintColor": "#5CA399",
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
                    {"name": "com.apple.security.application-groups"},
                    {"name": "com.apple.developer.associated-domains"},
                    {"name": "com.apple.developer.coremedia.allow-alternate-video-decoder-selection"},
                    {"name": "com.apple.developer.usernotifications.time-sensitive"},
                    {"name": "get-task-allow"},
                    {"name": "com.apple.developer.device-information.user-assigned-device-name"},
                    {"name": "com.apple.developer.group-session"},
                    {"name": "keychain-access-groups"},
                    {"name": "com.apple.developer.networking.multicast"},
                    {"name": "aps-environment"},
                    {"name": "com.apple.developer.siri"},
                    {"name": "com.apple.developer.networking.wifi-info"}
                ],
                "privacy": [
                    {"name": "AppleMusic", "usageDescription": "Allows adding audio files to your videos."},
                    {"name": "BluetoothPeripheral", "usageDescription": "Access to Bluetooth is required to scan for nearby Cast devices."},
                    {"name": "Camera", "usageDescription": "Allows you to create videos using the app."},
                    {"name": "Contacts", "usageDescription": "Contacts are sent to YouTube servers to help find friends."},
                    {"name": "LocalNetwork", "usageDescription": "Access to your network enables discovering and connecting to devices."},
                    {"name": "LocationWhenInUse", "usageDescription": "Attach location information to videos and improve recommendations."},
                    {"name": "Microphone", "usageDescription": "Allows including audio in your videos and voice search."},
                    {"name": "PhotoLibrary", "usageDescription": "Upload media you've already created."},
                    {"name": "UserTracking", "usageDescription": "Tracks user activity for personalized content."}
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
                    {"name": "com.apple.developer.devicecheck.appattest-environment"},
                    {"name": "com.apple.security.application-groups"},
                    {"name": "com.apple.developer.associated-domains"},
                    {"name": "com.apple.developer.replace-plugin"},
                    {"name": "com.apple.developer.usernotifications.communication"},
                    {"name": "com.apple.developer.usernotifications.time-sensitive"},
                    {"name": "keychain-access-groups"},
                    {"name": "aps-environment"},
                    {"name": "com.apple.developer.applesignin"},
                    {"name": "com.apple.developer.siri"},
                    {"name": "com.apple.developer.networking.wifi-info"}
                ],
                "privacy": [
                    {"name": "BluetoothAlways", "usageDescription": "Connects to external devices using Bluetooth."},
                    {"name": "Calendars", "usageDescription": "Access calendars for scheduling and event management."},
                    {"name": "Camera", "usageDescription": "Share images using camera access."},
                    {"name": "Contacts", "usageDescription": "Connects you with friends using your contacts."},
                    {"name": "FaceID", "usageDescription": "Required for secure logins."},
                    {"name": "LocalNetwork", "usageDescription": "Discovers and connects to devices on your network."},
                    {"name": "Location", "usageDescription": "Provides personalized experiences using location data."},
                    {"name": "LocationWhenInUse", "usageDescription": "Accesses your location while using the app."},
                    {"name": "Microphone", "usageDescription": "Needed for voice tweets."},
                    {"name": "PhotoLibraryAdd", "usageDescription": "Adds photos to your library."},
                    {"name": "PhotoLibrary", "usageDescription": "Uploads images from your photo library."},
                    {"name": "SpeechRecognition", "usageDescription": "Recognizes speech for enhanced user experience."},
                    {"name": "UserTracking", "usageDescription": "Tracks user activity for personalized content."}
                ]
            }
        })

    # Add the releases to the app data
    for release in releases:
        if release.get("assets"):
            version_info = {
                "version": release["tag_name"].lstrip("v").split('-')[1] if repo == "Raghav1729/BHTwitter" else release["tag_name"].lstrip("v").split('-')[0],
                "date": release["published_at"],
                "localizedDescription": release.get("body", ""),  # Use get to avoid KeyError
                "downloadURL": release["assets"][0]["browser_download_url"],
                "size": release["assets"][0]["size"]
            }
            app_data["versions"].append(version_info)
        else:
            print(f"No assets found for release: {release['tag_name']}")

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
