app_name = "frappe_docoverride"
app_title = "Frappe Docoverride"
app_publisher = "Niraj"
app_description = "Doc Override"
app_email = "nirajgautam196@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_docoverride/css/frappe_docoverride.css"
# app_include_js = "/assets/frappe_docoverride/js/frappe_docoverride.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_docoverride/css/frappe_docoverride.css"
# web_include_js = "/assets/frappe_docoverride/js/frappe_docoverride.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappe_docoverride/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "frappe_docoverride/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "frappe_docoverride.utils.jinja_methods",
# 	"filters": "frappe_docoverride.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_docoverride.install.before_install"
# after_install = "frappe_docoverride.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_docoverride.uninstall.before_uninstall"
# after_uninstall = "frappe_docoverride.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "frappe_docoverride.utils.before_app_install"
after_app_install = "frappe_docoverride.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "frappe_docoverride.utils.before_app_uninstall"
# after_app_uninstall = "frappe_docoverride.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_docoverride.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"System Console": "frappe_docoverride.overrides.system_console.SystemConsoleOverride"
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_docoverride.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_docoverride.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_docoverride.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_docoverride.tasks.weekly"
# 	],
# 	"monthly": [
# 		"frappe_docoverride.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "frappe_docoverride.install.before_tests"

# Overriding Methods
# ------------------------------
#

#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_docoverride.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["frappe_docoverride.utils.before_request"]
# after_request = ["frappe_docoverride.utils.after_request"]

# Job Events
# ----------
# before_job = ["frappe_docoverride.utils.before_job"]
# after_job = ["frappe_docoverride.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"frappe_docoverride.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

override_whitelisted_methods = {
	"frappe.desk.doctype.system_console.system_console.show_processlist": "frappe_docoverride.overrides.system_console.show_processlist"
}