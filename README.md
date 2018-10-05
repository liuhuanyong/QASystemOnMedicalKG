# QABasedOnMedicaKnowledgeGraph
self-implement of disease centered Medical graph from zero to full and sever as question answering base. 从无到有搭建一个以疾病为中心的一定规模医药领域知识图谱，并以该知识图谱完成自动问答与分析服务。

# 项目介绍

知识图谱是目前自然语言处理的一个热门方向，本人参加了ccks2018会议，并得到一些收获，可以查看我的ccks2018参会总结(https://github.com/liuhuanyong/CCKS2018Summary )。  
与知识图谱相关的另一种形态，即事理图谱，本人在这方面也尝试性地积累了一些工作，可参考：(https://github.com/liuhuanyong/ComplexEventExtraction )  
关于知识图谱概念性的介绍就不在此赘述。目前知识图谱在各个领域全面开花，如教育、医疗、司法、金融等。本项目立足医药领域，以垂直型医药网站为数据来源，以疾病为核心，构建起一个包含7类规模为4.4万的知识实体，11类规模约30万实体关系的知识图谱。
本项目将包括以下两部分的内容：
1) 基于垂直网站数据的医药知识图谱构建
2) 基于医药知识图谱的自动问答

# 项目最终效果
话不多少，直接上图。以下两图是实际问答运行过程中的截图：
![image](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/chat1.png)

![image](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/chat2.png)

# 项目运行：
1、配置要求：要求配置neo4j数据库及相应的python依赖包。neo4j数据库用户名密码记住，并修改相应文件。
2、知识图谱数据导入：python build_medicalgraph.py，导入的数据较多，估计需要几个小时。
3、启动问答：python chat_graph.py

# 一、医疗知识图谱构建
# 1.1 业务驱动的知识图谱构建框架
![image](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/kg_route.png)

# 1.2 脚本目录
prepare_data/datasoider.py：网络资讯采集脚本  
prepare_data/datasoider.py：网络资讯采集脚本  
prepare_data/max_cut.py：基于词典的最大向前/向后切分脚本  
build_medicalgraph.py：知识图谱入库脚本    　　

# 1.3 医药领域知识图谱规模
1.3.1 neo4j图数据库存储规模
![image](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/graph_summary.png)

1.3.2 知识图谱实体类型

| 实体类型 | 中文含义 | 实体数量 |举例 |
| :--- | :---: | :---: | :--- |
| Check | 诊断检查项目 | 3,353| 支气管造影;关节镜检查|
| Department | 医疗科目 | 54 |  整形美容科;烧伤科|
| Disease | 疾病 | 8,807 |  血栓闭塞性脉管炎;胸降主动脉动脉瘤|
| Drug | 药品 | 3,828 |  京万红痔疮膏;布林佐胺滴眼液|
| Food | 食物 | 4,870 |  番茄冲菜牛肉丸汤;竹笋炖羊肉|
| Producer | 在售药品 | 17,201 |  通药制药青霉素V钾片;青阳醋酸地塞米松片|
| Symptom | 疾病症状 | 5,998 |  乳腺组织肥厚;脑实质深部出血|
| Total | 总计 | 44,111 | 约4.4万实体量级|

1.3.3 知识图谱实体关系类型

| 实体关系类型 | 中文含义 | 关系数量 | 举例|
| :--- | :---: | :---: | :--- |
| belongs_to | 属于 | 8,844| <妇科,属于,妇产科>|
| common_drug | 疾病常用药品 | 14,649 | <阳强,常用,甲磺酸酚妥拉明分散片>|
| do_eat |疾病宜吃食物 | 22,238| <胸椎骨折,宜吃,黑鱼>|
| drugs_of |  药品在售药品 | 17,315| <青霉素V钾片,在售,通药制药青霉素V钾片>|
| need_check | 疾病所需检查 | 39,422| <单侧肺气肿,所需检查,支气管造影>|
| no_eat | 疾病忌吃食物 | 22,247| <唇病,忌吃,杏仁>|
| recommand_drug | 疾病推荐药品 | 59,467 | <混合痔,推荐用药,京万红痔疮膏>|
| recommand_eat | 疾病推荐食谱 | 40,221 | <鞘膜积液,推荐食谱,番茄冲菜牛肉丸汤>|
| has_symptom | 疾病症状 | 5,998 |  <早期乳腺癌,疾病症状,乳腺组织肥厚>|
| acompany_with | 疾病并发疾病 | 12,029 | <下肢交通静脉瓣膜关闭不全,并发疾病,血栓闭塞性脉管炎>|
| Total | 总计 | 294,149 | 约30万关系量级|

1.3.4 知识图谱属性类型

| 属性类型 | 中文含义 | 举例 |
| :--- | :---: | :---: |
| name | 疾病名称 | 喘息样支气管炎 |
| desc | 疾病简介 | 又称哮喘性支气管炎... |
| cause | 疾病病因 | 常见的有合胞病毒等...|
| prevent | 预防措施 | 注意家族与患儿自身过敏史... |
| cure_lasttime | 治疗周期 | 6-12个月 |
| cure_way | 治疗方式 | "药物治疗","支持性治疗" |
| cured_prob | 治愈概率 | 95% |
| easy_get | 疾病易感人群 | 无特定的人群 |


# 二、基于医疗知识图谱的自动问答
# 2.1 技术架构
![image](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/qa_route.png)


# 2.2 脚本结构
question_classifier.py：问句类型分类脚本  
question_parser.py：问句解析脚本  
chatbot_graph.py：问答程序脚本  

# 2.3 效果展示

be soon....

# 总结

If any question about the project or me ,see https://liuhuanyong.github.io/











