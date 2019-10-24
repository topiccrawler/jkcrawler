# jkcrawler

使用 Scrapy 写成的 JK 爬虫，图片源自哔哩哔哩、Tumblr、Instagram，以及微博、Twitter (待完成)

启动爬虫：

在 Windows 上，需要在 PowerShell 中执行以下命令

```shell script
scrapy crawl api.vc.bilibili -o data/api.vc.bilibili.jsonlines
scrapy crawl instagram -o data/instagram.jsonlines
scrapy crawl makooooon.tumblr -o data/makooooon.tumblr.jsonlines
scrapy crawl ryoryo-chan.tumblr -o data/ryoryo-chan.tumblr.jsonlines
scrapy crawl sscat-xyz.tumblr -o data/sscat-xyz.tumblr.jsonlines
```

若要在下一次启动爬虫时恢复工作进度，则需要在命令后面加上 `-s JOBDIR=crawls/{spider_name}`
