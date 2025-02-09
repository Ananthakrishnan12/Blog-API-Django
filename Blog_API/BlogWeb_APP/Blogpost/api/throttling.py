from rest_framework.throttling import UserRateThrottle

class BlogListThrottle(UserRateThrottle):
    scope = 'Blog-list'