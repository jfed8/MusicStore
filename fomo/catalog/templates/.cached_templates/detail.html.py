# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492098054.406819
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/catalog/templates/detail.html'
_template_uri = 'detail.html'
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
        product = context.get('product', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        __M_writer('\n    Product Detail\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def body_center():
            return render_body_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="tile-image">\n        <a id="detail-modal-button" ><img temp="')
        __M_writer(str( product.id ))
        __M_writer('" id="prod_graph" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('catalog/media/prod_imgs/')
        __M_writer(str(product.graphic))
        __M_writer('" alt="')
        __M_writer(str( product.name ))
        __M_writer('"></a>\n        <div class="tile-title">\n            <h5> <small>Click image to see more</small></h5>\n        </div>\n    </div>\n    <h2>')
        __M_writer(str( product.name ))
        __M_writer('</h2>\n\n')
        if hasattr(product, 'monthly_price'):
            __M_writer('                <h3 class="detail-h3">Type: Rental</h3>\n                <h3 class="detail-h3">Monthly Price: $')
            __M_writer(str( product.monthly_price ))
            __M_writer('</h3>\n')
        else:
            __M_writer('                <h3 class="detail-h3">Type: For Sale</h3>\n                <h3 class="detail-h3">Price: $')
            __M_writer(str( product.price ))
            __M_writer('</h3>\n')
        __M_writer('\n            <h3 class="detail-h3">Category: ')
        __M_writer(str( product.category ))
        __M_writer('</h3>\n            <h3 class="detail-h3">\n')
        if hasattr(product, 'quantity') and product.quantity > 0:
            __M_writer('                    <h3 style="color:red;" class="detail-h3">Available: ')
            __M_writer(str(product.quantity))
            __M_writer('</h3>\n')
        __M_writer('            </h3>\n            <h3 class="detail-h3" id="purchase_container">')
        __M_writer(str( form ))
        __M_writer('</h3>\n\n            <!-- <div id="purchase_container" class="detail-h3">\n')
        if hasattr(product, 'quantity') and product.quantity > 0:
            __M_writer('                    <h3 style="color:red;" class="detail-h3">In Stock</h3>\n')
        __M_writer('            </div> -->\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/catalog/templates/detail.html", "uri": "detail.html", "source_encoding": "utf-8", "line_map": {"30": 0, "43": 1, "48": 19, "53": 55, "59": 17, "65": 17, "71": 22, "81": 22, "82": 24, "83": 24, "84": 24, "85": 24, "86": 24, "87": 24, "88": 24, "89": 24, "90": 29, "91": 29, "92": 31, "93": 32, "94": 33, "95": 33, "96": 34, "97": 35, "98": 36, "99": 36, "100": 38, "101": 39, "102": 39, "103": 41, "104": 42, "105": 42, "106": 42, "107": 44, "108": 45, "109": 45, "110": 48, "111": 49, "112": 51, "118": 112}}
__M_END_METADATA
"""
