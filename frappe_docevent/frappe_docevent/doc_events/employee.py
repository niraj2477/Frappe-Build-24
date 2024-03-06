
def before_insert(doc,method=None):
    from frappe.utils import add_years
    doc.custom_appraisal_date = add_years(doc.date_of_joining, 1)