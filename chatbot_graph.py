#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

import os

from question_classifier import *
from question_parser import *
from answer_search import *


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '对不起，小生愚钝，祝您身体健康！每天开开心心的....'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return
        res_sql = self.parser.parser_main(res_classify)
        print(res_sql)
        self.searcher.search_main(res_sql)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('enter an question to search:')
        handler.chat_main(question)

