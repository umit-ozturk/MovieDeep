from imdbpie import Imdb
import urllib
import json


class YoutubeAPI:
    youtube_key = "AIzaSyCKSsxs6Xzxl5tHEOS9RRU5S_2NRGRXvRs"

    apis = {
        'search.list': 'https://www.googleapis.com/youtube/v3/search',
    }

    def __init__(self):
        self.youtube_key=youtube_key

    def get_api(self, name):
        return self.apis[name]

    def api_get(self, url, params):
        params['key'] = self.youtube_key
        f = urllib.request.urlopen(url + "?" + urllib.parse.urlencode(params))
        data = f.read()
        f.close()
        return data

    def search(self, q, max_results=2):

        params = {
            'q': q,
            'part': 'id, snippet',
            'maxResults': max_results
        }
        return self.search_advanced(params)

    def search_advanced(self, params, page_info=False):

        api_url = self.get_api('search.list')
        if params is None or 'q' not in params:
            raise ValueError('at least the Search query must be supplied')

        api_data = self.api_get(api_url, params)
        if page_info:
            return {
                'results': self.decode_list(api_data),
                'info': self.page_info
            }
        else:
            return self.decode_list(api_data)

    def decode_list(self, api_data):

        res_obj = json.loads(api_data)
        if 'error' in res_obj:
            msg = "Error " + res_obj['error']['code'] + " " + res_obj['error']['message']
            if res_obj['error']['errors'][0]:
                msg = msg + " : " + res_obj['error']['errors'][0]['reason']
            raise Exception(msg)
        else:
            self.page_info = {
                'resultsPerPage': res_obj['pageInfo']['resultsPerPage'],
                'totalResults': res_obj['pageInfo']['totalResults'],
                'kind': res_obj['kind'],
                'etag': res_obj['etag'],
                'prevPageToken': None,
                'nextPageToken': None
            }
            if 'prevPageToken' in res_obj:
                self.page_info['prevPageToken'] = res_obj['prevPageToken']
            if 'nextPageToken' in res_obj:
                self.page_info['nextPageToken'] = res_obj['nextPageToken']

            items_array = res_obj['items']
            if isinstance(items_array, dict) or len(items_array) == 0:
                return False
            else:
                return items_array


def get_client():
    client = Imdb()
    return client


def get_title(imdb_id):
    return get_client().get_title(imdb_id)


def get_ratings(imdb_id):
    return get_client().get_title_ratings(imdb_id)


def get_video(imdb_id):
    return get_client().get_title_videos(imdb_id)
