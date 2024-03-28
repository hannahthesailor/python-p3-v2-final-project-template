from models.__init__ import CONN, CURSOR

class Blog:

    all = []
    
    def __init__(self, name):
        self.name = name
        self.id = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (0 < len(name_parameter) <= 150):
            self._name = name_parameter
        else:
            raise ValueError("Try a different title!")
        
    def __repr__(self):
        return f"<Blog {self.id}: Name = {self.name}>"
    
    # ORM methods

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS blogs;
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO blogs (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Blog.all.append(self)

#CRUD
        
    @classmethod
    def create(cls, name):
        # create new blog and save
        blog = cls(name)
        blog.save()
        return blog
    
    @classmethod
    def instance_from_db(cls, row):
        blog = cls(row[1])
        blog.id = row[0]
        return blog

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM blogs
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        # Return
        sql = """
            SELECT *
            FROM blogs
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        # Update
        sql = """
            UPDATE blog
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        # Delete
        sql = """
            DELETE FROM blogs
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Blog.all = [blog for blog in Blog.all if blog.id != self.id]

    def posts(self):
        # One-to-many blog has many posts, post belongs to one blog
        from models.post import Post

        sql = """
            SELECT *
            FROM posts
            WHERE posts.blog_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Post.instance_from_db(row) for row in rows]