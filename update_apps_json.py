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
                {"name": "com.apple.developer.networking.wifi-info"},
                {"name": "com.apple.security.application-groups"},
                {"name": "keychain-access-groups"}
            ],
            "privacy": [
                {
                    "name": "Purchases",
                    "usageDescription": "Data related to purchases may be collected."
                },
                {
                    "name": "Financial Info",
                    "usageDescription": "Financial data may be collected for analytics."
                },
                {
                    "name": "Location",
                    "usageDescription": "Location data may be collected for personalization."
                },
                {
                    "name": "Contact Info",
                    "usageDescription": "Contact information may be collected and linked."
                },
                {
                    "name": "Contacts",
                    "usageDescription": "Contacts may be accessed for improved recommendations."
                },
                {
                    "name": "User Content",
                    "usageDescription": "User-generated content may be used for service improvement."
                },
                {
                    "name": "Search History",
                    "usageDescription": "Search history may be linked to your identity."
                },
                {
                    "name": "Browsing History",
                    "usageDescription": "Browsing history may be linked to your identity."
                },
                {
                    "name": "Identifiers",
                    "usageDescription": "Identifiers may be used to track users across apps."
                },
                {
                    "name": "Usage Data",
                    "usageDescription": "Usage data helps YouTube improve its services."
                },
                {
                    "name": "Diagnostics",
                    "usageDescription": "Diagnostics data may be collected."
                },
                {
                    "name": "Other Data",
                    "usageDescription": "Other data may be collected but not linked."
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
                {"name": "com.apple.developer.networking.wifi-info"},
                {"name": "com.apple.security.application-groups"},
                {"name": "keychain-access-groups"}
            ],
            "privacy": [
                {
                    "name": "Purchases",
                    "usageDescription": "Data related to purchases may be collected."
                },
                {
                    "name": "Location",
                    "usageDescription": "Location data may be linked to your identity."
                },
                {
                    "name": "Contact Info",
                    "usageDescription": "Contact information may be collected and linked."
                },
                {
                    "name": "Contacts",
                    "usageDescription": "Contacts may be accessed for improved recommendations."
                },
                {
                    "name": "User Content",
                    "usageDescription": "User-generated content may be used for service improvement."
                },
                {
                    "name": "Search History",
                    "usageDescription": "Search history may be linked to your identity."
                },
                {
                    "name": "Browsing History",
                    "usageDescription": "Browsing history may be linked to your identity."
                },
                {
                    "name": "Identifiers",
                    "usageDescription": "Identifiers may be used to track users across apps."
                },
                {
                    "name": "Usage Data",
                    "usageDescription": "Usage data helps Twitter improve its services."
                },
                {
                    "name": "Diagnostics",
                    "usageDescription": "Diagnostics data may be collected."
                },
                {
                    "name": "Other Data",
                    "usageDescription": "Other data may be collected but not linked."
                }
            ]
        }

    # Add version details for each release
    for release in releases:
        if not release.get("assets"):  # Skip if there are no assets
            continue

        version_data = {
            "version": release["tag_name"].lstrip("v").split('-')[0],  # Remove 'v' and extract version
            "date": release["published_at"],  # Release date
            "localizedDescription": release["body"] if release["body"] else "",  # Set to empty if body is null
            "downloadURL": release["assets"][0]["browser_download_url"]  # Use the first asset's download URL
        }
        app_data["versions"].append(version_data)

    return app_data

# Main function to populate apps.json structure
def populate_apps_json():
    for repo in repositories:
        releases = get_releases(repo)  # Fetch releases for the repository
        app_data = create_app_data(repo, releases)  # Create app data from the releases
        apps_json_structure["apps"].append(app_data)  # Append app data to the main structure

    return apps_json_structure

# Generate apps.json
apps_json = populate_apps_json()

# Write to apps.json file
with open("apps.json", "w") as f:
    json.dump(apps_json, f, indent=4)

print("apps.json has been generated successfully.")
