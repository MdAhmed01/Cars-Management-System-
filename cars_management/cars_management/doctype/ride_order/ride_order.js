// Copyright (c) 2026, Ahmed Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride order", {
	refresh(frm) {
        // Add a custom button
 		if (frm.doc.status === "New") {
            frm.add_custom_button("Accept Ride", async () => {
                frm.set_value("status", "Accepted");
                // save the form
                await frm.save();
                
            }, "Action");
            frm.add_custom_button("Reject", async () => {
                frm.set_value("status", "Rejected");
                // save the form
                await frm.save();
                
            }, "Action");
        
        }
    },
    after_save(frm) {
        if (frm.doc.status === "Accepted") {
            frappe.msgprint("Ride Accepted");
        } else if (frm.doc.status === "Rejected") {
            frappe.msgprint("Ride Rejected");
        }
    }
});