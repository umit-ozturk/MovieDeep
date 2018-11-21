from imdbpie import Imdb
from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyCKSsxs6Xzxl5tHEOS9RRU5S_2NRGRXvRs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(q, year, max_results=1, order="relevance", token=None, location=None, location_radius=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=q + str(year) + str(" trailer"),
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",  # Part signifies the different types of data you want
        maxResults=max_results,
        location=location,
        locationRadius=location_radius).execute()

    title = []
    videoId = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            title.append(search_result['snippet']['title'])
            videoId.append(search_result['id']['videoId'])

    youtube_dict = {'title': title, 'videoId': videoId}

    return youtube_dict


def get_client():
    client = Imdb()
    return client


def get_year(imdb_id):
    return get_client().get_title(imdb_id)['base']['year']


def get_title(imdb_id):
    return get_client().get_title(imdb_id)['base']['title']


def get_ratings(imdb_id):
    return get_client().get_title_ratings(imdb_id)


def get_video(imdb_id):
    return get_client().get_title_videos(imdb_id)