# Tagger CLI

Run the following command for default functionality.

```python tag.py```

Choose a file -- it will be enumerated 0 to X.

There's also a spot edit feature.

```python tag.py edit```

A clear all feature.

```python tag.py clear```

And a check to ensure the tag groups are correct.

```python tag.py check```

### News Sources

| News Agency | User ID |
|---|---|
| Fox News | 15704546335 |
| Fox News Insider | 149658925128808 |
| CNN | 5550296508 |
| CNBC | 97212224368 |

### Current Stories

| Topic | News Agency | ID |
|---|---|---|
| *Net Neutrality Repeal* |||
|| CNN | 5550296508_10157614223046509 |
|| Fox News | 15704546335_10156316052531336 |
| *Trump 3rd Quarter Salary Donation* |||
|| Fox News Insider | 149658925128808_1600412916720061 |
|| CNBC | 97212224368_10156206718254369 |

### Example queries

- [CNBC article](https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=15704546335_10156308025161336%2Fcomments%3Forder%3Dchronological%26limit%3D10000&version=v2.11)
- [Fox News Insider video](https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=149658925128808_1600412916720061%2Fcomments%3Forder%3Dchronological%26limit%3D10000&version=v2.11)
