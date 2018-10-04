#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

import os

from py2neo import Graph,Node
from question_classifier import *
from question_parser import *


class ChatBotGraph:
    def __init__(self):
        self.g = Graph(
            host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            http_port=7474,  # neo4j 服务器监听的端口号
            user="lhy",  # 数据库user name，如果没有更改过，应该是neo4j
            password="lhy123")
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()

    def chat_main(self, sent):
        answer = '对不起，小生愚钝，祝您身体健康！每天开开心心的....'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            answer = '对不起，小生愚钝，祝您身体健康！每天开开心心的....'
        res_parse = self.parser.parser_main(res_classify)
        return answer

if __name__ == '__main__':
    handler = ChatBotGraph()
    question = '感冒有什么特效药'
    handler.chat_main(question)
