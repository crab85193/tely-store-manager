import os
import shutil
from store_manager import StoreManager
from google_api_controller import GoogleAPIController

def main():
    store_manager = StoreManager()
    api = GoogleAPIController()

    target_dir = './static'

    shutil.rmtree(target_dir)
    os.mkdir(target_dir)

    store_manager.delete_all()

    results = api.search_store("飲食店")

    for result in results:
        store_manager.insert(
            result["place_id"],
            result["name"],
            " ".join(result["type"]),
            result["open"],
            result["photos"],
            result["rating"],
            result["price_level"]
        )


if __name__ == "__main__":
    main()