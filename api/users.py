from sqlalchemy.orm import joinedload
from models import User, Post

def get_user_posts(db, user_id: int) -> list[Post]:
    return (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .options(joinedload(Post.author))
        .all()
    )
