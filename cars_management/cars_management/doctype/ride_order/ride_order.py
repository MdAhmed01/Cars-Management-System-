# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Rideorder(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.SmallText
		contact_number: DF.Data
		customer_name: DF.Data
		date_time: DF.Datetime | None
		status: DF.Literal["New", "Accepted", "Rejected"]
		vehicle: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Ride order"
