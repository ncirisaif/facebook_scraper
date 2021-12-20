import service.constants as c
from pymongo import MongoClient
import json



try:
    client = MongoClient(c.MONGODB_URL, username=c.USERNAME, password=c.PASSWORD)
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
    
db = client.facebook
collection = db.posts

# scrape facebook page posts and save into the database
def scrape_save(posts : list):
    return db.posts.insert_many(posts)

def search_element(post_id:int):
    post={}
    results = collection.find_one({'post_id':str(post_id)})
    post[results['post_id']]={'text': results['text'], 'post_text': results['post_text'], 'shared_text': results['shared_text'], 'time': results['time'], 'image': results['image'], 'image_lowquality': results['image_lowquality'], 'images': results['images'], 'images_description': results['images_description'], 'images_lowquality': results['images_lowquality'], 'images_lowquality_description': results['images_lowquality_description'], 'video': results['video'], 'video_duration_seconds': results['video_duration_seconds'], 'video_height': results['video_height'], 'video_id': results['video_id'], 'video_quality': results['video_quality'], 'video_size_MB': results['video_size_MB'], 'video_thumbnail': results['video_thumbnail'], 'video_watches': results['video_watches'], 'video_width': results['video_width'], 'likes': results['likes'], 'comments': results['comments'], 'shares': results['shares'], 'post_url': results['post_url'], 'link': results['link'], 'user_id': results['user_id'], 'username': results['username'], 'user_url': results['user_url'], 'is_live': results['is_live'], 'factcheck': results['factcheck'], 'shared_post_id': results['shared_post_id'], 'shared_time': results['shared_time'], 'shared_user_id': results['shared_user_id'], 'shared_username': results['shared_username'], 'shared_post_url': results['shared_post_url'], 'available': results['available'], 'comments_full': results['comments_full'], 'reactors': results['reactors'], 'w3_fb_url': results['w3_fb_url'], 'reactions': results['reactions'], 'reaction_count': results['reaction_count'], 'image_id': results['image_id'], 'image_ids': results['image_ids']}
    return post
    
def get_all():
    posts={}
    results = list(collection.find({}))
    for i in range(len(results)):
        posts[results[i]['post_id']]={'text': results[i]['text'], 'post_text': results[i]['post_text'], 'shared_text': results[i]['shared_text'], 'time': results[i]['time'], 'image': results[i]['image'], 'image_lowquality': results[i]['image_lowquality'], 'images': results[i]['images'], 'images_description': results[i]['images_description'], 'images_lowquality': results[i]['images_lowquality'], 'images_lowquality_description': results[i]['images_lowquality_description'], 'video': results[i]['video'], 'video_duration_seconds': results[i]['video_duration_seconds'], 'video_height': results[i]['video_height'], 'video_id': results[i]['video_id'], 'video_quality': results[i]['video_quality'], 'video_size_MB': results[i]['video_size_MB'], 'video_thumbnail': results[i]['video_thumbnail'], 'video_watches': results[i]['video_watches'], 'video_width': results[i]['video_width'], 'likes': results[i]['likes'], 'comments': results[i]['comments'], 'shares': results[i]['shares'], 'post_url': results[i]['post_url'], 'link': results[i]['link'], 'user_id': results[i]['user_id'], 'username': results[i]['username'], 'user_url': results[i]['user_url'], 'is_live': results[i]['is_live'], 'factcheck': results[i]['factcheck'], 'shared_post_id': results[i]['shared_post_id'], 'shared_time': results[i]['shared_time'], 'shared_user_id': results[i]['shared_user_id'], 'shared_username': results[i]['shared_username'], 'shared_post_url': results[i]['shared_post_url'], 'available': results[i]['available'], 'comments_full': results[i]['comments_full'], 'reactors': results[i]['reactors'], 'w3_fb_url': results[i]['w3_fb_url'], 'reactions': results[i]['reactions'], 'reaction_count': results[i]['reaction_count'], 'image_id': results[i]['image_id'], 'image_ids': results[i]['image_ids']}
    return posts

def delete_one_post(post_id : int):    
    collection.delete_one({"post_id":str(post_id)})
    
def drop_collection():
    collection.drop()


