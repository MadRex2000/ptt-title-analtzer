import json

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"./TaipeiSansTCBeta-Regular.ttf")


def create_data_chart(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, sort_keys=True, separators=(',\n', ': '), ensure_ascii=False)
    chart_data = {}
    for key in data:
        if data[key] > 3:
            chart_data[key] = data[key]
    plt.bar(range(len(chart_data)), chart_data.values(), align='center')
    plt.xticks(range(len(chart_data)), chart_data.keys(), fontproperties=font, rotation=30)
    plt.title('PTT Gossiping Title Analyze')
    plt.ylabel('數量', fontproperties=font)
    plt.xlabel('關鍵詞', fontproperties=font)
    plt.savefig('data.png')
    # plt.show()


def create_push_chart(data):
    with open('push.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, sort_keys=True, separators=(',\n', ': '), ensure_ascii=False)
    data_name = []
    data_push = []
    for detail in data[0:10]:
        data_name.append(detail[0])
        data_push.append(detail[4])
    plt.figure(figsize=(30, 15))
    plt.barh(range(len(data_push)), data_push[::-1], align='center')
    plt.yticks(range(len(data_name)), data_name[::-1], fontproperties=font, rotation=30, size=12)
    plt.title('PTT Gossiping Title Analyze')
    plt.xlabel('推文數', fontproperties=font)
    plt.savefig('push.png')
    # plt.show()


def handle_data(datas):
    cal_data = {}
    for data in datas:
        try:
            details = eval(data[5][1:-1])
            if type(details) == tuple:
                for detail in details:
                    if str(detail['name']) in cal_data:
                        cal_data[str(detail['name'])] += 1
                    else:
                        cal_data[str(detail['name'])] = 1
            else:
                if detail['name'] in cal_data:
                    cal_data[str(detail['name'])] += 1
                else:
                    cal_data[str(detail['name'])] = 1
        except SyntaxError:
            pass
    create_data_chart(cal_data)


def order_key(data):
    try:
        return int(data[4]) if data[4] else 0
    except ValueError:
        return 0


def handle_push(datas):
    data = list(datas)
    data.sort(key=order_key, reverse=True)
    create_push_chart(data)
