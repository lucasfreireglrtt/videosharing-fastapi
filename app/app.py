from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends  
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {1: {"title": "First Post", "content": "This is the first post."},
              2: {"title": "Second Post", "content": "This is the second post."},
              3: {"title": "Third Post", "content": "This is the third post."},
              4: {"title": "Fourth Post", "content": "This is the fourth post."},
              5: {"title": "Fifth Post", "content": "This is the fifth post."},
              6: {"title": "Sixth Post", "content": "This is the sixth post."},
              7: {"title": "Seventh Post", "content": "This is the seventh post."},
              8: {"title": "Eighth Post", "content": "This is the eighth post."},
              9: {"title": "Ninth Post", "content": "This is the ninth post."},
                10: {"title": "Tenth Post", "content": "This is the tenth post."}}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return dict(list(text_posts.items())[:limit])
    return text_posts

@app.get("/posts/{post_id}")
def get_post(id: int) -> list[PostResponse]:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    post=Post(
        caption=caption,
        url='dummy url',
        file_type='photo',
        file_name='dummy name')
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

