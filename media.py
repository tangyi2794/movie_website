#!/usr/bin/env python
# coding:utf-8


class Movie():
    """视频模型类"""

    def __init__(self, _title, _poster_image_url, _trailer_youtube_url):
        """
        _title  视频标题
        _poster_image_url   视频封面URL
        _trailer_youtube_url   视频url
        """
        self.title = _title  # 视频标题
        self.poster_image_url = _poster_image_url     # 视频封面URL
        self.trailer_youtube_id = _trailer_youtube_url  # 视频id
        self.trailer_youtube_url = _trailer_youtube_url  # 视频url
