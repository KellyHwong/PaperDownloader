#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jan-04-21 02:35
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)

from urllib.parse import urljoin

BASE_URL = "https://openaccess.thecvf.com"
CONF_URLS = {
    "CVPR": {
        "2017": {
            "base": "CVPR2017"
        },
        "2018": {
            "base": "CVPR2018",
            "days": [
                "2018-06-19",
                "2018-06-20",
                "2018-06-21"
            ]
        },
        "2019": {
            "base": "CVPR2019",
            "days": [
                "2019-06-18",
                "2019-06-19",
                "2019-06-20"
            ]
        },
        "2020": {
            "base": "CVPR2020",
            "days": [
                "2020-06-16",
                "2020-06-17",
                "2020-06-18"
            ]
        }
    }
}


def get_conf_url(conf, year, **kwargs):
    """get_conf_url
    """
    day = None
    if "day" in kwargs:
        day = kwargs.pop("day")

    if conf not in CONF_URLS:
        raise ValueError(f"{conf} (conf) not in CONF_URLS: {CONF_URLS.keys()}")

    conf_url_dict = CONF_URLS[conf][year]
    conf_base_url = conf_url_dict["base"]

    if int(year) <= 2017:
        return urljoin(BASE_URL, conf_base_url)
    else:
        # day must be provided and in [0, 1, 2]
        if day is None:
            raise ValueError("day must be provided!")
        if day not in [0, 1, 2]:
            raise ValueError(
                f"{day} (day) not in [0, 1, 2].")

        days = conf_url_dict["days"]

        return urljoin(BASE_URL, f"{conf_base_url}?day={days[day]}")


def main():
    """test"""
    print(get_conf_url("CVPR", "2017"))
    # print(get_conf_url("CVPR", "2018"))
    print(get_conf_url("CVPR", "2018", day=0))


if __name__ == "__main__":
    main()
