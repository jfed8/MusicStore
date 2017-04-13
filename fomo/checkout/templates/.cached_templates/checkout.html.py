# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492099417.731389
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/checkout/templates/checkout.html'
_template_uri = 'checkout.html'
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
        usercart = context.get('usercart', UNDEFINED)
        cart_subtotal = context.get('cart_subtotal', UNDEFINED)
        cart_shipping = context.get('cart_shipping', UNDEFINED)
        ship_address = context.get('ship_address', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_tax = context.get('cart_tax', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        cart_total = context.get('cart_total', UNDEFINED)
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
        __M_writer('\n    Checkout\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        usercart = context.get('usercart', UNDEFINED)
        cart_subtotal = context.get('cart_subtotal', UNDEFINED)
        cart_shipping = context.get('cart_shipping', UNDEFINED)
        ship_address = context.get('ship_address', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def body_center():
            return render_body_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_tax = context.get('cart_tax', UNDEFINED)
        cart_total = context.get('cart_total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <script src="https://checkout.stripe.com/checkout.js"></script>\n    <h3 style="margin-top:0px;">Review Order</h3>\n    <p>Please confirm your order details before paying.</p>\n\n    <table class="table table-striped">\n        <caption>Order Items</caption>\n        <tr>\n            <th>Image</th>\n            <th>Name</th>\n            <th>Category</th>\n            <th>Quantity</th>\n            <th>Price</th>\n        </tr>\n')
        for item in usercart:
            __M_writer('            <tr>\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(item.product.graphic))
            __M_writer('" alt=""></td>\n                <td>')
            __M_writer(str(item.product.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(item.product.category.name))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(item.quantity))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(item.ext_price))
            __M_writer('</td>\n            </tr>\n')
        __M_writer('    </table>\n\n    <div id="cart-summary">\n        <table class="table table-striped" style="width:50%;">\n            <caption>Order Summary</caption>\n            <tr>\n                <td>Subtotal: </td>\n                <td>$')
        __M_writer(str(cart_subtotal))
        __M_writer('</td>\n\n            </tr>\n            <tr>\n                <td>Tax:  </td>\n                <td>$')
        __M_writer(str(cart_tax))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Shipping: </td>\n                <td>$')
        __M_writer(str(cart_shipping))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Total:</td>\n                <td id="cart_total" temp=\'')
        __M_writer(str(cart_total))
        __M_writer("'>$")
        __M_writer(str(cart_total))
        __M_writer('</td>\n            </tr>\n        </table>\n\n\n    </div>\n\n    <div id=\'table_ship_address\'>\n        <table class="table table-striped" style="width:50%;">\n            <caption>Shipping Address </caption>\n            <tr>\n                <td>Full name: </td>\n                <td>')
        __M_writer(str(ship_address.fullname))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Address:</td>\n                <td>')
        __M_writer(str(ship_address.address))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>City: </td>\n                <td>')
        __M_writer(str(ship_address.city))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>State:</td>\n                <td>')
        __M_writer(str(ship_address.state))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Zipcode:</td>\n                <td>')
        __M_writer(str(ship_address.zipcode))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Phone:</td>\n                <td>')
        __M_writer(str(ship_address.phone))
        __M_writer('</td>\n            </tr>\n        </table>\n        <a href="/checkout/shipping_edit/')
        __M_writer(str(ship_address.id))
        __M_writer('"class="btn btn-default">Edit</a>\n\n    </div>\n\n    ')
        __M_writer(str(form))
        __M_writer('\n\n    <br>\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/checkout/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"30": 0, "47": 1, "52": 19, "57": 107, "63": 17, "69": 17, "75": 21, "89": 21, "90": 35, "91": 36, "92": 37, "93": 37, "94": 37, "95": 37, "96": 38, "97": 38, "98": 39, "99": 39, "100": 40, "101": 40, "102": 41, "103": 41, "104": 44, "105": 51, "106": 51, "107": 56, "108": 56, "109": 60, "110": 60, "111": 64, "112": 64, "113": 64, "114": 64, "115": 76, "116": 76, "117": 80, "118": 80, "119": 84, "120": 84, "121": 88, "122": 88, "123": 92, "124": 92, "125": 96, "126": 96, "127": 99, "128": 99, "129": 103, "130": 103, "136": 130}}
__M_END_METADATA
"""
