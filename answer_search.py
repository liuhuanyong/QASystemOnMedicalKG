#!/usr/bin/env python3
# coding: utf-8
# File: answer_search.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-5

from py2neo import Graph,Node

class AnswerSearcher:
    def __init__(self):
        self.g = Graph(
            host="127.0.0.1",
            http_port=7474,
            user="lhy",
            password="lhy123")

    '''执行cypher查询，并返回相应结果'''
    def search_main(self, sqls):
        for sql in sqls:
            ress = self.g.run(sql).data()
            for res in ress:
                print(res)
        return




if __name__ == '__main__':
    searcher = AnswerSearch()