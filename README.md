# fec2xlsx
A python library for making Excel files from FEC filings

Microsoft Excel can be a powerful tool for analyzing FEC filings. This library (hopefully) makes it easy to create multi-sheet Excel files from files in the .fec file format, with a sheet for the summary data and a sheet for each type of itemization.

## Usage

Note: this library works best with version 3.7+ of Python due to the ordering of dictionary keys being [guaranteed](https://docs.python.org/3.7/library/stdtypes.html#typesmapping) to be in insertion order. The library should still work in older version of Python, but the columns on each sheet might be in a nonsensical order.

First, install from PyPi:

```
pip install fec2xlsx
```

Then, call one of the two methods for generating Excel files:

```
import fec2xlsx

fec2xlsx.file_number_xlsx(1326061, 'Gillibrand_Q1.xlsx')

fec2xlsx.file_location_xlsx('/path/to/1326016.fec', 'Harris_Q1.xlsx')
```

The `file_number_xlsx` method requests the specified `file_number` via http from the FEC's server's, first trying the URL for digital filings, then trying the URL for paper filings if the first response returns a 404 status code.

The `file_location_xlsx` method reads from the specified `file_path` (which takes anything you might pass to Python's [open](https://docs.python.org/3/library/functions.html#open) method) then writes to the specified `filename` output.

Both methods take an optional `options` keyword argument.

## Options

- `filter_memo_x`: (default: `True`) if True, ignores rows that have "X" as their `memo_code`. If, for example, a contribution comes in through a conduit committee like ActBlue, there are two rows: one for the contribution from an individual to the conduit and one from the conduit to the committee filing the report. Generally the second of those rows is marked with an "X" in the `memo_code` field and is the less useful of the two.

- `money_format`: (default: `$#,##0.00`) The format used for displaying monetary values. See [here](https://xlsxwriter.readthedocs.io/format.html#set_num_format) for more details/documentation.

- `date_format`: (default: `d mmm yyyy`) The format used for displaying date values. See [here](https://xlsxwriter.readthedocs.io/working_with_dates_and_time.html) for more details/documentation.
