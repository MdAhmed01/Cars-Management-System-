# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		total_distance=0
		for item in self.items:
			total_distance += item.distance
		self.total_amount= total_distance * self.rate
	


	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from cars_management.cars_management.doctype.ride_booking_item.ride_booking_item import RideBookingItem
		from frappe.types import DF

		amended_from: DF.Link | None
		driver: DF.Link
		items: DF.Table[RideBookingItem]
		order: DF.Link
		rate: DF.Currency
		total_amount: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Order Ride"
