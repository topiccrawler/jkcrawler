# jkcrawler

**2019/10/25 更新：加入微博话题**

**2019/10/24 更新：加入哔哩哔哩相簿**

使用 Scrapy 写成的 JK 爬虫，图片源自哔哩哔哩、Tumblr、Instagram，以及微博、Twitter

## 安装依赖

`pip install -r requirements.txt`

## 启动爬虫

*在 Windows 上需要在 PowerShell 中执行以下命令*

```shell script
scrapy crawl api.vc.bilibili -o data/api.vc.bilibili.jsonlines
scrapy crawl instagram -o data/instagram.jsonlines
scrapy crawl m.weibo -o data/m.weibo.jsonlines
scrapy crawl makooooon.tumblr -o data/makooooon.tumblr.jsonlines
scrapy crawl ryoryo-chan.tumblr -o data/ryoryo-chan.tumblr.jsonlines
```

若要在下一次启动爬虫时恢复工作进度，则需要在命令后面加上 <code>-s JOBDIR=crawls/<var>{spider_name}</var></code>

下载的图片在 `data/full/`，相关信息在 <code>data/<var>{spider_name}</var>.jsonlines</code> 里
