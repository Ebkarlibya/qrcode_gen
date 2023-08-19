import frappe
import pyqrcode
from io import BytesIO
import base64
from barcode.writer import ImageWriter
from barcode import generate




@frappe.whitelist()
def gen_qrcode(text: str):
    data = pyqrcode.create(text)

    return f'data:image/png;base64,{data.png_as_base64_str(scale=8)}'

@frappe.whitelist(allow_guest=True)
def gen_barcode(text: str, barcode_type: str = 'CODE128'):
    fp = BytesIO()
    generate(barcode_type, text, writer=ImageWriter(), output=fp)

    res = fp.getvalue()
    b64 = base64.b64encode(res)

    return f'data:image/png;base64,{b64.decode(errors="replace")}'


