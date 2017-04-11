# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491589392.9240131
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['page_title', 'title', 'body_above', 'body_left', 'body_right']


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
        def body_above():
            return render_body_above(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_right():
            return render_body_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_above'):
            context['self'].body_above(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_right'):
            context['self'].body_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('FOMO Home Page')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_above(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_above():
            return render_body_above(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- <ol class="breadcrumb" style="margin-bottom:0px;">\n      <li class="breadcrumb-item active">Home</li>\n    </ol> -->\n    <div class="img-wrapper">\n        <div class="cover" title="Family Oriented Music Organization">\n        </div>\n        <div class="img-overlay">\n            <a href="/catalog/" class="btn btn-md btn-default">Shop Now</a>\n            <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/FOMOLogo-02.png" alt="Family Oriented Music Organization">\n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_right():
            return render_body_right(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"30": 0, "46": 1, "51": 3, "56": 4, "61": 18, "66": 22, "71": 27, "77": 3, "83": 3, "89": 4, "95": 4, "101": 5, "108": 5, "109": 14, "110": 14, "116": 20, "122": 20, "128": 25, "134": 25, "140": 134}}
__M_END_METADATA
"""
