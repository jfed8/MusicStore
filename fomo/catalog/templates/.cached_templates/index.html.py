# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491602098.533356
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'body_above', 'body_left', 'body_center']


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
        categories = context.get('categories', UNDEFINED)
        def body_above():
            return render_body_above(context._locals(__M_locals))
        def body_center():
            return render_body_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_left():
            return render_body_left(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n\n-->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_above'):
            context['self'].body_above(**pageargs)
        

        __M_writer('\n')
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
        __M_writer('\n    Catalog\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_above(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_above():
            return render_body_above(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-lg-4 col-lg-offset-4">\n<form action="/catalog/search/">\n    <div class="input-group">\n        <span class="input-group-btn">\n            <button class="btn btn-default" id="search_submit" type="submit" >Search</button>\n        </span>\n        <input  id="search_box" type="text" class="form-control" name="product_name"  placeholder="Product..." >\n    </div>\n</form>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        categories = context.get('categories', UNDEFINED)
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="panel panel-default">\n      <div class="panel-heading">\n        <h3 class="panel-title">Categories</h3>\n      </div>\n      <div class="panel-body">\n          <ul class="nav nav-stacked panel">\n')
        for c in categories:
            __M_writer('              <li><a href="/catalog/index.filter/')
            __M_writer(str(c.id))
            __M_writer('"> ')
            __M_writer(str( c.name ))
            __M_writer(' </a></li>\n')
        __M_writer('              <li><a href="/catalog/"> Clear Filter </a></li>\n          </ul>\n      </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_center():
            return render_body_center(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="body-outer">\n        <div class="tile-outer">\n')
        for p in products:
            __M_writer('                <div class="tile-container">\n                    <div class="tile-image">\n                        <a href="/catalog/detail/')
            __M_writer(str( p.id ))
            __M_writer('/"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(p.graphic))
            __M_writer('" alt="')
            __M_writer(str( p.name ))
            __M_writer('"></a>\n                    </div>\n                    <div class="tile-title">\n                        <h4>')
            __M_writer(str( p.name ))
            __M_writer('</h4>\n                        <h5> <small>$')
            __M_writer(str( p.price ))
            __M_writer('</small></h5>\n                    </div>\n                </div>\n')
        __M_writer('        </div>\n    </div>\n\n    <br/>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"30": 0, "46": 1, "51": 18, "56": 32, "61": 49, "66": 70, "72": 16, "78": 16, "84": 20, "90": 20, "96": 33, "103": 33, "104": 41, "105": 42, "106": 42, "107": 42, "108": 42, "109": 42, "110": 44, "116": 51, "124": 51, "125": 54, "126": 55, "127": 57, "128": 57, "129": 57, "130": 57, "131": 57, "132": 57, "133": 57, "134": 57, "135": 60, "136": 60, "137": 61, "138": 61, "139": 65, "145": 139}}
__M_END_METADATA
"""
