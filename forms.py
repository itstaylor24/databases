"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name", validators=[InputRequired(message="must enter a name for your playlist")])
    description = TextAreaField("Description")



class SongForm(FlaskForm):
    """Form for adding songs."""
    title= TextAreaField("Song Title", validators=[InputRequired(message="must enter a song title")])
    artist = TextAreaField("Song Artist")
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

   
    song = SelectField('Song To Add', coerce=int)