frappe.ui.form.on("File", {
	refresh: (frm) => {
		if (!frm.doc.file_name.endsWith('.pdf')) {
			frm.fields_dict.pdf_preview.wrapper[0].style.display = 'none'
		}else {
			frm.fields_dict.pdf_preview.wrapper[0].style.display = 'block'
		}
	}
})