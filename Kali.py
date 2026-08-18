import requests

# ============================================
# ONLY CHANGE THIS LINE — paste your access token below
# ============================================
ACCESS_TOKEN = "EAAaRuA6zqbgBSWm6YxNM4CdyqHZCuxgNoNfBX2aGeLlpOnZAezeY5680JgvEDePRjUew7b3hZC7b3hZCWMRfjebo8xkffrdj1kCpwgp3BX6HrnZAYMpZCHjKlGcoJJSyUZC0XWKZCppzZBgMhBZBPA9mfWd3uwCG8zDaZBWqTI9tlZAJow5KAdfuPmOeYPx7AZDZD"
# ============================================


def get_instagram_details(access_token):
    url = "https://graph.instagram.com/me"
    params = {
        "fields": "username,biography,followers_count,follows_count,media_count,profile_picture_url,website,account_type",
        "access_token": access_token
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)
        return None


def main():
    if ACCESS_TOKEN == "your_access_token_here":
        print("Please set your ACCESS_TOKEN at the top of this file before running.")
        return

    data = get_instagram_details(ACCESS_TOKEN)
    if data:
        print(f"Username: {data.get('username')}")
        print(f"Account Type: {data.get('account_type')}")
        print(f"Biography: {data.get('biography')}")
        print(f"Website: {data.get('website')}")
        print(f"Followers: {data.get('followers_count')}")
        print(f"Following: {data.get('follows_count')}")
        print(f"Media Count: {data.get('media_count')}")
        print(f"Profile Picture URL: {data.get('profile_picture_url')}")


if __name__ == "__main__":
    main()
