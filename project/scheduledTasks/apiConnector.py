import requests
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def _fetch_api():
    url = 'https://cloud.nousdigital.net/s/rNPWPNWKwK7kZcS/download'
    api_response = requests.get('{0}'.format(url))

    try:
        api_response.raise_for_status()
        return api_response.json()
    except:
        logger.error('No connection to Api')
        return None


def update_items_table():
    json_response = _fetch_api()
    if json_response is not None:
        # can't import Item model before all apps are loaded , thats why the late import
        from api_fetcher.models import Item
        items_list = json_response["items"]
        if items_list is not None and len(items_list) > 0:
            current_item = None
            for item in items_list:
                # create a query object for each item but don't hit database
                current_item = Item(public_id=item["id"], title=item["title"], description=item["description"]\
                                    ,image_url=item["imageUrl"])
                try:
                    current_item.save()
                except:
                    logger.error('Item not saved')
                    pass
