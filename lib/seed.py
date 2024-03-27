from models.blog import Blog
from models.post import Post

from models.__init__ import CONN, CURSOR

if __name__ == "__main__":

    Blog.create_table()

    # Post.drop_table()
    Post.create_table()

    CURSOR.execute("DELETE FROM blogs")
    CURSOR.execute("DELETE FROM posts")
    CONN.commit()

    Blog.create("Recipes")
    Blog.create("Weekly Check In")

    Post.create("Protein Pancakes", "2 large Eggs, ½ cup Sour cream or plain full fat Greek Yogurt, (note 1), 2 servings Protein powder, (note 3), 1 teaspoon Baking powder, Cooking spray, butter, or coconut oil for greasing the pan", 1)
    Post.create("Jan 7, 2024", "This week felt so long! While I was able to get all my work done, I wasn't left with much time to do things for myself. I am feeling very drained but looking forward to resting up with weekend! I am definitely going to check out the new Pad Thai place with my friends at somepoint. The weathe is supposeto be decent so I'm going to do some cleaning with the windows open to really refresh the house.", 2)
    Post.create("Feb 11, 2024 ", "So much to do this week but it's too cold to stay motivated! Hoping the grounhog was right and we get an early spring!", 2)
    Post.create("Milkshake", "2 cups (about 480ml) vanilla ice cream, 1/2 cup (120ml) whole mill, 1 teaspoon vanilla extract, Whipped cream (optional, for topping), Maraschino cherry (optional, for garnish)", 1)
    Post.create("Chocolate Chip Cookies", "1 cup (2 sticks or 226g) unsalted butter, softened, 3/4 cup (150g) granulated sugar, 3/4 cup (150g) packed brown sugar,2 large eggs", 1)
    Post.create("March 12, 2024", "A pretty good week! Went hiking this weekend but it's already cold again. So ready for spring!", 2)