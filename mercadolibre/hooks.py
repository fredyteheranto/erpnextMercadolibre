# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mercadolibre"
app_title = "Mercado Libre Integracion"
app_publisher = "fredyteheranto"
app_description = "Mercado Libre Integracion demo lanch"
app_icon = "fa fa-cart-plus"
app_color = "#007eff"
app_email = "fredyteheran91@gmail.com"
app_license = "GNU General Public License"
app_url = "http://fredyteheranto.com"


fixtures = ["Custom Field"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#app_include_css = "/assets/mercadolibre/css/mercadolibre.css"
# app_include_js = "/assets/mercadolibre/js/mercadolibre.js"

# include js, css files in header of web template
# web_include_css = "/assets/mercadolibre/css/mercadolibre.css"
# web_include_js = "/assets/mercadolibre/js/mercadolibre.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mercadolibre.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mercadolibre.install.before_install"
# after_install = "mercadolibre.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mercadolibre.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mercadolibre.tasks.all"
# 	],
# 	"daily": [
# 		"mercadolibre.tasks.daily"
# 	],
# 	"hourly": [
# 		"mercadolibre.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mercadolibre.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mercadolibre.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mercadolibre.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mercadolibre.event.get_events"
# }

