import lackey 

#Provide the spotify path and open it using lackey
spotify_path = "C:/Users/Baris/AppData/Local/Microsoft/WindowsApps/Spotify.exe"
spotify_app = lackey.App(spotify_path)
spotify_app.open()

#Finding and clicking the search button in spotify
lackey.wait('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search.png',40)
lackey.click('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search.png')

#Finding and clicking on the searchbox
lackey.wait('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search_bar.png',40)
lackey.click('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search_bar.png')

#Typing the name of the song 
lackey.type('People are strange')

#Finding and clicking on the song to play it
lackey.wait('C:/Users/Baris/Desktop/RunSpotify/Screenshots/song.png',40)
lackey.click('C:/Users/Baris/Desktop/RunSpotify/Screenshots/song.png')
