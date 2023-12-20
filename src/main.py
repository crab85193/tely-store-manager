import os
import shutil
import sentry_sdk
from store_manager import StoreManager
from google_api_controller import GoogleAPIController

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DNS"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

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