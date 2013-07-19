#Static Flickr-Python-JQuery Gallery  

This is just a quick (and likely) dirty implemenation of a Photo Gallery which  
extracts all photosets from a user's feed and stores their data in a local json  
object.  

Each Photoset is stored in it's own json file and there is a master albums.json file  
which stores the list of Photosets(as used in albums in the gallery).  

This was my attempt at creating a VERY lightweight photo gallery where the user didn't  
wish to save the files locally and create thumbnails like my **Flask Gallery** and  
didn't like having to use Flickr's front-end (or, perhaps, let people know that the  
photos are stored there).

Uses OAUTH2 authentication.

*Configuration:*  

Create a file called 'keys.py' in the same directory as 'FLICKR.py'.  
It should contain the following lines:

    api_key = 'YourAPIKey'
    api_secret = 'YourAPISecretKey'
    user_id = 'YourUserID'
    
*Creating JSON files:*  

    python FLICKR.py

If this is the first time run then it will redirect you to Flickr in order to give  
the app permissions and download the appropriate tokens.  

It will then scrape Flickr for all of your photosets and create the appropriate  
files.

*Serving:*  

After the above have been completed then merely serve the directory with your  
favorite webserver. `Index.html` is the main page and `albums.html` is the photo page.  

The JSON files are stored in `./Albums` and are loaded appropriately.  

CSS and JS are served from their respectively named directories.

##Utilizes:  
+ Python
+ JQuery
+ Bootstrap w/ Simplex Theme
+ JQuery Swipebox
+ JQUery Loadimage

![Screenshot](https://raw.github.com/manxam/FPJ-Gallery/master/screenshots/index1.png)
![Screenshot](https://raw.github.com/manxam/FPJ-Gallery/master/screenshots/index2.png)
![Screenshot](https://raw.github.com/manxam/FPJ-Gallery/master/screenshots/gallery.png)