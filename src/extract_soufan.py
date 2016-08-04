#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
from bs4 import BeautifulSoup
import re
from house import House

def extract_first_page(html):
    soup = BeautifulSoup(html)
    # get total pages
    total_element = soup.find('span', {'class' : 'txt'})
    total_str = total_element.get_text()
    logger.debug('total string : %s' % (total_str))
    total = int(total_str[1])
    logger.debug('total = %d' % (total))
    # get house information, using house class
    #house_elements = soup.find_all(re.compile('^dl'))[1 : ]
    house_elements = soup.find_all('dl', id=re.compile('^list_\w+_\d+'))
    houses = convert(house_elements)

    return total, houses

def convert(house_elements):
    houses = []
    for house_element in house_elements:
        _house_dict = {}

        house_title_element = house_element.find('p', {'class' : 'title'}).a
        link = house_title_element['href']
        description = house_title_element.get_text()

        house_rooms_element = house_element.find('p', {'class' : 'mt12'})
        rooms_str = house_rooms_element.get_text().strip()
        logger.debug('rooms_str: %s' % (rooms_str))
        rooms = float(rooms_str[0]) + float(rooms_str[2]) / 10
        rooms_array = rooms_str.split('\n')
        logger.debug('rooms_str: %s' % (rooms_array))
        rooms_array[2]
        rooms_array[3]
        logger.debug('rooms_array[4] %s' % (rooms_array[4]))
        age = int(rooms_array[4].split('：')[1])

        _house_dict = {
            'link': link,
            'description': description,
            'rooms': rooms,
            'age': age
        }
        house = House(_house_dict)
        logger.debug('house : %s' % (house))
        houses.append(house)


    return houses
