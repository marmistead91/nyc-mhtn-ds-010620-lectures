# finds album in top 500 rolling stone
def find_album(x): 
    for project in top_500_rolling_stone:
        if x == project['album']:
            return x
        else:
            return None
        
       
    
#       finds the album from inputed rank of top 500 rolling stone
def find_rank(x):
    for rank in top_500_rolling_stone:
        if int(x) == int(rank['number']):
            return rank['album']
        
        
        
#     gives albums from year on top 500 rolling stone    
def find_by_year(x):
    albums_released = []
    for y in top_500_rolling_stone:
        if int(x) == int(y['year']):
            albums_released.append(y['album'])
    return albums_released


# gives albums released in the range of years on top 500
def year_rang(x,y):
    albums_released_range = []
    for ys in top_500_rolling_stone:
        if int(x) <= int(ys['year']) <= int(y):
            albums_released_range.append(ys['album'])
    return albums_released_range


# gives albums ranked within range 
def find_by_ranks(x,y):
    albums_released_range = []
    for ys in top_500_rolling_stone:
        if int(x) <= int(ys['number']) <= int(y):
            albums_released_range.append(ys['album'])
    return albums_released_range

# prints all titles
def all_titles():
    all_albums = []
    for project in top_500_rolling_stone:
        all_albums.append(project['album'])
    return all_albums

# prints all artists in top 500
def all_artists():
    all_artists = []
    for project in top_500_rolling_stone:
        all_artists.append(project['artist'])
    return all_artists


# gives you the most occuring artists in top 500
from collections import Counter

def top_500_artist():
    top_count = []
    cnt = Counter(all_artists())
    list_val = list(cnt.values())
    list_keys = list(cnt.keys())
    
    for inx, val in enumerate(cnt.values()):
        if val == max(cnt.values()):
            top_count.append(list_keys[inx])
    return top_count

# shows the most common word in album title
def most_common_word_album():
    word_count = []
    all_words = ' '.join(all_titles())
    lower_words = all_words.lower()
    x = lower_words.split()
    cnt = Counter(x)
    list_val = list(cnt.values())
    list_keys = list(cnt.keys())
    
    for inx, val in enumerate(cnt.values()):
        if val == max(cnt.values()):
            word_count.append(list_keys[inx])
    return word_count