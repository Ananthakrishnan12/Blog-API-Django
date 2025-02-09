# Blog-API-Django
This is a RESTful API for a blog platform built using Django and Django Rest Framework (DRF). 
It provides endpoints for managing blog posts, user authentication, pagination, and request throttling.

## Features
- 🔹 **CRUD Operations**: Create, Read, Update, and Delete blog posts.
- 🔹 **User Authentication**: Token-based authentication using DRF.
- 🔹 **Pagination**: Efficiently fetch blog posts with paginated results.
- 🔹 **Throttling**: Rate limit requests to prevent abuse.
- 🔹 **Filtering & Searching**: Retrieve blog posts based on different criteria.

## Tech Stack
- **Backend**: Django, Django Rest Framework (DRF)
- **Database**: SQLite 
- **Authentication**: DRF Token Authentication 

## Database Model

### BlogPost  
The **BlogPost** model represents a blog post created by a user.

#### Fields:  
- **title** (*CharField*): Stores the blog post title (max length: 100).  
- **content** (*TextField*): Contains the blog content.  
- **author** (*ForeignKey to User*): Links the post to a registered user.  
- **created_at** (*DateTimeField*): Automatically records when the post was created.  
- **updated_at** (*DateTimeField*): Automatically updates when the post is modified.  
- **is_published** (*BooleanField*): Defines whether the post is published (default: `False`).  
- **total_likes** (*IntegerField*): Stores the number of likes on the post (default: `0`).  

---

### Comment  
The **Comment** model allows users to leave comments on a blog post.

#### Fields:  
- **comment_user** (*ForeignKey to User*): The user who commented.  
- **likes** (*PositiveIntegerField*): Tracks likes (either `0` or `1`, using validators).  
- **comments** (*TextField*): Stores the actual comment text.  
- **blogpost** (*ForeignKey to BlogPost*): Links the comment to a specific blog post.  
- **created** (*DateTimeField*): Timestamp when the comment was created.  
- **updated** (*DateTimeField*): Timestamp when the comment was last updated.  


# API Testing Tool: 🔬 POSTMAN 

# Endpoints: (with Demo Gif) wait for a few seconds...

- **Register**  
  ![Register API Demo](https://github.com/Ananthakrishnan12/Blog-API-Django/blob/main/demo/Blog-API-registeration.gif?raw=true)  

- **Login**  
  ![Login API Demo](https://github.com/Ananthakrishnan12/Blog-API-Django/blob/main/demo/Blog-API-login.gif?raw=true)  

- **Post Create & Get (List)**  
  ![BlogPost Create & List API Demo](https://github.com/Ananthakrishnan12/Blog-API-Django/blob/main/demo/Blog-API-Post-Create-_-List-.gif?raw=true)  

- **Post Comment Create & Get (List)**  
  ![BlogPost Comment Create & List API Demo](https://github.com/Ananthakrishnan12/Blog-API-Django/blob/main/demo/Blog-API-Post-Comment-Create-_-List-.gif?raw=true)  

- **Logout**  
  ![Logout API Demo](https://github.com/Ananthakrishnan12/Blog-API-Django/blob/main/demo/Blog-API-logout.gif?raw=true)  

