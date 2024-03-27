from models.__init__ import CONN, CURSOR

class Post:

    all = []
    
    def __init__(self, title, text, blog_id):
        self.title = title
        self.text = text
        self.blog_id = blog_id
        self.id = None

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_add):
        if(isinstance(title_add, str)) and (0 < len(title_add) <= 25):
            self._title = title_add
        else:
            raise ValueError("Must be beteween 1 and 25 characters!")

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_add):
        if(isinstance(text_add, str)) and (0 < len(text_add)):
            self._text = text_add
        else:
            raise ValueError("Must contain at least one character!")

    @property
    def blog_id(self):
        return self._blog_id
    
    @blog_id.setter
    def blog_id(self, blog_id_name):
        if(isinstance(blog_id_name, int)):
            self._blog_id = blog_id_name
        else:
            raise ValueError("Blog ID must be an integer.")

    def __repr__(self):
        return f"<Post {self.id}: Title = {self.title}, Text = {self.text}, Blog ID = {self.blog_id}>"

    # CRUD methods

    @classmethod
    def create_table(cls):
        # Create
        sql = """
            CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            text TEXT,
            blog_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        # Drop
        sql = """
            DROP TABLE IF EXISTS posts;
        """
        CURSOR.execute(sql)

    def save(self):
        # insert / update
        sql = """
            INSERT INTO posts (title, text, blog_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.text, self.blog_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Post.all.append(self)

    @classmethod
    def create(cls, title, text, blog_id):
        #create instance
        post = cls(title, text, blog_id)
        post.save()
        return post
    
    @classmethod
    def instance_from_db(cls, row):
        # return post
        post = cls(row[1], row[2], row[3])
        post.id = row[0]
        return post
    
    @classmethod
    def get_all(cls):
        # return 
        sql = """
            SELECT *
            FROM posts
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM posts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        # update post
        sql = """
            UPDATE posts
            SET title = ?, text = ?, blog_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.text, self.blog_id, self.id))
        CONN.commit()

    def delete(self):
        # delete post
        sql = """
            DELETE FROM posts
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    
        Post.all = [post for post in Post.all if post.id != self.id]
    
    def blog(self):
        # post belongs to blog
        from models.blog import Blog

        sql = """
            SELECT blogs.id, blogs.name
            FROM blogs
            INNER JOIN posts
            ON blogs.id = posts.blog_id
            WHERE posts.blog_id = ?
        """

        row = CURSOR.execute(sql, (self.blog_id,)).fetchone()
        
        if row:
            return Blog.instance_from_db(row)
        else:
            return None