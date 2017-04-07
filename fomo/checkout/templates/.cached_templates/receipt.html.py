# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491530861.5165806
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/checkout/templates/receipt.html'
_template_uri = 'receipt.html'
_source_encoding = 'utf-8'
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
        saleitems = context.get('saleitems', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        payment = context.get('payment', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        sale = context.get('sale', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        shippingaddress = context.get('shippingaddress', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    Receipt\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        saleitems = context.get('saleitems', UNDEFINED)
        def body_center():
            return render_body_center(context)
        payment = context.get('payment', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        shippingaddress = context.get('shippingaddress', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <script src="https://checkout.stripe.com/checkout.js"></script>\r\n    <h3> Order Receipt</h3>\r\n    <p>Thank you for your order! Your order details and receipt are listed below.</p>\r\n\r\n    <table class="table table-striped">\r\n        <caption>Order</caption>\r\n        <tr>\r\n            <th>Order ID</th>\r\n            <th>Date Stamp</th>\r\n            <th>Subtotal</th>\r\n            <th>Tax</th>\r\n            <th>Shipping</th>\r\n            <th>Total</th>\r\n        </tr>\r\n        <tr>\r\n            <td>')
        __M_writer(str(sale.id))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(sale.date_stamp))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(sale.subtotal))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(sale.tax))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(sale.shipping))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(sale.total))
        __M_writer('</td>\r\n        </tr>\r\n    </table>\r\n    <table class="table table-striped">\r\n        <caption>Order Items</caption>\r\n        <tr>\r\n            <th>Image</th>\r\n            <th>Name</th>\r\n            <th>Category</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n        </tr>\r\n')
        for item in saleitems:
            __M_writer('            <tr>\r\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(item.product.graphic))
            __M_writer('" alt=""></td>\r\n                <td>')
            __M_writer(str(item.product.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(item.product.category.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(item.quantity))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(item.sale_price))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n\r\n    <table class="table table-striped">\r\n        <caption>Payment</caption>\r\n        <tr>\r\n            <th>Method</th>\r\n            <th>Card Brand</th>\r\n            <th>Card Expiration</th>\r\n            <th>Amount Payed</th>\r\n            <th>Amount Refunded</th>\r\n            <th>Currency</th>\r\n        </tr>\r\n        <tr>\r\n            <td>')
        __M_writer(str(payment.method))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(payment.card_brand))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(payment.card_expiration))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(payment.amount))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(payment.amount_refunded))
        __M_writer('</td>\r\n            <td>')
        __M_writer(str(payment.currency))
        __M_writer('</td>\r\n        </tr>\r\n    </table>\r\n\r\n\r\n    <div id=\'table_ship_address\'>\r\n        <table class="table table-striped">\r\n            <caption>Shipping Address</caption>\r\n            <tr>\r\n                <td>Full name: </td>\r\n                <td>')
        __M_writer(str(shippingaddress.fullname))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Address:</td>\r\n                <td>')
        __M_writer(str(shippingaddress.address))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>City: </td>\r\n                <td>')
        __M_writer(str(shippingaddress.city))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>State:</td>\r\n                <td>')
        __M_writer(str(shippingaddress.state))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Zipcode:</td>\r\n                <td>')
        __M_writer(str(shippingaddress.zipcode))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Phone:</td>\r\n                <td>')
        __M_writer(str(shippingaddress.phone))
        __M_writer('</td>\r\n            </tr>\r\n        </table>\r\n\r\n    </div>\r\n\r\n\r\n\r\n    <br>\r\n\r\n    <p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\n    as well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\n    your needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/checkout/templates/receipt.html", "uri": "receipt.html", "source_encoding": "utf-8", "line_map": {"28": 0, "42": 1, "47": 19, "52": 124, "58": 17, "64": 17, "70": 21, "81": 21, "82": 37, "83": 37, "84": 38, "85": 38, "86": 39, "87": 39, "88": 40, "89": 40, "90": 41, "91": 41, "92": 42, "93": 42, "94": 54, "95": 55, "96": 56, "97": 56, "98": 56, "99": 56, "100": 57, "101": 57, "102": 58, "103": 58, "104": 59, "105": 59, "106": 60, "107": 60, "108": 63, "109": 76, "110": 76, "111": 77, "112": 77, "113": 78, "114": 78, "115": 79, "116": 79, "117": 80, "118": 80, "119": 81, "120": 81, "121": 91, "122": 91, "123": 95, "124": 95, "125": 99, "126": 99, "127": 103, "128": 103, "129": 107, "130": 107, "131": 111, "132": 111, "138": 132}}
__M_END_METADATA
"""
