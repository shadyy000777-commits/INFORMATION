import requests

def get_instagram_details(access_token):
    url = "https://graph.instagram.com/me"
    params = {
        "fields": "username,email,phone_number,linked_accounts,biography,followers_count,follows_count,media_count,profile_picture_url",
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Example usage
access_token = "your_access_token_here"
data = get_instagram_details(access_token)
if data:
    print(f"Username: {data.get('username')}")
    print(f"Email: {data.get('email')}")
    print(f"Phone Number: {data.get('phone_number')}")
    print(f"Biography: {data.get('biography')}")
    print(f"Followers: {data.get('followers_count')}")
    print(f"Media Count: {data.get('media_count')}")
