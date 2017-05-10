#!/usr/bin/env python
# coding:utf-8

class Movie():
    """视频模型类"""

    def __init__(self, _title, _poster_image_url, _trailer_youtube_url):
        self.title = _title
        self.poster_image_url = _poster_image_url
        self.trailer_youtube_id = _trailer_youtube_url
        self.trailer_youtube_url = _trailer_youtube_url
