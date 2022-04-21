from pdf2image import convert_from_path
from frappe.utils.file_manager import save_url
import frappe

__version__ = '1.0.0'


def get_file_path(doc):
	base = frappe.get_site_path()

	if doc.is_private:
		return base + doc.file_url
	else:
		return base + '/public' + doc.file_url

def is_pdf(name):
	j =  name.split('.')

	if len(j) > 1:
		return j.pop().lower() == 'pdf'
	else:
		return False

def generate_thumbnail(doc, event=None):

	if not is_pdf(doc.file_name):
		return

	if doc.image:
		return
	
	file_path = get_file_path(doc)
	pages = convert_from_path(file_path)
	if len(pages) >= 1:
		image_path = "{}/public/files/{}_thumbnail.jpeg".format(frappe.get_site_path(), doc.name)
		url_path = "/files/{}_thumbnail.jpeg".format(doc.name)
		pages[0].save(image_path, 'JPEG')
		doc.image = url_path