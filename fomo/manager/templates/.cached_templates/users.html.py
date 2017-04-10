# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491843986.988482
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/manager/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
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
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n    Users\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        request = context.get('request', UNDEFINED)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h3> Users List </h3>\n    <p> Below is a table of the current users</p>\n    <table class="table table-striped">\n        <tr>\n            <th>First Name</th>\n            <th>Last Name</th>\n            <th>Username</th>\n            <th>Email</th>\n            <th>Actions</th>\n        </tr>\n')
        for u in users:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(u.first_name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(u.last_name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(u.username))
            __M_writer('</td>\n\n                <td>')
            __M_writer(str(u.email))
            __M_writer('</td>\n                <td>\n')
            if request.user.has_perm('account.change_fomouser'):
                __M_writer("                        <a href='/manager/manageuser/")
                __M_writer(str(u.id))
                __M_writer("'>Edit</a>\n                        |\n                        <a href='/manager/changeuserpassword/")
                __M_writer(str(u.username))
                __M_writer("'>Change Password</a>\n")
            if request.user.has_perm('account.delete_fomouser'):
                __M_writer("                        |\n                        <a class='delete_link'  href='/manager/manageuser.delete/")
                __M_writer(str(u.id))
                __M_writer("'>Delete</a>\n")
            __M_writer('                </td>\n            </tr>\n\n')
        __M_writer('    </table>\n\n    <!-- Modal -->\n    <div class="modal fade" id="DeleteConfirm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n      <div class="modal-dialog" role="document">\n        <div class="modal-content">\n          <div class="modal-header">\n            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n            <h4 class="modal-title" id="myModalLabel">Confirm</h4>\n          </div>\n          <div class="modal-body">\n            Are you sure you want to delete this user?\n          </div>\n          <div class="modal-footer">\n            <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\n            <a id=\'finalize_delete\' href=\'\' class="btn btn-danger">Yes</a>\n          </div>\n        </div>\n      </div>\n    </div>\n\n\n    <div class="text-center">\n        <a class="btn btn-primary" href="/manager/createuser">Create User</a>\n    </div>\n    <br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/manager/templates/users.html", "uri": "users.html", "source_encoding": "utf-8", "line_map": {"19": 1, "32": 0, "43": 1, "44": 2, "49": 20, "54": 80, "60": 18, "66": 18, "72": 22, "80": 22, "81": 33, "82": 34, "83": 35, "84": 35, "85": 36, "86": 36, "87": 37, "88": 37, "89": 39, "90": 39, "91": 41, "92": 42, "93": 42, "94": 42, "95": 44, "96": 44, "97": 46, "98": 47, "99": 48, "100": 48, "101": 50, "102": 54, "108": 102}}
__M_END_METADATA
"""
