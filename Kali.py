import requests

def get_account_info(api_key):
    url = "https://api.example.com/account"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
api_key = "your_api_key_here"
account_data = get_account_info(api_key)
print(account_data)
