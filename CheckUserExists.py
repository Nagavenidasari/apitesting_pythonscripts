
import requests

def check_user_exists(api_url, username):
    full_url = f"{api_url}?username={username}"

    response = requests.get(full_url)
    
    if response.status_code == 200:
        data = response.json()
        for user_data in data:
            if user_data.get('username') == username:
                return True

        return False
    else:
        print(f"Failed to query API. Status Code:{response.status_code}")
        return False

api_url = "https://jsonplaceholder.typicode.com/users"
username_to_check = "Bret"

user_exists = check_user_exists(api_url,username_to_check)

if user_exists:
    print(f"The user '{username_to_check}' exists in the system")
else:
    print(f"The user '{username_to_check}' does not exists in the system")
    
