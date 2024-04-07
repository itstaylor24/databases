"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30), nullable= False)
    description = db.Column(db.Text)
    songs= db.relationship('Song', secondary= 'playlistsongs', backref='playlists')

    def __repr__(self):
        return f"<Playlist {self.id, self.name, self.description}>"

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    artist = db.Column(db.Text)

    def __repr__(self):
        return f"<Song {self.title, self.artist}>"


    # ADD THE NECESSARY CODE HERE








class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlistsongs'
    id = db.Column(db.Integer,  primary_key= True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))

    def __repr__(self):
        return f"<PlaylistSong {self.playlist_id, self.song_id}>"

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
