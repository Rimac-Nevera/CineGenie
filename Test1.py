movies={ "action":["John Wick series","Mad Max Fury","Fast & Furious series","The Dark Knight","Avengers"],"comedy":["Bruce Almighty","The Mask","Home Alone","Mr. Bean's Holiday","Ted"],"drama":["Tere Ishk Mein","Dhadak 2"],"horror":["The Conjuring","The Nun","Anabelle"]}
salutations=input("Introduce yourself! ")
print("CineGenie : Yo! My name is CineGenie!")
print("CineGenie : How can I help you find some good movies today ?")
print("CineGenie : First let us get to know the genres I can offer. ")
print('''CineGenie : I can offer the following genres :
      "Action"
      "Comedy"
      "Drama"2
      "Horror''')
print("CineGenie : If I don't know the genre, just blame my lazy ahh creator, capisce ?")
q1=input("Make small talk first! Get to know CineGenie better! ")
print("CineGenie : I am doing well, what about you ?")
a1=input("")
if a1=="Good":
    print("Fantastic to hear bro!")
else:
    print("No worries mate,its gonna be fine.")
print("CineGenie : Alright bro, lets get to business. ")
print("CineGenie : What kind of movies do you like ??")
q2=input("Whats your favorite genre ? : ").lower()
print("CineGenie : Great choice bro!")
print("CineGenie : Here's some movies based on the genre you chose:")
for movies in movies[q2]:
    print(movies)
else:
     print("CineGenie : Oops! Looks like I don't have that genre in my database. Sorry about that, bro!")