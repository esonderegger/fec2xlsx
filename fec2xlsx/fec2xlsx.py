import xlsxwriter
import datetime


def make_xlsx(fec_iterable, filename, options={}):
    filter_memo_x = options.get('filter_memo_x', True)
    workbook, formats = init_xslx_file(filename, options)
    sheets = {
        'Summary': {
            'sheet': workbook.add_worksheet('Summary'),
            'headers': None,
            'row': 1,
        }
    }
    for item in fec_iterable:
        if item.data_type == 'summary':
            sheets['Summary']['headers'] = write_column_headers(
                sheets['Summary']['sheet'],
                formats,
                item.data.keys()
            )
            write_row(
                sheets['Summary']['sheet'],
                formats,
                item.data,
                sheets['Summary']['headers'],
                sheets['Summary']['row'],
            )
        if item.data_type == 'itemization':
            if filter_memo_x and 'memo_code' in item.data:
                if item.data['memo_code'] == 'X':
                    continue
            form_type = item.data['form_type']
            if form_type[0] == 'S':
                form_type = 'Schedule ' + item.data['form_type'][1]
            if form_type not in sheets:
                sheets[form_type] = {
                    'sheet': workbook.add_worksheet(form_type),
                    'headers': None,
                    'row': 1,
                }
                sheets[form_type]['headers'] = write_column_headers(
                    sheets[form_type]['sheet'],
                    formats,
                    item.data.keys()
                )
                sheets[form_type]['sheet'].freeze_panes(1, 0)
            write_row(
                sheets[form_type]['sheet'],
                formats,
                item.data,
                sheets[form_type]['headers'],
                sheets[form_type]['row'],
            )
            sheets[form_type]['row'] += 1
    workbook.close()


def init_xslx_file(filename, options):
    money_format = options.get('money_format', '$#,##0.00')
    date_format = options.get('date_format', 'd mmm yyyy')
    workbook = xlsxwriter.Workbook(filename)
    formats = {}
    formats['money'] = workbook.add_format({'num_format': money_format})
    formats['date'] = workbook.add_format({'num_format': date_format})
    formats['header'] = workbook.add_format(
        {'bold': True, 'bottom': 2, 'bottom_color': '#DADFE8'})
    formats['bold'] = workbook.add_format({'bold': True})
    return workbook, formats


def write_column_headers(worksheet, formats, columns):
    headers = list(columns)
    for i in range(len(headers)):
        worksheet.write(0, i, headers[i], formats['header'])
        worksheet.set_column(i, i, len(headers[i]))
    return headers


def write_row(worksheet, formats, data, headers, row_num):
    for i in range(len(headers)):
        column = headers[i]
        data_item = data[column]
        if data_item is None:
            continue
        if isinstance(data_item, float):
            worksheet.write_number(
                row_num,
                i,
                float(data_item),
                formats['money'],
            )
        elif isinstance(data_item, datetime.datetime):
            worksheet.write_datetime(
                row_num,
                i,
                data_item.replace(tzinfo=None),
                formats['date'],
            )
        else:
            worksheet.write_string(row_num, i, str(data_item))
