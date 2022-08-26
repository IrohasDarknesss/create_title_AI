import codecs
from get_video_info import get_video_info

query = 'スマブラ'
dict = get_video_info(
    query,
    50,
    100
)

save_csv = './csv/youtube_title.csv'
with codecs.open(save_csv, "w", encoding='cp932', errors='replace') as f:
    for i, items_per_page in enumerate(dict):
        if i == 0:
            column_list = ['id', 'url',
                           'publishedAt','channelTitle', 'channelId', 'title',
                           'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount', 'commentCount']
            column_list_str = ','.join(column_list)
            f.write(column_list_str + '\n')
        for item in items_per_page:
            dic_list = []
            dic_list.append(item['id'])
            dic_list.append('http://youtube.com/watch?v=' + item['id'])
            # snippet オブジェクトには、タイトル、説明、カテゴリなどが格納されている。
            snippet = item['snippet']
            for key in ['publishedAt', 'channelTitle','channelId','title']:
                dic_list.append(snippet[key].replace(',', '_'))
            # statistics オブジェクトには、動画に関する統計情報が格納されている。
            statistics = item['statistics']
            for key in ['viewCount','likeCount','dislikeCount','favoriteCount','commentCount']:
                dic_list.append(statistics[key] if key in statistics else "NA")               
            f.write(','.join(list(map(str, dic_list))) + '\n')
