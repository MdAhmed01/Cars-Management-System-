# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		audit_completed: DF.Check
		brand: DF.Data
		color: DF.Data | None
		condition: DF.Rating
		insurance_expiry: DF.Date | None
		is_published: DF.Check
		license_plate: DF.Data
		model: DF.Data
		name: DF.Int | None
		route: DF.Data | None
		status: DF.Literal["New", "Out of Service", "Sold"]
		title: DF.Data | None
		vehicle_image: DF.AttachImage | None
		year: DF.Int
	# end: auto-generated types

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
