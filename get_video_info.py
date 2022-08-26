from googleapiclient.discovery import build

def get_video_info(query, maxResults, next):
    search_request = youtube.search().list(
        part='id',
        q=query,
        type='video',
        maxResults=maxResults,
    )
    
    i = 0
    while search_request and i < next:
        search_response = search_request.execute()
        video_ids = [item['id']['videoId'] for item in search_response['items']]

        videos_response = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids)
        ).execute()

        yield videos_response['items']
        # list_nextメソッドで次の検索へ進む
        search_request = youtube.search().list_next(search_request, search_response)
        i += 1

    return search_request

YOUTUBE_API_KEY = 'YOURAPIKEYS'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
