# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Drivers(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name or ''}"

	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		driver_photo: DF.AttachImage | None
		enabled: DF.Check
		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data | None
		license_number: DF.Data
		phone_number: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "Drivers"
