# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Vehicle(Document):
	def before_save(self):
		self.title=f"{self.brand} {self.model} {self.year}"
		

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		brand: DF.Data
		color: DF.Data | None
		license_plate: DF.Data
		model: DF.Data
		name: DF.Int | None
		title: DF.Data
		year: DF.Int
	# end: auto-generated types

	# end: auto-generated types

	_DOCTYPE_NAME = "Vehicle"
