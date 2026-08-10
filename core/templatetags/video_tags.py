from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    if not url:
        return url
    
    patterns = [
        (r'(?:https?://)?(?:www\.)?youtube\.com/watch\?.*v=([a-zA-Z0-9_-]{11})', r'https://www.youtube.com/embed/\1'),
        (r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})', r'https://www.youtube.com/embed/\1'),
        (r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})', r'https://www.youtube.com/embed/\1'),
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, url):
            return re.sub(pattern, replacement, url)
    
    return url
