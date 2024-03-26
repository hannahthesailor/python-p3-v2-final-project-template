import sqlite3

CONN = sqlite3.connect('blog_post.db')
CURSOR = CONN.cursor()
