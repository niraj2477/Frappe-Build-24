
def after_app_install(name):
    import frappe
    role=frappe.get_doc({
        'doctype': 'Role',
        'role_name': 'System Console Manager'
    }).insert(ignore_permissions=True,ignore_if_duplicate=True)

    frappe.get_doc({
        'doctype': 'Custom DocPerm',
        'role': role.role_name,
        'parent':'System Console',
        'read': 1,
        'write': 1,
        'create': 1,
        'delete': 1,
    }).insert(ignore_permissions=True,ignore_if_duplicate=True)
    frappe.get_doc({
        'doctype': 'Custom DocPerm',
        'role': role.role_name,
        'parent':'Console Log',
        'read': 1,
        'write': 1,
        'create': 1,
        'delete': 1,
    }).insert(ignore_permissions=True,ignore_if_duplicate=True)
