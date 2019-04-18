import fecfile
from . import fec2xlsx


def file_number_xlsx(file_number, filename):
    items = fecfile.iter_http(file_number)
    fec2xlsx.make_xlsx(items, filename)


def file_location_xlsx(file_path, filename):
    items = fecfile.iter_file(file_path)
    fec2xlsx.make_xlsx(items, filename)
