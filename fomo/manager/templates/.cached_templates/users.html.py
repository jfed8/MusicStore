# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490749489.2429693
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/manager/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'body_center']


from catalog import models as cmod 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def body_center():
            return render_body_center(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    Users\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        users = context.get('users', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3> Users List </h3>\r\n    <p> Below is a table of the current users</p>\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <th>First Name</th>\r\n            <th>Last Name</th>\r\n            <th>Username</th>\r\n            <th>Email</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for u in users:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str(u.first_name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(u.last_name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(u.username))
            __M_writer('</td>\r\n\r\n                <td>')
            __M_writer(str(u.email))
            __M_writer('</td>\r\n                <td>\r\n')
            if request.user.has_perm('account.change_fomouser'):
                __M_writer("                        <a href='/manager/manageuser/")
                __M_writer(str(u.id))
                __M_writer("'>Edit</a>\r\n                        |\r\n                        <a href='/manager/changeuserpassword/")
                __M_writer(str(u.username))
                __M_writer("'>Change Password</a>\r\n")
            if request.user.has_perm('account.delete_fomouser'):
                __M_writer("                        |\r\n                        <a class='delete_link'  href='/manager/manageuser.delete/")
                __M_writer(str(u.id))
                __M_writer("'>Delete</a>\r\n")
            __M_writer('                </td>\r\n            </tr>\r\n\r\n')
        __M_writer('    </table>\r\n\r\n    <!-- Modal -->\r\n    <div class="modal fade" id="DeleteConfirm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n      <div class="modal-dialog" role="document">\r\n        <div class="modal-content">\r\n          <div class="modal-header">\r\n            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n            <h4 class="modal-title" id="myModalLabel">Confirm</h4>\r\n          </div>\r\n          <div class="modal-body">\r\n            Are you sure you want to delete this user?\r\n          </div>\r\n          <div class="modal-footer">\r\n            <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n            <a id=\'finalize_delete\' href=\'\' class="btn btn-danger">Yes</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n\r\n    <div class="text-center">\r\n        <a class="btn btn-default" href="/manager/createuser">Create User</a>\r\n    </div>\r\n    <br>\r\n    <p>Our support teams and account management teams provide the best service in the industry. We\'re passionate about our\r\n        products as well as our employees and it shows in the level of service that we provide. We\'re always happy to help\r\n        find the solution for your needs. If you are in need of support, reach out to our support team (@fomo_support) on\r\n        the company Slack channel.</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/manager/templates/users.html", "uri": "users.html", "source_encoding": "utf-8", "line_map": {"17": 1, "30": 0, "41": 1, "42": 2, "47": 20, "52": 84, "58": 18, "64": 18, "70": 22, "78": 22, "79": 33, "80": 34, "81": 35, "82": 35, "83": 36, "84": 36, "85": 37, "86": 37, "87": 39, "88": 39, "89": 41, "90": 42, "91": 42, "92": 42, "93": 44, "94": 44, "95": 46, "96": 47, "97": 48, "98": 48, "99": 50, "100": 54, "106": 100}}
__M_END_METADATA
"""
