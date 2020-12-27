#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Dec-20-20 20:28
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)

"""cvf_paper_downloader
"""
import os
import requests
from bs4 import BeautifulSoup
from utils.dir_utils import makedir_exist_ok

conf_urls = {
    "CVPR2017": "https://openaccess.thecvf.com/CVPR2017",
    "CVPR2018": {
        "prefix": "https://openaccess.thecvf.com/CVPR2018",
        "days": [
            "2018-06-19",
            "2018-06-20",
            "2018-06-21"
        ]
    },
    "CVPR2019": "https://openaccess.thecvf.com/CVPR2019",
    "CVPR2020": "https://openaccess.thecvf.com/CVPR2020"
}


def get_conf_url(conf, **kwargs):
    """
    docstring
    """
    if "day_index" in kwargs:
        day_index = kwargs["day_index"]

    if conf == "CVPR2017":
        conf_url = conf_urls[conf]
    else:
        prefix = conf_urls[conf]
        day = conf_urls[conf][day_index]

    return conf_url


def _download(url, headers="", folder="", filename="", retried=0):
    """_download
    # Arguments:
        url:
    """
    from urllib.parse import urlparse
    filename = filename if filename else os.path.basename((urlparse(url).path))

    if not os.path.isdir(folder):
        makedir_exist_ok(folder)
    filepath = os.path.join(folder, filename)

    data = requests.get(url).content
    with open(filepath, "wb") as f:
        f.write(data)
    print(f"Downloaded to {filepath}.")


def download(conf):
    conf_url = get_conf_url(conf)
    page_html = requests.get(conf_url).content
    page_html = page_html.decode("utf-8")
    with open("CVPR2017.html", "w", encoding="utf-8") as f:
        f.write(page_html)

    soup = BeautifulSoup(page_html, "lxml")
    all_pdf_a = soup.find_all("a", text="pdf")
    pdf_href_list = [a["href"] for a in all_pdf_a]

    # print(len(pdf_href_list))  # 783

    # download papers in the list
    host_root = "https://openaccess.thecvf.com/"
    from urllib.parse import urljoin
    for pdf_href in pdf_href_list:
        pdf_href = urljoin(host_root, pdf_href)
        print(pdf_href)
        _download(pdf_href, folder=os.path.join(".", "papers", conf))


def main():
    download(conf="CVPR2017")


if __name__ == "__main__":
    main()
