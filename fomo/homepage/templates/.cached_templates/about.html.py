# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492099843.234731
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'body_center']


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
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n    more_menu_items\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n')
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
        __M_writer('\n    About\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\n<h1 style="margin-top:0px;">About Us</h1>\n<div class="container-fluid">\n<div class="row">\n    <h3>Our Mission:</h3>\n    <p>To become your family\'s favorite music store</p>\n    <h3>Our Story</h3>\n    <p>Visit any FOMO Music Store at any time and you’re guaranteed to see somebody making music. After all, making music is what we\'re all about.\n    Playing the incredible selection of instruments is not only allowed, it’s encouraged. You’ll find people of all ages, from novice to\n    pros playing trumpets, saxaphones, and other instruments. The huge inventory of musical instruments and accessories, sound and recording\n    equipment, sheet music and videos, computers and music software covers every musician’s needs no matter what his or her playing style or ability may be.</p>\n    <p>FOMO is currently a local rental store with locations throughout the state of Utah. Our current size doesn\'t prevent us from having big dreams.\n        We will one day become the world\'s favorite music store.</p>\n    <p>Come in and see us today!</p>\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"30": 0, "39": 1, "44": 19, "49": 38, "55": 17, "61": 17, "67": 22, "73": 22, "79": 73}}
__M_END_METADATA
"""
