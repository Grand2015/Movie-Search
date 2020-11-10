

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
import requests         # 网页请求模块
from lxml import etree  # 网页请求数据解析模块
from django.http import HttpResponse
'''
# 对于 >= Python 3.4：
import importlib
import sys
importlib.reload(sys)

Python 2.X
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
url = 'https://movie.douban.com/subject/1292600/'


def get_movie_info(headers_in, url_in):
    r = requests.get(url_in, headers=headers_in)
    html = etree.HTML(r.text)
    # u8 = etree.tostring(html, encoding="utf-8", pretty_print=True, method="html").decode("utf-8")
    name = html.xpath('//*[@id="content"]/h1/span[1]/text()')
    # print(name[0])

    point = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    # print(point)

    contact = html.xpath('//*[@id="link-report"]/span/text()')
    # contact = contact.strip()
    return name[0], point[0], contact[0]


def movie_search(request):
    url_str = "<a href='" + url + "'>Click Here</a>"
    movie_dict = {}
    if request.GET:
        movie_name, movie_point, movie_contact = get_movie_info(headers, url)
        movie_dict['movie'] = movie_name
        movie_dict['mark'] = movie_point
        movie_dict['comment'] = movie_contact
        movie_dict['linkage'] = url_str
    return render(request, "movieSearch.html", {"movie_dict": movie_dict})

