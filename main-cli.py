import argparse
import json
import re
import random


def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    # TODO: 添加更多参数
    parser.add_argument("-a", "--assign", help="是否指定文章", required=True)
    parser.add_argument("-p", "--passage", help="文章标题（如果需要指定文章）")
    
    args = parser.parse_args()
    return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
        data=json.load(f)
    
    return data



def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        # TODO: 读取一个用户输入并且存储到 keys 当中
        keys.append(input())

    return keys


def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换
        article = re.sub("\{\{"+str(i+1)+"\}\}",keys[i],article)

    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]

    # TODO: 根据参数或随机从 articles 中选择一篇文章
    # TODO: 给出合适的输出，提示用户输入
    # TODO: 获取用户输入并进行替换
    # TODO: 给出结果

    

    article = ""
    hints = []
    title = ""
    if(eval(args.assign)):
        #print(233)
        assert args.passage is not None, "指定文章时文章标题不能为空"
        title = args.passage
        for p in articles:
            if(p["title"]==title):
                article = p["article"]
                hints = p["hints"]
                break
    else:
        index = random.randint(0,len(articles)-1)
        #print(index)
        article = articles[index]["article"]
        hints = articles[index]["hints"]
        title = articles[index]["title"]


    #print(hints)
    #print(article)

    keys = get_inputs(hints)
    article = replace(article,keys)
    print("\n你写出的怪文：")
    print(article)


    


