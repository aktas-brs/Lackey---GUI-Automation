import lackey 

#Provide the spotify path and open it us,ng lackey
spotify_path = "C:/Users/Baris/AppData/Local/Microsoft/WindowsApps/Spotify.exe"
spotify_app = lackey.App(spotify_path)
spotify_app.open()

#Making sure the spotify window is on top cy clicking its logo
lackey.wait('Image/spotify_logo.jpg',40)
lackey.click('Image/spotify_logo.jpg')

#Finding and clicking the search button in spotify
lackey.wait('Image/search.jpg',40)
lackey.click('Image/search.jpg')

#Finding and clicking on the searchbox
lackey.wait('Image/search_box.jpg',40)
lackey.click('Image/search_box.jpg')

#Typing the name of the album that contains the song i will play
lackey.type('Cem Karaca Olumsuzler')
#Finding and clicking on the album from search results
lackey.wait('Image/olumsuzler.jpg',40)
lackey.click('Image/olumsuzler.jpg')

#Finding and double clicking on the song 
lackey.wait('Image/namus_belasi.jpg',40)
lackey.doubleClick('Image/namus_belasi.jpg')

