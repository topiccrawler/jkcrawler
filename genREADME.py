import os
from os import path


def genREADME():
    cwd = os.getcwd()
    head = [
        f'# {path.basename(cwd)}',
        '',
        '使用 Scrapy 写成的 JK 爬虫，图片源自哔哩哔哩、Tumblr、Instagram，以及微博、Twitter',
        '',
        '## 安装依赖',
        '',
        '`pip install -r requirements.txt`',
        '',
        '## 启动爬虫',
        '',
        '*在 Windows 上需要在 PowerShell 中执行以下命令*',
        '',
        '```shell script',
    ]

    if os.path.exists('update.md'):
        with open('update.md') as f:
            update = f.read().rstrip()
        head.insert(1, update)
        head.insert(1, '')

    if not path.exists('data/'):
        os.mkdir('data')
    os.system('scrapy list > data/scrapylist.txt')
    with open('data/scrapylist.txt') as f:
        spiders = f.read().splitlines()
    lines = [f'scrapy crawl {spider} -o data/{spider}.jsonlines' for spider in spiders]

    tail = [
        '```',
        '',
        '若要在下一次启动爬虫时恢复工作进度，则需要在命令后面加上 <code>-s JOBDIR=crawls/<var>{spider_name}</var></code>',
        '',
        '下载的图片在 `data/full/`，相关信息在 <code>data/<var>{spider_name}</var>.jsonlines</code> 里',
        '',
    ]

    with open('README.md', 'w') as f:
        f.write('\n'.join(head + lines + tail))


if __name__ == '__main__':
    genREADME()
