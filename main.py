from ytmusicapi import YTMusic
import json


def addToJson(playlist):
  file =  open("songs.json", "w")
  file.writelines(playlist)
  file.close()

def addCharts(charts, playlist):
  #yt = yt.add_playlist_items(playlist, )
  pass

def getVideoIdFromChart(charts, list):
  songs = charts["songs"]
  items = songs["items"]
  for item in items:
    id = item['videoId']
    list.append(id)

def addToPlaylist(yt, playlist, list, charts):
  songs = charts["songs"]
  items = songs["items"]
  current_playlist = yt.get_playlist(playlist['id'])
  current_songs = [track['videoId'] for track in current_playlist['tracks']]

  # create a list of songs not already in the playlist
  new_songs = []
  for song in list:
      if song not in current_songs:
          new_songs.append(song)
      else:
          for item in items:
            name = item['videoId']
            print(f"The song  '{item['title']}' is already in the playlist.")

  # add the new songs to the playlist
  if new_songs:
    yt.add_playlist_items(playlist['id'], new_songs)
  else:
     print("No new songs to add to the playlist")




#Auth
yt = YTMusic('oauth.json')
videoidlist = []

playlist = yt.get_playlist("PLybE7jDXksXKKU98sEnz-MbEXo6FWLzWV")
charts = yt.get_charts("ZZ")




tracks = playlist['tracks']
jsontracks = json.dumps(tracks, indent=4)

addToJson(jsontracks)
getVideoIdFromChart(charts, videoidlist)
addToPlaylist(yt, playlist, videoidlist, charts)

