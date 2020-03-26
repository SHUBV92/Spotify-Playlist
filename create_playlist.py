# Step 1: Log Into Youtube 
# Step 2: Grab Our Liked Videos 
# Step 3: Create A New Playlist 
# Step 4: Search For the song 
# Step 5: Add this song into the new Spotify playlist 
import json 
from secrets import spotify_user_id

class CreatePlaylist:

# Step 1: Log Into Youtube 
    def get_youtube_client(self):
        pass

# Step 2: Grab Our Liked Videos 
    def get_liked_videos(self):
        pass

# Step 3: Create A New Playlist 
    def create_playlist(self):
        request_body= json.dumps({
            "name": "Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })
    
        query  

# Step 4: Search For the song 
def get_spotify_uri(self):
    pass

# Step 5: Add this song into the new Spotify playlist 
def add_song_to_playlist(self):
    pass

