# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491592113.4333
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['menu_items', 'more_menu_items']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def more_menu_items():
            return render_more_menu_items(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n    more_menu_items\n-->\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def more_menu_items():
            return render_more_menu_items(context)
        request = context.get('request', UNDEFINED)
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n    <li ><a href="/">Home<span class="sr-only">(current)</span></a></li>\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'index') else ''))
        __M_writer('"><a href="/catalog/">Catalog</a></li>\n    <li ><a href="/homepage/terms">Terms</a></li>\n    <li ><a href="/homepage/faq">FAQ</a></li>\n    <li ><a href="/homepage/about">About</a></li>\n    <li ><a href="/homepage/contact">Contact</a></li>\n')
        if request.user.has_perm('account.manager_menu'):
            __M_writer('        <li ><a href="/manager/products">Manager Portal</a></li>\n')
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'more_menu_items'):
            context['self'].more_menu_items(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_more_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def more_menu_items():
            return render_more_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"30": 0, "40": 1, "45": 31, "51": 18, "60": 18, "61": 20, "62": 20, "63": 25, "64": 26, "65": 28, "70": 30, "76": 29, "82": 29, "88": 82}}
__M_END_METADATA
"""
