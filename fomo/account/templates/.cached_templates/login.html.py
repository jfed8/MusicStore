# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492028298.9204748
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/account/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'body_right', 'body_center']


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
        def body_right():
            return render_body_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def body_center():
            return render_body_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_right'):
            context['self'].body_right(**pageargs)
        

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
        __M_writer('\n    Login\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_right():
            return render_body_right(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3 class="text-center">Log-in to your account</h3>\n\n\n\n      ')
        __M_writer(str( form ))
        __M_writer('\n\n      <br/>\n    </div>\n    <p>Don\'t have an account? <a href="/account/signup/">Sign-up now!</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/account/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"30": 0, "42": 1, "47": 19, "52": 22, "57": 35, "63": 17, "69": 17, "75": 21, "81": 21, "87": 24, "94": 24, "95": 30, "96": 30, "102": 96}}
__M_END_METADATA
"""
