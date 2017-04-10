# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491597756.015711
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/catalog/templates/search.html'
_template_uri = 'search.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'body_above', 'body_center']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def body_above():
            return render_body_above(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n    more_menu_items\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_above'):
            context['self'].body_above(**pageargs)
        

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
        __M_writer('\n    Search Results\n')
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


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_center():
            return render_body_center(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!-- <table class="table table-striped">\n    <caption class="text-center"><strong>Search Results</strong></caption>\n    <tr>\n        <th></th>\n        <th>Name</th>\n        <th>Category</th>\n        <th>Price</th>\n        <th></th>\n    </tr>\n')
        for p in products:
            __M_writer('        <tr class="clickable-row" data-href=\'/catalog/detail/')
            __M_writer(str(p.id))
            __M_writer('\'>\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(p.graphic))
            __M_writer('" alt=""></td>\n                <td>')
            __M_writer(str(p.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(p.category.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(p.price))
            __M_writer('</td>\n                <td><a href="/catalog/detail/')
            __M_writer(str( p.id ))
            __M_writer('"class="btn btn-primary">View</a></td>\n        </tr>\n\n')
        __M_writer('</table> -->\n\n<h5 style="border-bottom: solid #dddddd 1px;">Search Results</h5>\n\n<div class="tile-outer">\n')
        for p in products:
            __M_writer('        <div class="tile-container">\n            <div class="tile-image">\n                <a href="/catalog/detail/')
            __M_writer(str( p.id ))
            __M_writer('/"><img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(p.graphic))
            __M_writer('" alt="')
            __M_writer(str( p.name ))
            __M_writer('"></a>\n            </div>\n            <div class="tile-title">\n                <h4>')
            __M_writer(str( p.name ))
            __M_writer('</h4>\n                <h5> <small>$')
            __M_writer(str( p.price ))
            __M_writer('</small></h5>\n                <p>')
            __M_writer(str( p.description ))
            __M_writer('</p>\n            </div>\n        </div>\n')
        __M_writer('</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/catalog/templates/search.html", "uri": "search.html", "source_encoding": "utf-8", "line_map": {"30": 0, "43": 1, "48": 19, "53": 33, "58": 74, "64": 17, "70": 17, "76": 21, "82": 21, "88": 35, "96": 35, "97": 45, "98": 46, "99": 46, "100": 46, "101": 47, "102": 47, "103": 47, "104": 47, "105": 48, "106": 48, "107": 49, "108": 49, "109": 50, "110": 50, "111": 51, "112": 51, "113": 55, "114": 60, "115": 61, "116": 63, "117": 63, "118": 63, "119": 63, "120": 63, "121": 63, "122": 63, "123": 63, "124": 66, "125": 66, "126": 67, "127": 67, "128": 68, "129": 68, "130": 72, "136": 130}}
__M_END_METADATA
"""
