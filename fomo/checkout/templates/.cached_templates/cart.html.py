# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492099028.893079
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/checkout/templates/cart.html'
_template_uri = 'cart.html'
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
        request = context.get('request', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n    more_menu_items\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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
        __M_writer('\n    Cart\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def body_center():
            return render_body_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h3 style="margin-top:0px;"> Cart Items |<a style="font-size:15px;" href="/checkout/cart.emptyCart">&nbsp;Empty Cart</a></h3>\n    <p> Below is a table of the current items in your cart</p>\n    <table class="table table-striped">\n        <tr>\n            <th>Image</th>\n            <th>Name</th>\n            <th>Category</th>\n            <th>Quantity</th>\n            <th>Price</th>\n            <th></th>\n        </tr>\n')
        for item in request.user.retrieveCart():
            __M_writer('            <tr>\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(item.product.graphic))
            __M_writer('" alt=""></td>\n                <td><a href="/catalog/detail/')
            __M_writer(str( item.product.id ))
            __M_writer('">')
            __M_writer(str(item.product.name))
            __M_writer('</a></td>\n                <td>')
            __M_writer(str(item.product.category.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(item.quantity))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(item.ext_price))
            __M_writer("</td>\n                <td><a class='remove_link'  href='/checkout/cart.removeItem/")
            __M_writer(str(item.id))
            __M_writer("'>Remove</a></td>\n            </tr>\n")
        __M_writer('\n    </table>\n    <div id="cart-summary">\n        <table class="table">\n            <tr>\n                <th>Subtotal:</th>\n                <th>$')
        __M_writer(str(request.user.cartSubtotal()))
        __M_writer('</th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n                <th></th>\n            </tr>\n            <tr>\n                <th>Tax:  </th>\n                <th>$')
        __M_writer(str(request.user.cartTax()))
        __M_writer('</th>\n            </tr>\n            <tr>\n                <th>Shipping: </th>\n                <th>$')
        __M_writer(str(request.user.cartShipping()))
        __M_writer('</th>\n            </tr>\n            <tr>\n                <th>Total:</th>\n                <th>$')
        __M_writer(str(request.user.cartTotal()))
        __M_writer('</th>\n            </tr>\n        </table>\n\n    </div>\n    <div class="text-center">\n        <a href="/checkout/shipping" class="btn btn-primary">Checkout</a>\n    </div>\n    <br>\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/checkout/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"30": 0, "41": 1, "46": 19, "51": 87, "57": 17, "63": 17, "69": 21, "77": 21, "78": 33, "79": 34, "80": 35, "81": 35, "82": 35, "83": 35, "84": 36, "85": 36, "86": 36, "87": 36, "88": 37, "89": 37, "90": 38, "91": 38, "92": 39, "93": 39, "94": 40, "95": 40, "96": 43, "97": 49, "98": 49, "99": 69, "100": 69, "101": 73, "102": 73, "103": 77, "104": 77, "110": 104}}
__M_END_METADATA
"""
