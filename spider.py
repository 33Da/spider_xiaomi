import requests
from lxml import etree

class SpiderXiaoMi:
    # 爬取url
    url = "http://list.mi.com/"

    def start_spider(self):
        # 获取响应
        response = requests.get(self.url)

        # 获取html
        html = response.text

        # 解析
        selector = etree.HTML(html)

        # 结果字典
        result = {}



        i = 0

        #  获取到每个的种类和对应物品
        for e in selector.xpath('//li[@class="nav-item"]'):


            types = e.xpath('.//a[@class="link"]//span[@class="text"]/text()')   # 获取种类
            for t in types :
                if t.strip() != "":  # 将空的去掉
                    type = t.strip()


            # 获取每个货物
            goods = e.xpath('.//ul[@class="children-list clearfix"]//a/text()')

            money = e.xpath('.//p[@class="price"]/text()')

            goods_dict = {}  # {good:money}

            goods_dict_list = []   # [{good:money},{good:money},{good:money}....]


            for index in range(len(goods)):
                if goods[index] == "查看全部":   # 错误项
                    break
                goods_dict[goods[index]] = money[index]

                goods_dict_list.append(goods_dict)

                goods_dict = {}




            if type != '服务' and type != '社区':  # 错误项
                result[type] = goods_dict_list
        print(result)

        return result











