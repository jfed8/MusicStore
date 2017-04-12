# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492029426.730216
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/account/templates/myaccount.html'
_template_uri = 'myaccount.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'body_left', 'body_center']


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
        def body_left():
            return render_body_left(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n\n-->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

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
        __M_writer('\n    My Account\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="panel panel-default">\n      <div class="panel-heading">\n        <h3 class="panel-title">Actions</h3>\n      </div>\n      <div class="panel-body">\n          <ul class="nav nav-stacked panel">\n              <li><a href="/account/changepassword">Change Password</a></li>\n              <li><a href="/account/changeself">Edit Information</a></li>\n              <li><a href="/account/orderhistory">Order History</a></li>\n          </ul>\n      </div>\n    </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h3 style="margin-top:0px;">My Account</h3>\n    <table class="table table-striped">\n        <tr>\n            <td>First Name:</td>\n            <td>')
        __M_writer(str( user.first_name ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Last Name:</td>\n            <td>')
        __M_writer(str( user.last_name ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Email: </td>\n            <td>')
        __M_writer(str( user.email ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Address: </td>\n            <td>')
        __M_writer(str( user.address ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>City: </td>\n            <td>')
        __M_writer(str( user.city ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>State: </td>\n            <td>')
        __M_writer(str( user.state ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Zipcode: </td>\n            <td>')
        __M_writer(str( user.zipcode ))
        __M_writer('</td>\n        </tr>\n        <tr>\n            <td>Phone: </td>\n            <td>')
        __M_writer(str( user.phone ))
        __M_writer('</td>\n        </tr>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/account/templates/myaccount.html", "uri": "myaccount.html", "source_encoding": "utf-8", "line_map": {"30": 0, "42": 1, "47": 18, "52": 36, "57": 74, "63": 16, "69": 16, "75": 20, "81": 20, "87": 38, "94": 38, "95": 43, "96": 43, "97": 47, "98": 47, "99": 51, "100": 51, "101": 55, "102": 55, "103": 59, "104": 59, "105": 63, "106": 63, "107": 67, "108": 67, "109": 71, "110": 71, "116": 110}}
__M_END_METADATA
"""
