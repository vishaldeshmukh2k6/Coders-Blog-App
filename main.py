from app import app,db
import views
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == "__main__":
    app.run(port=5018)



