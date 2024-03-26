# from models.__init__ import CONN, CURSOR

# class Author:


#     def __init__(self, first_name, last_name, username):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username

#     @property
#     def username(self):
#         return self._username
    
#     @username.setter
#     def username(self, username_name):
#         if(isinstance(username_name, str)) and  (0 < len(username_name) <= 150 and not hasattr(self, "username_name")):
#             self._username = username_name
#         else:
#             raise ValueError("Username must be at least 1 character and no more than 25 and unique")
        
#     @property
#     def first_name(self):
#         return self._first_name
    
#     @first_name.setter
#     def first_name(self, first_name_name):
#         pass

#     @property
#     def last_name(self):
#         return self._last_name
    
#     @last_name.setter
#     def last_name(self, last_name_name):
#         pass

#     #other orm

#     # create, drop, save, get all, find, update, delete
