# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492099491.541157
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/checkout/templates/receipt.html'
_template_uri = 'receipt.html'
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
        shippingaddress = context.get('shippingaddress', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        saleitems = context.get('saleitems', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        payment = context.get('payment', UNDEFINED)
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
        __M_writer('\n    Receipt\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        shippingaddress = context.get('shippingaddress', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        saleitems = context.get('saleitems', UNDEFINED)
        payment = context.get('payment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <script src="https://checkout.stripe.com/checkout.js"></script>\n    <h3 style="margin-top:0px;">Order Receipt</h3>\n    <p>Thank you for your order! Your order details and receipt are listed below.</p>\n\n    <table class="table table-striped">\n        <caption>Order</caption>\n        <tr>\n            <th>Order ID</th>\n            <th>Date Stamp</th>\n            <th>Subtotal</th>\n            <th>Tax</th>\n            <th>Shipping</th>\n            <th>Total</th>\n        </tr>\n        <tr>\n            <td>')
        __M_writer(str(sale.id))
        __M_writer('</td>\n            <td>')
        __M_writer(str(sale.date_stamp.date()))
        __M_writer('</td>\n            <td>$')
        __M_writer(str(sale.subtotal))
        __M_writer('</td>\n            <td>$')
        __M_writer(str(sale.tax))
        __M_writer('</td>\n            <td>$')
        __M_writer(str(sale.shipping))
        __M_writer('</td>\n            <td>$')
        __M_writer(str(sale.total))
        __M_writer('</td>\n        </tr>\n    </table>\n    <table class="table table-striped">\n        <caption>Order Items</caption>\n        <tr>\n            <th>Image</th>\n            <th>Name</th>\n            <th>Category</th>\n            <th>Quantity</th>\n            <th>Price</th>\n        </tr>\n')
        for item in saleitems:
            __M_writer('            <tr>\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(item.product.graphic))
            __M_writer('" alt=""></td>\n                <td>')
            __M_writer(str(item.product.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(item.product.category.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(item.quantity))
            __M_writer('</td>\n                <td>$')
            __M_writer(str(item.sale_price))
            __M_writer('</td>\n            </tr>\n')
        __M_writer('    </table>\n\n    <table class="table table-striped">\n        <caption>Payment</caption>\n        <tr>\n            <th>Method</th>\n            <th>Card Brand</th>\n            <th>Card Expiration</th>\n            <th>Amount Payed</th>\n            <th>Amount Refunded</th>\n            <th>Currency</th>\n        </tr>\n        <tr>\n            <td>')
        __M_writer(str(payment.method))
        __M_writer('</td>\n            <td>')
        __M_writer(str(payment.card_brand))
        __M_writer('</td>\n            <td>')
        __M_writer(str(payment.card_expiration))
        __M_writer('</td>\n            <td>$')
        __M_writer(str(payment.amount))
        __M_writer('</td>\n            <td>$')
        __M_writer(str(payment.amount_refunded))
        __M_writer('</td>\n            <td>')
        __M_writer(str(payment.currency))
        __M_writer('</td>\n        </tr>\n    </table>\n\n\n    <div id=\'table_ship_address\'>\n        <table class="table table-striped" style="width:50%;">\n            <caption>Shipping Address</caption>\n            <tr>\n                <td>Full name: </td>\n                <td>')
        __M_writer(str(shippingaddress.fullname))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Address:</td>\n                <td>')
        __M_writer(str(shippingaddress.address))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>City: </td>\n                <td>')
        __M_writer(str(shippingaddress.city))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>State:</td>\n                <td>')
        __M_writer(str(shippingaddress.state))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Zipcode:</td>\n                <td>')
        __M_writer(str(shippingaddress.zipcode))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>Phone:</td>\n                <td>')
        __M_writer(str(shippingaddress.phone))
        __M_writer('</td>\n            </tr>\n        </table>\n\n    </div>\n\n\n\n    <br>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/checkout/templates/receipt.html", "uri": "receipt.html", "source_encoding": "utf-8", "line_map": {"30": 0, "44": 1, "49": 19, "54": 121, "60": 17, "66": 17, "72": 21, "83": 21, "84": 37, "85": 37, "86": 38, "87": 38, "88": 39, "89": 39, "90": 40, "91": 40, "92": 41, "93": 41, "94": 42, "95": 42, "96": 54, "97": 55, "98": 56, "99": 56, "100": 56, "101": 56, "102": 57, "103": 57, "104": 58, "105": 58, "106": 59, "107": 59, "108": 60, "109": 60, "110": 63, "111": 76, "112": 76, "113": 77, "114": 77, "115": 78, "116": 78, "117": 79, "118": 79, "119": 80, "120": 80, "121": 81, "122": 81, "123": 91, "124": 91, "125": 95, "126": 95, "127": 99, "128": 99, "129": 103, "130": 103, "131": 107, "132": 107, "133": 111, "134": 111, "140": 134}}
__M_END_METADATA
"""
