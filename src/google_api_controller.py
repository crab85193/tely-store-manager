import os
import requests
import googlemaps
import geocoder

class GoogleAPIController():
    def __init__(self):
        self.__gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_API_KEY"))
    
    def download_place_photo(self, photo_reference, file_name=None):
        base_url = "https://maps.googleapis.com/maps/api/place/photo"
        max_width = 400

        params = {
            "maxwidth": max_width,
            "photoreference": photo_reference,
            "key": os.environ.get("GOOGLE_API_KEY")
        }

        response = requests.get(base_url, params=params, stream=True)

        if response.status_code == 200:
            if file_name:
                f_name = os.environ.get("SAVE_IMG_DIR") + "/" + file_name + ".jpg"
            else:
                f_name = os.environ.get("SAVE_IMG_DIR") + "/" + photo_reference + ".jpg"

            with open(f_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=128):
                    file.write(chunk)
        else:
            print("Error: Unable to download the image.")
            
    def get_store_photo_url(self, photo_reference, place_id):
        self.download_place_photo(photo_reference, place_id)
        return f"{os.environ.get('IMAGE_SERVER_PROTOCOL')}://{os.environ.get('IMAGE_SERVER_ADDRESS')}/static/{place_id}.jpg"
        
    def search_store(self, keyword):
        location = geocoder.ip('me').latlng
        search_response = self.__gmaps.places_nearby(location=location, keyword=keyword, radius=50000, language="ja")
        stores_info = []
        
        for place in search_response['results']:
            store_info = {}
            try:
                store_info["place_id"] = place["place_id"]
                store_info["name"] = place["name"]
            except Exception as e:
                print(e)
                continue
            try:
                store_info["type"] = place["types"]
            except Exception as e:
                store_info["type"] = []
            try:
                store_info["open"] = place["opening_hours"]["open_now"]
            except Exception as e:
                store_info["open"] = None
            try:
                store_info["photos"] = self.get_store_photo_url(place["photos"][0]["photo_reference"], place["place_id"])
            except Exception as e:
                print(e)
                store_info["photos"] = ""
            try:
                store_info["rating"] = place["rating"]
            except Exception as e:
                store_info["rating"] = None
            try:
                store_info["price_level"] = place["price_level"]
            except Exception as e:
                store_info["price_level"] = None
                
            stores_info.append(store_info)

        return stores_info
    