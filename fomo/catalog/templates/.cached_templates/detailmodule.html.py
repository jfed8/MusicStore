# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491842982.1199338
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/catalog/templates/detailmodule.html'
_template_uri = 'detailmodule.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['body_center']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        pictures = context.get('pictures', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        pictures = context.get('pictures', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="center-selector">\n')
        for pic in pictures:
            __M_writer('        <img class="product_picture_modal" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str(pic.path))
            __M_writer('" alt="')
            __M_writer(str(pic.product.name))
            __M_writer('">\n')
        __M_writer('    </div>\n\n    <div class="center-selector">\n        <button id="btn_previous" class="btn btn-default">Previous</button>\n        <button id="btn_next" class="btn btn-default">Next</button>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/catalog/templates/detailmodule.html", "uri": "detailmodule.html", "source_encoding": "utf-8", "line_map": {"30": 0, "39": 1, "44": 16, "50": 3, "58": 3, "59": 6, "60": 7, "61": 7, "62": 7, "63": 7, "64": 7, "65": 7, "66": 9, "72": 66}}
__M_END_METADATA
"""
