
def on_submit(doc, method):
    import frappe
    from frappe.utils import add_years, today
    cycle= frappe.get_doc("Appraisal Cycle",doc.appraisal_cycle)
    employee = frappe.get_doc("Employee",doc.employee)

    if cycle.start_date < employee.custom_appraisal_date < cycle.end_date:
        employee.custom_appraisal_date = add_years(today(),1)
        employee.save()