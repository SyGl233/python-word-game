# sast2023 word game

## 环境配置

需要可以使用以下python库：

argparse

json

re

random

os

streamlit   *非内部库*

## 使用设置

使用python main-cli.py *命令行参数* 运行cli版本

使用streamlit run main-gui.py 运行gui版本


对cli版本约定以下参数：

```

--file  -f  接文章的路径
--assign  -a  接一个bool值表示是否指定文章标题
--passage  -p  表示指定的文章标题


```

文章使用 JSON 存储，的格式如下：
```
{
    "language":"",
    "articles":[
        {*一篇文章*}
    ]
}
```
一篇文章的格式：
```
"title":"*文章标题*",
"articles":"*正文*{{1}}*正文*{{2}}...",
"hints":["{{1}}的提示","{{2}}的提示"]
```

## 游戏功能

包括CLI和GUI两种版本

支持基础填词功能，题库包含三种语言

可以在完成填词后保存文章，保存路径为./logs/（仅GUI版）

可以自行向根目录添加.json文件，但目前还不支持在GUI中添加新题库或文章