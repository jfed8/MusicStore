# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490631179.1505978
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/account/templates/myaccount.html'
_template_uri = 'myaccount.html'
_source_encoding = 'utf-8'
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
        def body_left():
            return render_body_left(context._locals(__M_locals))
        def body_center():
            return render_body_center(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n\r\n-->\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

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
        __M_writer('\r\n    My Account\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <a class="btn btn-default" href="/account/changepassword">Change Password</a>\r\n        </tr>\r\n        <tr>\r\n            <a class="btn btn-default" href="/account/changeself">Edit Information</a>\r\n        </tr>\r\n    </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3>My Account</h3>\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <td>First Name:</td>\r\n            <td>')
        __M_writer(str( user.first_name ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>Last Name:</td>\r\n            <td>')
        __M_writer(str( user.last_name ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>Email: </td>\r\n            <td>')
        __M_writer(str( user.email ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>Address: </td>\r\n            <td>')
        __M_writer(str( user.address ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>City: </td>\r\n            <td>')
        __M_writer(str( user.city ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>State: </td>\r\n            <td>')
        __M_writer(str( user.state ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>Zipcode: </td>\r\n            <td>')
        __M_writer(str( user.zipcode ))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>Phone: </td>\r\n            <td>')
        __M_writer(str( user.phone ))
        __M_writer('</td>\r\n        </tr>\r\n    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/account/templates/myaccount.html", "uri": "myaccount.html", "source_encoding": "utf-8", "line_map": {"28": 0, "40": 1, "45": 18, "50": 30, "55": 68, "61": 16, "67": 16, "73": 20, "79": 20, "85": 32, "92": 32, "93": 37, "94": 37, "95": 41, "96": 41, "97": 45, "98": 45, "99": 49, "100": 49, "101": 53, "102": 53, "103": 57, "104": 57, "105": 61, "106": 61, "107": 65, "108": 65, "114": 108}}
__M_END_METADATA
"""
