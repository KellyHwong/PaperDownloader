#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Dec-20-20 20:28
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)

"""cvf_paper_downloader
"""
import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from cvf_downloader.conf_url import BASE_URL, CONF_URLS, get_conf_url
from cvf_downloader.downloader import Downloader, _download


def get_download_queue(conf, year, **kwargs):
    conf_url = get_conf_url(conf, year, **kwargs)
    page_html = requests.get(conf_url).content
    page_html = page_html.decode("utf-8")

    # with open(conf+year+".html", "w", encoding="utf-8") as f:
    #     f.write(page_html)

    soup = BeautifulSoup(page_html, "lxml")
    all_pdf_a = soup.find_all("a", text="pdf")
    pdf_href_list = [a["href"] for a in all_pdf_a]

    # print(len(pdf_href_list))  # 783

    # setup download_queue
    download_queue = []
    for i, pdf_href in enumerate(pdf_href_list):
        paper_url = urljoin(BASE_URL, pdf_href)
        print(f"[{i+1}/{len(pdf_href_list)}]Appending paper: {paper_url}.")
        download_queue.append(paper_url)

    return download_queue


def cmd_parser():
    """parse arguments
    """
    parser = argparse.ArgumentParser()

    def string2bool(string):
        """string2bool
        """
        if string not in ["False", "True"]:
            raise argparse.ArgumentTypeError(
                f"""input(={string}) NOT in ["False", "True"]!""")
        if string == "False":
            return False
        elif string == "True":
            return True

    parser.add_argument('--conf', type=str, dest='conf',
                        action='store', default="CVPR", help="""conf, conference name, one of ["CVPR"].""")
    parser.add_argument('--year', type=str, dest='year',
                        action='store', default="2020", help="""year, year of the conference, e.g., 2017, 2018.""")
    parser.add_argument('--day', type=int, dest='day',
                        action='store', default=0, help="""day, day index of the conference, for CVPR2020 as example, one of [0, 1, 2].""")

    # Downloading arguments
    parser.add_argument('--threads', '-t', type=int, dest='threads', action='store', default=4,
                        help='thread count for downloading comic')
    parser.add_argument('--timeout', '-T', type=int, dest='timeout', action='store', default=30,
                        help='timeout for downloading comic')

    args = parser.parse_args()

    return args


def download_conf_test(conf, year, **kwargs):
    """download_conf
    """
    download_queue = get_download_queue(conf, year, **kwargs)

    folder = os.path.join(".", "papers", conf+year)
    if "day" in kwargs:
        day = kwargs.pop("day")
        days = CONF_URLS[conf][year]["days"]
        date_name = days[day]
        folder = os.path.join(folder, date_name)

    # download papers in the queue
    multi_threading = False
    if not multi_threading:
        for i, paper_url in enumerate(download_queue):
            print(f"[{i+1}/{len(download_queue)}]", end="")
            _download(paper_url, folder=folder)
    else:
        downloader = Downloader(thread=args.threads, timeout=args.timeout)
        downloader.download(download_queue, session=None,
                            headers=None, folder=folder)


def tests():
    # download_conf_test(conf="CVPR", year="2017") # pass
    # download_conf_test(conf="CVPR", year="2018", day=0)  # pass
    pass


def main():
    """download_conf
    """
    args = cmd_parser()
    conf = args.conf
    year = args.year
    day = args.day

    download_queue = get_download_queue(conf, year, day=day)

    folder = os.path.join(".", "papers", conf+year)
    if "days" in CONF_URLS[conf][year]:
        days = CONF_URLS[conf][year]["days"]
        date_name = days[day]
        folder = os.path.join(folder, date_name)

    # download papers in the queue
    multi_threading = False
    if not multi_threading:
        for i, paper_url in enumerate(download_queue):
            print(f"[{i+1}/{len(download_queue)}]", end="")
            _download(paper_url, folder=folder)
    else:
        downloader = Downloader(thread=args.threads, timeout=args.timeout)
        downloader.download(download_queue, session=None,
                            headers=None, folder=folder)


if __name__ == "__main__":
    main()
