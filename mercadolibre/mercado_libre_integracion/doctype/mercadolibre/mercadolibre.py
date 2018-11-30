# -*- coding: utf-8 -*-
# Copyright (c) 2018, fredyteheranto and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
import json

from frappe.model.document import Document

class mercadolibre(Document):
	req = requests.get('https://github.com/timeline.json')
	req.json()
