class Player:
    def __init__(self, name):
        self.name = name 
        self.matches_played = 0
        self.runs = 0
        self.wickets = 0
    def update_performance(self , runs_scored , wickets_taken):
            self.matches_played  += 1
            self.runs += runs_scored
            self.wickets += wickets_taken
    def showstats(self):
        print(f"Name : { self.name} | Matches Played: {self.matches_played} | Runs: {self.runs} | Wickets: {self.wickets} ")
class Team:
    def __init__(self , name):
        self.name = name
        self.player_list = []
    def addplayer(self, player_object):
        self.player_list.append(player_object)
    def show_team_roaster(self):
        print(f"=== Team Roster: {self.name} === ")
        for i in self.player_list:
            i.showstats()
p1 = Player("Baber Azam")
p2 = Player("Aashan Raja")
p3 = Player("Arafat Minhas")
p1.update_performance(12, 2)
p2.update_performance(2300 , 22)
team1 = Team("Peshawer Zalmi")
team2 = Team("Islamabad United")
team1.addplayer(p1)
team2.addplayer(p2)
team2.addplayer(p3)
team1.show_team_roaster()
print("=============================================================================")
team2.show_team_roaster()
    
        