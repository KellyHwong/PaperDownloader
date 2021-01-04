# PaperDownloader

PaperDownloader, paper downloading helper for CVF[1] conference papers.

## Usage

Firstly install this package and cd:

```bash
python setup.py install --user
cd ./cvf_downloader
```

Start downloading the papers :-)

Download all the CVPR2017 papers into `./papers/CVPR2017` folder.

```Python
python main.py --conf=CVPR --year=2017
```

For CVPR2018+, day argument must be provided, day should be one of 0 ,1, 2.

Download all the first day of CVPR2018 papers into `./papers/CVPR2018/2018-06-19` folder.

```Python
python main.py --conf=CVPR --year=2018, --day=0
```

Let's try latest CVPR2020 papers, download all the first day of CVPR2020 papers into `./papers/CVPR2018/2020-06-16` folder.

```Python
python main.py --conf=CVPR --year=2020, --day=0
```

## References

[1]. Computer Vision Foundation open access, [https://openaccess.thecvf.com/menu](https://openaccess.thecvf.com/menu)
