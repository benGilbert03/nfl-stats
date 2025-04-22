import requests

# Step 1: Get the list of all NFL athletes
base_url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes"
response = requests.get(base_url)
data = response.json()

# Step 2: Loop through the list of player URLs
player_urls = [item['$ref'] for item in data.get('items', [])]

quarterbacks = []

print("Fetching players...")

# Step 3: Fetch details for each player and filter by position
for url in player_urls:
    player_data = requests.get(url).json()
    
    # Safely access nested data
    position = player_data.get("position", {}).get("abbreviation", "")
    
    if position == "QB":
        quarterbacks.append({
            "name": player_data.get("displayName"),
            "team": player_data.get("team", {}).get("displayName", "Unknown"),
            "position": position
        })

# Step 4: Print the list of QBs
print(f"Found {len(quarterbacks)} quarterbacks:\n")
for qb in quarterbacks:
    print(f"{qb['name']} - {qb['team']} ({qb['position']})")
