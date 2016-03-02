"""
Tonifai by Alexander Terela

This program allows you to input an image URL. The Clarifai API will recognize the top 5 #tags 
from the image and query Soundcloud to find the top 5 tracks that match these image #tags. Users 
can also change these numbers to find more tracks, or more specific images that match a set of 
tags. My aim is for users to find music that would go hand in hand with an image or set of 
images. 

Users need to input their Soundcloud username and password in order to authorize to 
utilize the Soundcloud API. 

My next plan for the project is to allow the user to input a 
Soundcloud track or set of tags for a track which will query an image service utilizing the 
Clarifai API to find the best image to use as the cover photo for the track. 

Also this code is pretty janky, but it works. 
"""

import soundcloud
from clarifai.client import ClarifaiApi

# Soundcloud
clientID = YOUR_CLIENT_ID
clientSecret = YOUR_CLIENT_SECRET

# create client object with app and user credentials
client = soundcloud.Client(client_id=clientID,
                           client_secret=clientSecret,
                           username=YOUR_SOUNDCLOUD_USERNAME,
                           password=YOUR_SOUNDCLOUD_PASSWORD)

# Clarifai
CLARIFAI_APP_ID = YOUR_CLARIFAI_APP_ID
CLARIFAI_APP_SECRET = YOUR_CLARIFAI_APP_SECRET

clarifai_api = ClarifaiApi(app_id=CLARIFAI_APP_ID, app_secret=CLARIFAI_APP_SECRET)

#results = clarifai_api.tag_image_urls('http://d21vu35cjx7sd4.cloudfront.net/dims3/MMAH/thumbnail/645x380/quality/90/?url=http%3A%2F%2Fs3.amazonaws.com%2Fassets.prod.vetstreet.com%2F3a%2F54%2F5ae8bfcc41b381c27a792e0dd891%2FAP-KWDHXS-645sm8113.jpg')

#results = clarifai_api.tag_urls("http://d21vu35cjx7sd4.cloudfront.net/dims3/MMAH/thumbnail/645x380/quality/90/?url=http%3A%2F%2Fs3.amazonaws.com%2Fassets.prod.vetstreet.com%2F3a%2F54%2F5ae8bfcc41b381c27a792e0dd891%2FAP-KWDHXS-645sm8113.jpg")

#results = clarifai_api.tag_urls("http://www.midtownhotelnyc.com/resourcefiles/homeimages/hilton-garden-inn-new-york-manhattan-midtown-east-home1-top.jpg")

userInput = input('Please enter your image URL: ')

results = clarifai_api.tag_urls(userInput)

for result in results.get('results'):
  tag = result['result']['tag']['classes']
  break
  # debug
  #print(tag)
# debug
#print (tag)

taglist = list()

i = 0
for t in tag:
    if (i==5):
        break
    # debug
    #print (t)
    taglist.append(t)
    i += 1

# debug
#print(taglist)

tagslist = ",".join(taglist)

tracks = client.get('/tracks',
                    tags = tagslist,
                    order='created_at', 
                    limit=5, 
                    )

# print the results
print("The top #tag matching tracks from Soundcloud are: ")
for i, v in enumerate(tracks):
    print (i, v.title, v.created_at)

