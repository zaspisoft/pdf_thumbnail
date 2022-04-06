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


def generate_thumbnail(doc, event=None):

	if not doc.file_name.endswith('pdf'):
		return
	
	file_path = get_file_path(doc)
	pages = convert_from_path(file_path, 500)
	if len(pages) >= 1:
		image_path = "{}/public/files/{}_thumbnail.jpeg".format(frappe.get_site_path(), doc.name)
		url_path = "/files/{}_thumbnail.jpeg".format(doc.name)
		pages[0].save(image_path, 'JPEG')
		frappe.db.set_value('File', doc.name, 'image', url_path)
		frappe.db.commit()


