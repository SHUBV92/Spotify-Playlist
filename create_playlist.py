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
    
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.id)
        response = request.post(
            query, 
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id 
        return response_json("id")


# Step 4: Search For the song 
def get_spotify_uri(self, track, artist):
    query   = "https://api.spotify.com/v1/search?query=track%3A{}+"
    song_name, 
    artisit
)
    response = request.get(
        query, 
        header={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )

# Step 5: Add this song into the new Spotify playlist 
def add_song_to_playlist(self):
    pass   

