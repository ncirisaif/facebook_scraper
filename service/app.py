from fastapi import FastAPI , HTTPException, status 
from service.scraper import facebook_scraper
import  service.constants as c
from database.database_manager import *


app = FastAPI()

@app.get("/")
async def root():
    return {"FACEBOOK": "SCRAPER"}

@app.get("/get_all_posts/")
async def get_all_posts():
    try:
        return get_all()
    except Exception as error:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=error)

@app.get("/get_one_post_by_id")
async def get_one_post(post_id:int):
    try:
        print("not done", post_id)
        return search_element(post_id)
    except Exception as error:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                 detail=f"Post with ID {post_id} not found")

@app.put("/scrape_save_posts")
async def scraping(pagename:str=c.PAGE_NAME):
    try:
        posts = facebook_scraper(pagename)
        scrape_save(posts)
    except Exception as error:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=error)

@app.delete("/delete_one/")
async def delete_post(post_id : int):
    try:
        return delete_one_post(post_id)
    except Exception as error:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=error)

@app.delete("/delete_all")
async def delete_all():
    try:
        return drop_collection()
        print(deleted)
    except Exception as error:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=error)

