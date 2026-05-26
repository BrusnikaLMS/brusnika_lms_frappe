frappe.ui.form.on('Brusnika LMS Settings', {
	refresh(frm) {
		frm.set_intro(
			__('Save your Brusnika.LMS URL, then follow the instructions below to connect from the LMS side.'),
			'blue'
		);
	}
});
