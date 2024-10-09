import requests
import json

repositories = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

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
    "apps": [],
    "userinfo": {},
    "news": []
}

def get_releases(repo):
    url = f"https://api.github.com/repos/{repo}/releases"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching releases for {repo}: {e}")
        return []

def create_app_data(repo, releases):
    app_data = {
        "developerName": repo.split('/')[0],
        "localizedDescription": f"Latest updates for {repo.split('/')[-1]}.",
        "tintColor": "#5CA399",
        "screenshotURLs": [],
        "versions": [],
        "subtitle": "Latest release information",
    }

    if repo == "Raghav1729/uYouPlus":
        app_data["name"] = "YouTube"
        app_data["bundleIdentifier"] = "com.google.ios.youtube"
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/uYou.png"
        app_data["screenshotURLs"] = [
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus1.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus2.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus3.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus4.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus5.jpeg",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus6.jpeg"
        ]
        app_data["screenshots"] = [
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus1.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus2.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus3.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus4.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus5.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus6.jpeg"}
        ]
        app_data["permissions"] = [
            {"type": "photos", "usageDescription": "Allows YouTube to upload media from your photo library."},
            {"type": "background-audio", "usageDescription": "Allows YouTube to play audio in the background."}
        ]
        app_data["appPermissions"] = {
            "entitlements": [
                {"name": "get-task-allow"},
                {"name": "aps-environment"},
                {"name": "com.apple.developer.associated-domains"},
                {"name": "com.apple.developer.coremedia.allow-alternate-video-decoder-selection"},
                {"name": "com.apple.developer.device-information.user-assigned-device-name"},
                {"name": "com.apple.developer.networking.multicast"},
                {"name": "com.apple.developer.networking.wifi-info"},
                {"name": "com.apple.developer.usernotifications.time-sensitive"},
                {"name": "com.apple.security.application-groups"},
                {"name": "keychain-access-groups"}
            ],
            "privacy": [
                {"name": "AppleMusic", "usageDescription": "This lets you add your own audio files to your videos."},
                {"name": "BluetoothPeripheral", "usageDescription": "YouTube needs bluetooth access to scan for nearby Cast devices."},
                {"name": "Camera", "usageDescription": "This lets you create videos using the app."},
                {"name": "Contacts", "usageDescription": "Your contacts will be sent to YouTube servers to help you find friends to share videos with."},
                {"name": "LocalNetwork", "usageDescription": "Access to your network allows YouTube to discover and connect to devices such as your TV."},
                {"name": "LocationWhenInUse", "usageDescription": "Makes it easier for you to attach location information to your videos and live streams and allows for features such as improved recommendations and ads."},
                {"name": "Microphone", "usageDescription": "This lets you include audio with your videos and search using your voice."},
                {"name": "PhotoLibrary", "usageDescription": "This lets you upload media you've already created."}
            ]
        }

    elif repo == "Raghav1729/BHTwitter":
        app_data["name"] = "X"
        app_data["bundleIdentifier"] = "com.atebits.Tweetie2"
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/BHTwitter.jpg"
        app_data["screenshotURLs"] = [
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter1.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter2.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter3.png",
            "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter4.png"
        ]
        app_data["screenshots"] = [
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter1.png"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter2.png"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter3.png"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter4.png"}
        ]
        app_data["permissions"] = [
            {"type": "photos", "usageDescription": "Allows X to access media from your photo library."}
        ]
        app_data["appPermissions"] = {
            "entitlements": [
                {"name": "get-task-allow"},
                {"name": "aps-environment"}
            ],
            "privacy": [
                {"name": "LocationWhenInUse", "usageDescription": "Allows X to attach location to tweets."}
            ]
        }

    for release in releases:
        if not release.get("assets"):
            continue

        version_data = {
            "version": (
                release["tag_name"].lstrip("v").split('-')[1] if repo == "Raghav1729/BHTwitter" 
                else release["tag_name"].lstrip("v").split('-')[0]
            ),
            "date": release["published_at"],
            "localizedDescription": release["body"] or f"Latest updates for {repo.split('/')[-1]}.",
            "minOSVersion": "14.0",
            "downloadURL": release["assets"][0]["browser_download_url"],
            "size": release["assets"][0]["size"],
        }
        app_data["versions"].append(version_data)

    return app_data

# Fetch releases and build the apps section
for repo in repositories:
    releases = get_releases(repo)
    app_data = create_app_data(repo, releases)
    apps_json_structure["apps"].append(app_data)

# Write the updated structure to apps.json
with open('apps.json', 'w') as f:
    json.dump(apps_json_structure, f, indent=4)

print("apps.json updated successfully!")
