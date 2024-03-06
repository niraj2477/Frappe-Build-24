from frappe.desk.doctype.system_console.system_console import SystemConsole
from frappe.utils.safe_exec import read_sql, safe_exec
import frappe
class SystemConsoleOverride(SystemConsole):
	def run(self):

		frappe.only_for("System Console Manager",message=True)
		try:
			frappe.local.debug_log = []
			if self.type == "Python":
				safe_exec(self.console, script_filename="System Console")
				self.output = "\n".join(frappe.debug_log)
			elif self.type == "SQL":
				self.output = frappe.as_json(read_sql(self.console, as_dict=1))
		except Exception:
			self.commit = False
			self.output = frappe.get_traceback()

		if self.commit:
			frappe.db.commit()
		else:
			frappe.db.rollback()
		frappe.get_doc(
			dict(doctype="Console Log", script=self.console, type=self.type, committed=self.commit)
		).insert()
		frappe.db.commit()


@frappe.whitelist()
def show_processlist():
	frappe.only_for("System Console Manager")

	return frappe.db.multisql(
		{
			"postgres": """
			SELECT pid AS "Id",
				query_start AS "Time",
				state AS "State",
				query AS "Info",
				wait_event AS "Progress"
			FROM pg_stat_activity""",
			"mariadb": "show full processlist",
		},
		as_dict=True,
	)