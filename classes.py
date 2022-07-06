class Person:
    def __init__(self, name, age, nationality, games, likes, song):
        self.name = name
        self.age = age
        self.nationailty = nationality
        self.games = games
        self.likes = likes
        self.song = song
    def Bio(self):
        return {"Name":self.name, "Age":self.age, "Nationality":self.nationailty, "Games":self.games, "Likes":self.likes, "Favourite Song":self.song}
Nomzz1 = Person("Nomzz1", "16", "Bri'ish", ["Valorant", "Minecraft", "Overwatch"], "Programming", "Unforgettable")
print(Nomzz1.Bio())