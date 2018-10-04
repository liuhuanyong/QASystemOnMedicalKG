#!/usr/bin/env python3
# coding: utf-8
# File: question_parser.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

class QuestionPaser:
    def __init__(self):
        return

    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    '''解析主函数'''
    def parser_main(self, res_classify):
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_type = res_classify['question_type']
        if question_type == 'disease_symptom':
            datas = [['rel', 'Disease', name, 'has_symptom', 'Symptom'] for name in entity_dict.get('disease')]
        elif question_type == 'disease_cause':
            datas = [['attr', 'Disease', name, 'cause'] for name in entity_dict.get('disease')]
        elif question_type == 'disease_acompany':
            datas = [['rel', 'Disease', name, 'acompany', 'Disease'] for name in entity_dict.get('disease')]
        elif question_type == 'disease_not_food':
            datas = [['rel', 'Disease', name, 'not_eat', 'Food'] for name in entity_dict.get('disease')]
        elif question_type == 'disease_do_food':
            datas = [['rel', 'Disease', name, 'do_eat', 'Food'] for name in entity_dict.get('disease')]
        elif question_type == 'disease_drug':
            datas = [['rel', 'Disease', name, 'common_drug', 'Drug'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_drug':#TODO
            a = 1
        elif question_type == 'disease_prevent':
            datas = [['attr', 'Disease', name, 'prevent'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_prevent':#TODO
            a = 1
        elif question_type == 'disease_lasttime':
            datas = [['attr', 'Disease', name, 'cure_lasttime'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_lasttime':#TODO
            a = 1
        elif question_type == 'disease_cureway':
            datas = [['attr', 'Disease', name, 'cure_way'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_cureway':#TODO
            a = 1
        elif question_type == 'disease_cureprob':
            datas = [['attr', 'Disease', name, 'cured_prob'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_cureprob':#TODO
            a = 1
        elif question_type == 'disease_easyget':
            datas = [['attr', 'Disease', name, 'easy_get'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_easyget':#TODO
            a = 1
        elif question_type == 'disease_check':
            datas = [['rel', 'Disease', name, 'need_check', 'Check'] for name in entity_dict.get('disease')]
        elif question_type == 'symptom_disease_check':#TODO
            a = 1
        elif question_type == 'drug_disease':
            datas = [['rel', 'Disease','common_drug', 'Drug', name] for name in entity_dict.get('drug')]
        elif question_type == 'others':#TODO
            a = 1


if __name__ == '__main__':
    handler = QuestionPaser()
