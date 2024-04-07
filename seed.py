from models import Song, Playlist, PlaylistSong, db 
from app import app


with app.app_context():
    db.drop_all()
    db.create_all()
song1 = Song(title="Summer Softt", artist="Stevie Wonder")

song2 = Song(title="Isn't She Lovely", artist="Stevie Wonder")

song3 =Song(title="Ain't That a Shame", artist = "Fats Domino")

song4 = Song(title="Blueberry Hill", artist = "Fats Domino")

song5 = Song(title="Purple Rain", artist = "Prince")

song6 = Song(title="Little Red Corvette", artist = "Prince")

song7 = Song(title="Diamonds and Pearls", artist= "Prince")

song8 = Song(title="My Girl", artist="The Temptations")

song9 = Song(title="Mona Lisa", artist="Nat King Cole")

song10= Song(title="Crazy", artist="Gnarls Barkley")

song11= Song(title="LoveSong", artist="The Cure")

playlist1 = Playlist(name= "Stevie Hits", description="a collection of the best songs from Stevie Wonder")
playlist2 = Playlist(name= "Prince Hits", description="a collection of the best songs the artist formerly known as, Prince")
playlist3 = Playlist(name= "Classic Hits", description="all of your favorites from the 1950s")


with app.app_context():
    db.session.add_all([song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, playlist1, playlist2, playlist3])
    db.session.commit()