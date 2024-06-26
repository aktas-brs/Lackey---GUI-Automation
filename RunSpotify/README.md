## Introduction ##
This is a simple code for running an app and making some gui operations on the app. In this example i run spotify and search for an album then i play a chosen song from that album. Inside the Image folder i have the necessary images of the regions of spotify that the program interacts (click,type). I will explain the code step by step.

## Find the full path the spotify ##
To do this:
 - Open a command prompt by pressing `windows + R`.
 - Type `where spotify` and press enter.

you will get the full path to spotify.	

The full path to spotify on my computer looks like this:
![cmd](https://user-images.githubusercontent.com/122377157/225025802-cb94ae5c-afcc-4aed-ae66-20e0f2e25605.png)

## Define the app and run it: ##

1) Define the full path on python as:

`spotify_path = "C:/Users/Baris/AppData/Local/Microsoft/WindowsApps/Spotify.exe"`

You shoul either use one forwardslash `/` or double backslash `\\` when giving a path as a string. If you directly copied the path from cmd window there will be one backslash `\` between folder names so you have to modify it.

2) Define the lackey app object as:

`spotify_app = lackey.App(spotify_path)`

3) Now run the defined app:

`spotify_app.open()`

## Find the song you want to play ##

This will be done in some steps:
 - Click search button
 - Click the search bar
 - Write the song's name
 - Click the play button for that song

1) Click search button

Firs you need to take a screenshot of the button and save it to a folder like this:

![search](https://github.com/aktas-brs/Lackey---GUI-Automation/assets/122377157/ef9ce0cf-c501-4268-bda1-8e3928c3d8e5)

Use `lackey.wait('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search.png',40)` to find the location of the search button on screen.
Then use `lackey.click('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search.png')` to click the position of the button.

2) Click the search bar
Similarly, taking a screenshot and using the same code lines find and click the search bar like this:

![search_bar](https://github.com/aktas-brs/Lackey---GUI-Automation/assets/122377157/09ecf51c-c8ba-4ab5-9746-c4d2c85e8dc1)

`lackey.wait('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search_bar.png',40)
lackey.click('C:/Users/Baris/Desktop/RunSpotify/Screenshots/search_bar.png')`


