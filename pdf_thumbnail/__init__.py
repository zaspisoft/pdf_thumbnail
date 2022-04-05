from pdf2image import convert_from_path
from frappe.utils.file_manager import save_url

__version__ = '1.0.0'


def get_file_path(doc):
	base = frappe.get_site_path()

	if doc.is_private:
		return base + doc.file_url
	else:
		return base + '/public' + doc.file_url


def generate_thumbnail(doc, event=None):
	file_path = get_file_path(doc)
	pages = convert_from_path(file_path, 500)
	if len(pages) >= 1:
		image_path = "{}/{}_thumbnail.jpeg".fromat(frappe.get_site_path(), doc.name)
		pages[0].save(image_path, 'JPEG')
		frappe.db.set_value('File', doc.name, 'image', image_path)
		frappe.db.commit()


