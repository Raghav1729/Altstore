import requests
import json

# Define the repositories
repositories = [
    "Raghav1729/BHTwitter",
    "Raghav1729/uYouPlus"
]

# Prepare the updated base structure for apps.json
apps_json_structure = {
    "name": "Raghav Repository",
    "identifier": "com.google.ios.youtube",  # Retained as the main identifier for the repo
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
        "com.google.ios.youtube",  # Retained for featured apps
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

# Function to create app data from repository and releases
def create_app_data(repo, releases):
    app_data = {
        "developerName": repo.split('/')[0],  # Get the developer name from the repo
        "localizedDescription": f"Latest updates for {repo.split('/')[-1]}.",  # Descriptive text for the app
        "tintColor": "#5CA399",
        "screenshotURLs": [],  # Placeholder for screenshots
        "versions": [],  # List to hold version details
        "subtitle": "Latest release information",  # Subtitle for the app
    }

    # Assign name, bundle ID, icon URL, and screenshots based on the repository
    if repo == "Raghav1729/uYouPlus":
        app_data["name"] = "YouTube"  # Set name for uYouPlus
        app_data["bundleIdentifier"] = "com.google.ios.youtube"  # Set bundle ID for uYouPlus
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/uYou.png"
        
        # Add screenshots for YouTube
        app_data["screenshots"] = [
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus1.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus2.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus3.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus4.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus5.jpeg"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/uYouPlus/uyouplus6.jpeg"}
        ]
        
        # Permissions for YouTube based on App Store information
        app_data["permissions"] = [
            {
                "type": "contact-info",
                "usageDescription": "YouTube accesses contact information to track users across apps."
            },
            {
                "type": "identifiers",
                "usageDescription": "Identifiers are used to track users across apps and websites."
            }
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
                {
                    "name": "AppleMusic",
                    "usageDescription": "This lets you add your own audio files to your videos."
                },
                {
                    "name": "BluetoothPeripheral",
                    "usageDescription": "YouTube needs bluetooth access to scan for nearby Cast devices."
                },
                {
                    "name": "Camera",
                    "usageDescription": "This lets you create videos using the app."
                },
                {
                    "name": "Contacts",
                    "usageDescription": "Your contacts will be sent to YouTube servers to help you find friends to share videos with."
                },
                {
                    "name": "LocalNetwork",
                    "usageDescription": "Access to your network allows YouTube to discover and connect to devices such as your TV."
                },
                {
                    "name": "LocationWhenInUse",
                    "usageDescription": "Makes it easier for you to attach location information to your videos and live streams and allows for features such as improved recommendations and ads."
                },
                {
                    "name": "Microphone",
                    "usageDescription": "This lets you include audio with your videos and search using your voice."
                },
                {
                    "name": "PhotoLibrary",
                    "usageDescription": "This lets you upload media you've already created."
                }
            ]
        }

    elif repo == "Raghav1729/BHTwitter":
        app_data["name"] = "X"  # Set name for BHTwitter
        app_data["bundleIdentifier"] = "com.atebits.Tweetie2"  # Set bundle ID for BHTwitter
        app_data["iconURL"] = "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/icons/BHTwitter.jpg"
        
        # Add screenshots for Twitter
        app_data["screenshots"] = [
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter1.png"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter2.png"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter3.png"},
            {"imageURL": "https://raw.githubusercontent.com/Raghav1729/Altstore/refs/heads/master/assets/screenshots/BHTwitter/twitter4.png"}
        ]
        
        # Permissions for Twitter based on App Store information
        app_data["permissions"] = [
            {
                "type": "purchases",
                "usageDescription": "Twitter collects data related to your purchases for better ad targeting."
            },
            {
                "type": "location",
                "usageDescription": "Twitter uses location data for tailored content and advertisements."
            },
            {
                "type": "contact-info",
                "usageDescription": "Twitter accesses your contact info to help connect you with others."
            },
            {
                "type": "user-content",
                "usageDescription": "User-generated content may be used for service improvement."
            },
            {
                "type": "browsing-history",
                "usageDescription": "Browsing history is used for personalized content."
            },
            {
                "type": "identifiers",
                "usageDescription": "Identifiers are used for tracking across applications."
            },
            {
                "type": "usage-data",
                "usageDescription": "Usage data helps Twitter improve its services."
            }
        ]
        
        app_data["appPermissions"] = {
            "entitlements": [
                {"name": "com.apple.developer.devicecheck.ap-pattest-environment"},
                {"name": "com.apple.developer.associated-domains"},
                {"name": "com.apple.developer.replace-plugin"},
                {"name": "com.apple.developer.usernotifications.communication"},
                {"name": "com.apple.developer.usernotifications.time-sensitive"},
                {"name": "aps-environment"},
                {"name": "com.apple.developer.applesignin"},
                {"name": "com.apple.developer.siri"}
            ],
            "privacy": [
                {
                    "name": "Bluetooth",
                    "usageDescription": "Bluetooth access is required to connect to external devices."
                },
                {
                    "name": "Calendars",
                    "usageDescription": "Twitter needs access to your calendars for event scheduling."
                },
                {
                    "name": "Camera",
                    "usageDescription": "This lets you take photos and videos directly from the app."
                },
                {
                    "name": "Face ID",
                    "usageDescription": "Face ID is used for secure logins."
                },
                {
                    "name": "LocalNetwork",
                    "usageDescription": "Access to your local network is needed for discovering devices."
                },
                {
                    "name": "LocationWhenInUse",
                    "usageDescription": "Location access is necessary to provide tailored experiences."
                },
                {
                    "name": "Microphone",
                    "usageDescription": "Microphone access is required for voice tweets."
                },
                {
                    "name": "PhotoLibraryAdd",
                    "usageDescription": "Access to your photo library is needed for uploading images."
                },
                {
                    "name": "PhotoLibrary",
                    "usageDescription": "Twitter may access your photo library to share photos."
                },
                {
                    "name": "SpeechRecognition",
                    "usageDescription": "Speech recognition is required for voice commands."
                },
                {
                    "name": "UserTracking",
                    "usageDescription": "User tracking helps Twitter provide personalized content."
                }
            ]
        }

    # Add the releases to the app data
    for release in releases:
        version_info = {
            "version": release["tag_name"],
            "notes": release["body"],
            "downloadURL": release["assets"][0]["url"] if release["assets"] else None
        }
        app_data["versions"].append(version_info)

    return app_data

# Loop through the repositories and populate the apps array
for repo in repositories:
    releases = get_releases(repo)
    app_data = create_app_data(repo, releases)
    apps_json_structure["apps"].append(app_data)

# Output the final apps.json structure
print(json.dumps(apps_json_structure, indent=4))
