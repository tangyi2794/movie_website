#!/usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import media
import fresh_tomatoes

data_file = "data.json"


def data_json_parsing(_json_file):
        # json数据解析 生成list 并且返回
    file = open(_json_file)
    data_list = json.load(file)
    file.close()
    return data_list


def generate_the_data(_data_list):
        # 将解析后的数据放入模型类对象，将对象放入list
    movies = []
    for data_dic in _data_list:
        movie = media.Movie("", "", "")
        movie.title = data_dic["title"]
        movie.poster_image_url = data_dic["poster_image_url"]
        movie.trailer_youtube_id = data_dic["trailer_youtube_url"]
        movie.trailer_youtube_url = data_dic["trailer_youtube_url"]
        # print movie.trailer_youtube_id
        movies.append(movie)  # 将对象放入list
    return movies


def start_website():
        # Program entrance run the logic
    data_list = data_json_parsing(data_file)
    movies = generate_the_data(data_list)
    fresh_tomatoes.open_movies_page(movies)
    # print movies

start_website() #   


