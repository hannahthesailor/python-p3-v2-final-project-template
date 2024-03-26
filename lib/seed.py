from models.blog import Blog
from models.post import Post

from models.__init__ import CONN, CURSOR

if __name__ == "__main__":

    Blog.create_table()
    Post.create_table()

    CURSOR.execute("DELETE FROM blogs")
    CURSOR.execute("DELETE FROM posts")
    CONN.commit()

    Blog.create("Recipes")
    Blog.create("Weekly Check In")

    Post.create("Protein Pancakes", "2 large Eggs, ½ cup Sour cream or plain full fat Greek Yogurt, (note 1), 2 servings Protein powder, (note 3), 1 teaspoon Baking powder, Cooking spray, butter, or coconut oil for greasing the pan", 1)
    Post.create("Jan 7, 2024", "This week felt so long! While I was able to get all my work done, I wasn't left with much time to do things for myself. I am feeling very drained but looking forward to resting up with weekend! I am definitely going to check out the new Pad Thai place with my friends at somepoint. The weathe is supposeto be decent so I'm going to do some cleaning with the windows open to really refresh the house.", 2)
    Post.create("Title", "Text of the third post", 1)
    Post.create("Title", "Text of the fourth post", 1)
    Post.create("Title", "Text of the fifth post", 2)
    Post.create("Title", "Text of the sixth post", 2)