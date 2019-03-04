# ttrpy

[![Build Status](https://travis-ci.com/joelowj/ttrpy.svg?token=zM8uDnAP2GXz8Hagm4hw&branch=master)](https://travis-ci.com/joelowj/ttrpy) [![codecov](https://codecov.io/gh/joelowj/ttrpy/branch/master/graph/badge.svg)](https://codecov.io/gh/joelowj/ttrpy)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

Technical Trading Rule Python is an open source library for popular technical analysis function for financial time series data.

## Installation

To install the current release:

```
$ pip install ttrpy
```

## Usage Overview

Load historical stock data into `Pandas` from existing csv file or directly from the web.
```python
>>> import pandas as pd
>>> df = pd.read_csv("weekly_MSFT.csv").sort_values(by="timestamp").reset_index(drop=True)
>>> df.tail(3)
```

```
      timestamp    open    high     low   close   volume
1098 2019-01-25  106.75   107.88    ...    ...     ...
1099 2019-02-01  106.26   106.48    ...    ...     ...
1100 2019-02-07  102.87   107.27    ...    ...     ...
```

Let's say we are interested in the overall long-term trend for `MSFT`, we can use the simple moving average function from the trend package.

```python
>>> from ttrpy.trend.sma import sma
>>> df = sma(df, "close", "sma", 200)
>>> df.tail(3)
```

```
      timestamp    open    high     low   close   volume    sma
1098 2019-01-25  106.75   107.88    ...    ...     ...    71.080175
1099 2019-02-01  106.26   106.48    ...    ...     ...    71.392625
1100 2019-02-07  102.87   107.27    ...    ...     ...    71.707025
```

As easy as that!

## Contribution Guidelines

**If you want to contribute to ttrpy, be sure to review the [contribution
guidelines](CONTRIBUTING.md). This project adheres to ttrpy's
[code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.**

To get the local repository set up for development,

```
$ pip install pipenv
$ pip install --dev
```

If you find a bug, kindly open an issue [here](https://github.com/joelowj/ttrpy/issues/new).

If you would like to request a new feature, feel free to do so by opening an issue [here](https://github.com/joelowj/ttrpy/issues/new).

To fix a bug or enhance an existing module, follow these steps:
- Fork the repository
- Create a new branch (`git checkout - b branch-name`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -m 'commit message'`)
- Push to the branch (`git push origin branch-name`)
- Create a Pull Request

## Versioning
We use [SemVer](https://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/joelowj/ttrpy/tags)

## License
This project is licensed under Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
