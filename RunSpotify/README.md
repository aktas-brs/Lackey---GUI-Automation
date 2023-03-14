## Introduction ##
This is a simple code for running an app and making some gui operations on the app. In this example i run spotify and search for an album then i play a chosen song from that album.I will explain the code step by step.

## Find the full path the spotify ##
To do this:
* Open a command prompt by pressing `windows + R`.
* Type `where spotify` and press enter.

you will get the full path to spotify.	

The full path to spotify on my computer looks like this:
![image](https://user-images.githubusercontent.com/122377157/225025802-cb94ae5c-afcc-4aed-ae66-20e0f2e25605.png)

## Define the app and run it: ##

Define the full path on python as:
* `spotify_path = "C:/Users/Baris/AppData/Local/Microsoft/WindowsApps/Spotify.exe"`

You shoul either use one forwardslash `/` or double backslash `\\` when giving a path as a string. If you directly copied the path from cmd window there will be one backslash between folder names so you have to modify it.

Define the lackey app object as:
* `spotify_app = lackey.App(spotify_path)`

Now run the defined app:
* `spotify_app.open()`


