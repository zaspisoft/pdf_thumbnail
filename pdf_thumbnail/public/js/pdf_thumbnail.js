function is_pdf(name) {
	const dirs =   name.split('.')
	if(dirs.length > 1){
		return dirs.pop().toLowerCase() == 'pdf'
	}	
	
	return false
}

frappe.ui.form.on("File", {
	refresh: (frm) => {
		if (!is_pdf(frm.doc.file_name)) {
			frm.fields_dict.pdf_preview.wrapper[0].style.display = 'none'
		}else { 1 
			frm.fields_dict.pdf_preview.wrapper[0].style.display = 'block'
		}
	}
})