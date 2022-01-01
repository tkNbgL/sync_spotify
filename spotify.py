import sys
import json
import requests
import base64

class ShopifyPlayList(object):
    # def __init__(self, collaborative, description, external_urls, href, id, images, name, owner, primary_color, public, sharing_info, snapshot_id, tracks, type,
    # uri):
    #     self.description = description
    #     self.collaborative = collaborative
    #     self.external_urls = external_urls
    #     self.href = href
    #     self.id = id
    #     self.images = images
    #     self.name = name
    #     self.owner = owner
    #     self.primary_color = primary_color
    #     self.public = public
    #     self.sharing_info = sharing_info
    #     self.snapshot_id = snapshot_id
    #     self.type = type
    #     self.uri = uri
    #     self.tracks = tracks
    def __init__(self, dict1):
        self.__dict__.update(dict1)

class PlayList(object):
    def __init__(self, id, href, name, owner, public, sharing_info, tracks)

def getPlaylistItems(play_lists):
    items = list()
    for val in play_lists:
        items.append(val['href'])
    return items    

def getPlayLists(play_list_hrefs):
    play_lists = list()
    for href in play_list_hrefs:
        playlistJson = requests.get(href, headers = header).json()
        playlist = json.loads(json.dumps(playlistJson), object_hook=ShopifyPlayList)
        play_lists.append(playlist)
    return play_lists

#get bearer token
authCredential = "2e920c26beff4c14a5c1d29c1689e11f:b4b9ba29fc6c409da174b02dcb9c7fe6"
authCredentialsBase64Bytes = base64.b64encode(authCredential.encode("ascii"))
authStringBase64 = authCredentialsBase64Bytes.decode("ascii")
authData = "Basic " + authStringBase64
authHeaders = {'Authorization' : authData}
payload = {'grant_type': 'client_credentials'}

shopifyAccessToken = requests.post("https://accounts.spotify.com/api/token", headers = authHeaders, data=payload)
print("credentials:" + shopifyAccessToken.text)
print("\n")

#store access tokens for later use
credentials_json = shopifyAccessToken.json()
#taken from web player headers
access_token = 'Bearer ' + "BQAs8cnYvuqyoF0p6yG7nGDTNIc3xayFoJNAbeHwbFGrQvEWeD42CtZ3wbnbZkWmkDhDAwZ8_jCRay5QWDtaxtopHaoRm9LGI6cbRnAOknMket7Wa0mko2nFpP3ywiR9_fPg-oapcBC8R5YiWYXZ-ZSOVWRde4qZPOFp9UyTyZPzXV7ygi4thStPlagvy6kJ4yKxCG7jvMqVqiX-ULDJhekdy8xbHTq9x5FaEaYzuLWclvo9z-zT9etaomxQ458s2oO1sqT_fIPJoReh50axHvjcJ4R3gK1H99rNmbInHjShWTh6zc3hB_BaB-w2"
print("access token: " + access_token)
print("\n")

#get current user's profile
url = "https://api.spotify.com/v1/me"
header = {'Authorization': access_token}
user = requests.get(url, headers = header)
print(user.text)
print("\n")

#get current user's list of playlists
#get href
#make a get request to that href to see what its got
#it hat external_urls.spotify value map that to list of string
#this url indicate to content of the specified playlist
#this lists contains all the songs in a playlist with corresponding track, artists, available market information
#we are going to key values about track to search in a different platform later
#take track.album.artists "name" and "type" some track may contain more than one artists be awere of that
#get id(may be used later to fetch specified track) and get song's name in playlists, it's on the main object

#get current user's playlists
url = "https://api.spotify.com/v1/me/playlists"
play_lists = requests.get(url, headers = header).json()
# print("play_lists:", play_lists)

# get hrefs of playlists
# example_href = play_lists['items'][0]['href'] #this is wrong find a way to accessing first element
# print("ex href: ", example_href)
play_list_hrefs = getPlaylistItems(play_lists['items'])
play_lists = getPlayLists(play_list_hrefs)
for play_list in play_lists:
    print(play_list.name)

# output_file = open('playlist.txt', 'w')

#get list of songs
# songs_of_playlists = requests.get(example_href, headers = header).json()
# o_playlist = json.loads(json.dumps(songs_of_playlists), object_hook=PlayList)
# print("my playlist: ", o_playlist.name)
