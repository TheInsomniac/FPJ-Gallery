# coding: utf-8
import flickrapi
import json
import io
import re
import os
from operator import itemgetter

''' Create a file called 'keys.py' in the same directory as 'FLICKR.py'.
    It should contain the following lines:

    api_key = 'YourAPIKey'
    api_secret = 'YourAPISecretKey'
    user_id = 'YourUserID'
'''
# Now we import the api, secret, and user_id from keys.py
from keys import api_key, api_secret, user_id

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='etree')
(token, frob) = flickr.get_token_part_one(perms='write')
if not token: raw_input("Press ENTER after you authorized this program")
flickr.get_token_part_two((token, frob))

def getPhotosets(flickr):
    photoset_list = flickr.photosets_getList(user_id=user_id).find('photosets').findall('photoset')
    photoset_list_array = []
    for photoset in photoset_list:
        photoset_id = photoset.attrib['id']
        photoset_title = photoset.find('title').text
        photoset_list_array.append({
            'id':photoset_id,
            'name':photoset_title})
    return photoset_list_array

def getPhotos(flickr,id):
    photoset_photos = flickr.photosets_getPhotos(photoset_id=id).find('photoset').findall('photo')
    photoset_photos_list = []
    for photo in photoset_photos:
        photo_id = photo.attrib['id']
        secret = photo.attrib['secret']
        farm = photo.attrib['farm']
        server = photo.attrib['server']
        #title = photo.attrib['title']
        title = re.sub('[^A-Za-z0-9]+', ' ', os.path.splitext(photo.attrib['title'])[0].title())
        photo_url = 'http://farm%s.static.flickr.com/%s/%s_%s_b.jpg' % (farm,server,photo_id,secret)
        thumb_url = 'http://farm%s.static.flickr.com/%s/%s_%s_q.jpg' % (farm,server,photo_id,secret)
        photoset_photos_list.append({'title':title, 'thumb':thumb_url, 'large':photo_url})
    return photoset_photos_list

def create_json():
    photosets = getPhotosets(flickr)
    albums = []
    for photoset in photosets:
        photos = getPhotos(flickr,photoset['id'])
        albums.append({"album":photoset['name']})
        output = {photoset['name'] : {'photos': photos}}
        filename = 'albums/' + photoset['name'] + '.json'
        with io.open(filename, 'w', encoding = 'utf-8') as f:
            f.write(unicode(json.dumps(output, ensure_ascii = False)))

    albums = sorted(albums,key=itemgetter('album'), reverse=True)
    with io.open('albums/albums.json', 'w', encoding = 'utf-8') as f:
        f.write(unicode(json.dumps(albums, ensure_ascii = False)))

if __name__ == "__main__":
    create_json()