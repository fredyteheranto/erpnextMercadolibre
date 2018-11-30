# -*- coding: utf-8 -*-
# Copyright (c) 2018, fredyteheranto and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
import json
import sys
from frappe import _
from frappe.model.document import Document

class mercadolibre(Document):

    def main():
        #meli = Meli(client_id="2748831568094",client_secret="1WAQdOfGf6ThKYqS9FyAnfRnKDPI3b9T", access_token="APP_USR-2748831568094-113012-0a31e41bc274af4303f3e7984732490c-192107249", refresh_token="TG-5c016389af115f0006aaf521-192107249")
        #response = meli.get("/items/ITEM_ID")
        #print(sys.path.append)
        #frappe.errprint("your message")
        #
        frappe.msgprint('fredy desde erpnext integrando mercadolibre')
    main()