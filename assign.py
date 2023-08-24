class CricketMatch:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

    def __str__(self):
        return f"{self.location} {self.team1} {self.team2} {self.timing}"

class CricketMatchTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        match = CricketMatch(location, team1, team2, timing)
        self.matches.append(match)

    def search_by_team(self, team_name):
        result = []
        for match in self.matches:
            if match.team1 == team_name or match.team2 == team_name:
                result.append(match)
        return result

    def search_by_location(self, location):
        result = []
        for match in self.matches:
            if match.location == location:
                result.append(match)
        return result

    def search_by_timing(self, timing):
        result = []
        for match in self.matches:
            if match.timing == timing:
                result.append(match)
        return result

# User input for search parameter
print("Choose one of the search parameter:")
print("1. List of all the matches of a Team")
print("2. List of Matches on a Location")
print("3. List of Matches based on timing")
choice = int(input())

# Create a cricket match table and add matches to it
table = CricketMatchTable()
table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
table.add_match("Chennai", "India", "South Africa", "DAY")
table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
table.add_match("Delhi", "India", "Australia", "DAY")

if choice == 1:
    team_name = input("Enter the name of the team: ")
    result = table.search_by_team(team_name)
elif choice == 2:
    location = input("Enter the location: ")
    result = table.search_by_location(location)
elif choice == 3:
    timing = input("Enter the timing (DAY or DAY-NIGHT): ")
    result = table.search_by_timing(timing)

# Print the search results
for match in result:
    print(match)
