#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *
from bs4 import BeautifulSoup
import re
from house import House
from house import HousePage

def extract(html):
    total, next_link, houses = extract_page(html)
    return HousePage({
        'total': total,
        'next_link': next_link,
        'houses': houses
        })

def extract_page(html):
    soup = BeautifulSoup(html)
    # get total pages
    total_element = soup.find('span', {'class' : 'txt'})
    total_str = total_element.get_text()
    #logger.debug('total string : %s' % (total_str))
    total = int(total_str[1])
    #logger.debug('total = %d' % (total))
    # get house information, using house class
    #house_elements = soup.find_all(re.compile('^dl'))[1 : ]
    house_elements = soup.find_all('dl', id=re.compile('^list_\w+_\d+'))
    houses = convert(house_elements)

    next_link = None
    try:
        link_element = soup.find(id='PageControl1_hlk_next')
        next_link = link_element['href']
        #logger.debug('next_link: %s' % (next_link))
    except Exception, e:
        logger.warn(e)

    return total, next_link, houses

def convert(house_elements):
    houses = []
    for house_element in house_elements:
        _house_dict = {}

        house_title_element = house_element.find('p', {'class' : 'title'}).a
        link = house_title_element['href']
        description = house_title_element.get_text()

        storey = -1
        building = -1
        orientation = None
        age = -1
        try:
            house_rooms_element = house_element.find('p', {'class' : 'mt12'})
            rooms_str = house_rooms_element.get_text().strip()
            rooms = float(rooms_str[0]) + float(rooms_str[2]) / 10
            rooms_array = rooms_str.split('\n')
            _tmp = rooms_array[2].strip()
            storey = _tmp[1:3]
            building = int(_tmp.split('层(共')[1].split('层)')[0])
            orientation = rooms_array[3].strip()[1:]
            age = int(rooms_array[4].split('：')[1])
        except Exception, e:
            logger.warn(e)

        house_sub_element = house_element.find('p', {'class' : 'mt10'})
        name = house_sub_element.a['title']
        village_name = house_sub_element.a.strong.get_text()
        village_phase = house_sub_element.a.get_text().strip(village_name)
        address = house_sub_element.get_text().strip(house_sub_element.a.get_text()).strip()

        try:
            house_sub_element = house_element.find('p', {'class' : 'gray6 mt10'})
            agent = house_sub_element.a.get_text().strip()
        except Exception, e:
            agent = None
            logger.error(e)

        house_sub_element = house_element.find('div', {'class' : 'pt4 floatl'})
        _policy = house_sub_element.find('span', {'class' : 'colorGreen note'})
        if _policy:
            policy = _policy.get_text().strip()
        else:
            policy = ''


        house_sub_element = house_element.find('div', {'class' : 'area alignR'}).find_all('p')
        covered_area = int(house_sub_element[0].get_text().strip())

        house_sub_element = house_element.find('div', {'class' : 'moreInfo'})
        total_price = int(house_sub_element.find('span', {'class' : 'price'}).get_text().strip()) * 10000
        centiare_price = int(house_sub_element.find('p', {'class' : 'danjia alignR mt5'}).get_text().strip().strip('元/'))

        _house_dict = {
            'name': name,
            'village_name': village_name,
            'village_phase': village_phase,
            'link': link,
            'description': description,
            'rooms': rooms,
            'age': age,
            'orientation': orientation,
            'storey': storey,
            'building': building,
            'address': address,
            'agent': agent,
            'policy': policy,
            'covered_area': covered_area,
            'total_price': total_price,
            'centiare_price': centiare_price
        }
        house = House(_house_dict)
        logger.debug('house : %s' % (house))
        houses.append(house)

    return houses
