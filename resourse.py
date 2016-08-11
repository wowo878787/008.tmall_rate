# coding:utf-8
import urllib2, requests
import sys, json, random, time

root_doc = 'https://rate.tmall.com/list_detail_rate.htm?itemId=40889098453&spuId=295158557&sellerId=194315137&order=1&append=0&picture=1&currentPage='
min_page = 1
max_page = 2
first_key = '"rateDetail":'
typeEncode = sys.getfilesystemencoding()


def make_urls(root_doc, min_page, max_page):
    '''
    生成所有页面的链接
    :param root_doc: 请求内容的简化地址,细节另补
    :param max_page: 取到的最大页数(淘宝最大99页),因为最后一位取不到所以应给100
    :return: 所有页面url的列表
    '''
    print 'in make_url'
    urls = []
    for i in range(min_page, max_page):
        urls.append(root_doc + str(i))
    print 'out make_url'
    return urls


def get_json(current_url, first_key, typeEncode):
    print 'in get_json'
    '''
    获得工整的json格式数据

    :param current_url: 当前页面的url
    :param first_key: 第一对json数据的键,用于删除,以保持json译码的工整
    :param typeEncode: 当前计算机的编码形式
    :return: 除去第一个键的json格式数据
    '''
    done=0
    while done==0:
        try:
            # json_doc = requests.get(current_url).text
            json_doc = urllib2.urlopen(current_url).read()
            done=1
        except UnboundLocalError:
            print current_url
            time.sleep(180)
            continue
    json_doc = json_doc.decode(typeEncode).encode('utf-8')  # 知乎上的参数写反了,这块要再研究编码的问题,还有那个mbcs的类型是什么
    left_slice = 4 + len(first_key)  # 4我不太记得怎么来的了,好像是会带一行CRLF
    json_doc_sliced = json_doc[left_slice:]
    print 'out get_json'
    return json_doc_sliced


# 当前文件位置
# location=os.path.dirname(__file__)+'//data.json'


def list_elements(json_doc, data_file):
    '''
    往文件里写入重新编排过的有用的信息

    :param json_doc: 一页工整的json格式数据
    :param data_file: 所要保存在什么文件里
    :return: 无
    '''
    # 先将json解析成python字典类型，然后就跟操作字典一样取值
    print 'in list_elements'
    try:
        json_dict = json.loads(json_doc)
    except:
        print json_doc

    for item in json_dict['rateList']:
        data_item = {}
        data_item['id'] = item['id']
        data_item['gmtCreateTime'] = item['gmtCreateTime']
        data_item['auctionSku'] = item['auctionSku']
        data_item['pics'] = item['pics']
        data_item['rateContent'] = item['rateContent']
        if item['appendComment']:
            data_item['appendPics'] = item['appendComment']['pics']
            data_item['appendComment'] = item['appendComment']['content']
        else:
            data_item['appendPics'] = u''
            data_item['appendComment'] = u''
        data_file.write(str(data_item) + '\n')
    print 'out list_elsments'


def saving_data(root_doc, max_page, first_key, typeEncode):
    '''
    一页一页的读网页,编排数据,写入文件,只运行这个

    :param root_doc: 请求内容的简化地址,细节另补
    :param max_page: 取到的最大页数(淘宝最大99页),因为最后一位取不到所以应给100
    :param first_key: 第一对json数据的键,用于删除,以保持json译码的工整
    :param typeEncode: 当前计算机的编码形式
    :return:
    '''
    print 'in saving_data'
    all_url = make_urls(root_doc, min_page, max_page)
    if min_page==1:
        data_file = open('data.txt', 'w')
    else:
        data_file = open('data.txt', 'a')
    for current_url in all_url:
        print 'now saving page: ' + current_url[-2:]
        list_elements(get_json(current_url, first_key, typeEncode), data_file)
        r = random.randint(10, 50)
        print ('--------> sleep(s) : %d' % r)
        time.sleep(r)
    data_file.close()
    print 'out saving_data'


saving_data(root_doc, max_page, first_key, typeEncode)
