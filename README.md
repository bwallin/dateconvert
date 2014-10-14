[![Build Status](https://travis-ci.org/kpurdon/dateconvert.svg)](https://travis-ci.org/kpurdon/dateconvert)


[![PyPi Version](http://img.shields.io/pypi/v/dateconvert.svg)](http://img.shields.io/pypi/v/dateconvert.svg)


[![GitHub Version](http://img.shields.io/github/tag/kpurdon/dateconvert.svg)](http://img.shields.io/github/tag/kpurdon/dateconvert.svg)

Python DATECONVERT
====

#Summary

This is a python distribution which contains command-line (CLI) utilities for conversion of date formats.

# Included Conversions:
YYYYMMDD -> Day-Of-Year

# Installation

This tool is hosted on PyPi (Python Package Index) and can be installed using pip:

```pip install dateconvert```


# Use

When the tool is installed using pip all of the CLI functions are automatically available.

From the command line run:

```day_of_year -p 20110101```

# Development

The source is hosted on [GitHub](https://github.com/kpurdon/dateconvert). To develop on this source clone the repository and complete the following:

1. Install fabric ```pip install fabric```
2. CD into the project directory
3. Run the setup task ```fab setup_env```
4. Run the tests ```fab test```
5. Develop!

To submit changes please make a pull request. Any pull requests without passing tests will be rejected.
