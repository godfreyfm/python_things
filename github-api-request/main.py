import requests

# GitHub username you want to fetch the projects for
username = "****"

# API endpoint for fetching user's repositories
response = requests.get(f"https://api.github.com/users/{username}/repos")

if response.status_code == 200:
    my_projects = response.json()

    # Print the whole objects list
    """print(my_projects)
    print(type(my_projects))"""

    # Print just the names and URLs
    for project in my_projects:
        print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")
else:
    print(f"Failed to retrieve repositories: {response.status_code}")
    print(response.json())