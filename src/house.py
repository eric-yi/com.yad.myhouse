#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __init__ import *

class HousePage:
    def __init__(self, _page):
        self.total = -1
        self.next_link = None
        self.houses = []

        if 'total' in _page:
            self.total = _page['total']
        if 'next_link' in _page:
            self.next_link = _page['next_link']
        if 'houses' in _page:
            self.houses = _page['houses']


class House:
    def __init__(self, _house):
        self.name = None
        self.village_name = None
        self.village_phase = None
        self.description = None
        self.link = None
        self.rooms = -1
        self.policy = None
        self.orientation = None
        self.storey = None
        self.building = None
        self.age = -1
        self.address = None
        self.agent = None
        self.covered_area = -1
        self.used_area = -1
        self.total_price = -1
        self.centiare_price = -1


        if 'name' in _house:
            # 名称
            self.name = _house['name']
        if 'village_name' in _house:
            # 小区名称
            self.village_name = _house['village_name']
        if 'village_phase' in _house:
            # 小区几期
            self.village_phase = _house['village_phase']
        if 'description' in _house:
            # 描述
            self.description = _house['description']
        if 'link' in _house:
            # 详情链接
            self.link = _house['link']
        if 'rooms' in _house:
            # 户型
            self.rooms = _house['rooms']
        if 'policy' in _house:
            # 满五唯一
            self.policy = _house['policy']
        if 'orientation' in _house:
            # 朝向
            self.orientation = _house['orientation']
        if 'storey' in _house:
            # 楼层
            self.storey = _house['storey']
        if 'building' in _house:
            # 整栋类型
            self.building = _house['building']
        if 'age' in _house:
            # 建筑年代
            self.age = _house['age']
        if 'address' in _house:
            # 地址
            self.address = _house['address']
        if 'agent' in _house:
            # 中介
            self.agent = _house['agent']
        if 'covered_area' in _house:
            # 建筑面积
            self.covered_area = _house['covered_area']
        if 'used_area' in _house:
            # 使用面积
            self.used_area = _house['used_area']
        if 'total_price' in _house:
            # 价格
            self.total_price = _house['total_price']
        if 'centiare_price' in _house:
            # 每平价格
            self.centiare_price = _house['centiare_price']


    def __str__(self):
        return ('name: %s, village_name: %s, village_name: %s, description: %s, ' +
                'link: %s, rooms: %f, policy: %s, ' +
                'orientation: %s, storey: %s, building: %s, age: %d, ' +
                'address: %s, agent: %s, covered area: %d, used area: %d, ' +
                'total price: %d, centiare price: %d') % (
                    self.name,
                    self.village_name,
                    self.village_phase,
                    self.description,
                    self.link,
                    self.rooms,
                    self.policy,
                    self.orientation,
                    self.storey,
                    self.building,
                    self.age,
                    self.address,
                    self.agent,
                    self.covered_area,
                    self.used_area,
                    self.total_price,
                    self.centiare_price
                )

