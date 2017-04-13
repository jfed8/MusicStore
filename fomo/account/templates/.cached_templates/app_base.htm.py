# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492097457.306289
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['menu_items', 'more_menu_items', 'body_left']


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
        def body_left():
            return render_body_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n\n-->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

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
        __M_writer('\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'index') else ''))
        __M_writer('"><a href="/">Home<span class="sr-only">(current)</span></a></li>\n    <li ><a href="/catalog/">Catalog</a></li>\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'terms') else ''))
        __M_writer('"><a href="/homepage/terms">Terms</a></li>\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'faq') else ''))
        __M_writer('"><a href="/homepage/faq">FAQ</a></li>\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'about') else ''))
        __M_writer('"><a href="/homepage/about">About</a></li>\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'contact') else ''))
        __M_writer('"><a href="/homepage/contact">Contact</a></li>\n')
        if request.user.has_perm('account.manager_menu'):
            __M_writer('        <li ><a href="/manager/products">Manager Portal</a></li>\n')
        __M_writer('\n\n    ')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/account/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"30": 0, "42": 1, "47": 30, "52": 48, "58": 16, "67": 16, "68": 17, "69": 17, "70": 19, "71": 19, "72": 20, "73": 20, "74": 21, "75": 21, "76": 22, "77": 22, "78": 23, "79": 24, "80": 26, "85": 29, "91": 28, "97": 28, "103": 32, "109": 32, "115": 109}}
__M_END_METADATA
"""
