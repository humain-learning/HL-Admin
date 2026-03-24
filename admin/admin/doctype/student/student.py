# Copyright (c) 2026, Raghav Kaul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Student(Document):
	def before_validate(self):
		self.fullname = self.first_name + " " + self.last_name

	def validate(self):
		pass
