class Player:
    def __init__(self, name, nationality, team, assists, goals):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.assists = assists
        self.goals = goals
    
    def __str__(self):
        return " ".join(
            [f"{self.name:20}",
            self.team, "assists:",
            f"{self.assists:3}", "goals:",
            f"{self.goals:3}",
            "total:", str(self.assists+self.goals)
            ])

# {'name': 'Joey Daccord', 'nationality': 'USA', 'assists': 0, 'goals': 0, 'penalties': 0, 'team': 'SEA', 'games': 5}
