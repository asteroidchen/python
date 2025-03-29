import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

# ================= 配置区域 =================
TARGET_URL = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1526269427171_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8"  # 替换为合法图片源地址（如Unsplash/Pexels等）
SAVE_DIR = '../../../爬虫图片'  # 图片保存路径
MAX_WORKERS = 5  # 并发下载线程数
TIMEOUT = 10  # 请求超时时间（秒）


# ============================================

def create_directory():
    """创建保存目录"""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"目录已创建：{SAVE_DIR}")


def get_image_urls(url):
    """解析页面获取图片URL"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')
        img_tags = soup.find_all('img')

        img_urls = []
        for img in img_tags:
            src = img.get('src') or img.get('data-src')
            if src and src.startswith(('http', '//')):
                img_url = urljoin(url, src)
                img_urls.append(img_url)
        return list(set(img_urls))  # 去重
    except Exception as e:
        print(f"解析失败：{e}")
        return []


def download_image(img_url):
    """下载单张图片"""
    try:
        filename = os.path.join(SAVE_DIR, img_url.split("/")[-1].split("?")[0])
        if os.path.exists(filename):
            print(f"已存在：{filename}")
            return

        response = requests.get(img_url, stream=True, timeout=TIMEOUT)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"下载成功：{filename}")
    except Exception as e:
        print(f"下载失败 {img_url}: {e}")


if __name__ == "__main__":
    # 法律声明
    print("=" * 60)
    print("请确保：")
    print("1. 目标网站允许爬取图片（检查robots.txt）")
    print("2. 图片不涉及版权问题")
    print("3. 不用于商业用途（除非获得授权）")
    print("=" * 60)

    create_directory()
    img_urls = get_image_urls(TARGET_URL)

    if img_urls:
        print(f"发现 {len(img_urls)} 张图片，开始下载...")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            executor.map(download_image, img_urls)
        print("下载任务完成！")
    else:
        print("未找到有效图片链接")
