# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491530831.013398
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/checkout/templates/checkout.html'
_template_uri = 'checkout.html'
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
        cart_subtotal = context.get('cart_subtotal', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_total = context.get('cart_total', UNDEFINED)
        cart_shipping = context.get('cart_shipping', UNDEFINED)
        ship_address = context.get('ship_address', UNDEFINED)
        form = context.get('form', UNDEFINED)
        cart_tax = context.get('cart_tax', UNDEFINED)
        usercart = context.get('usercart', UNDEFINED)
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
        __M_writer('\r\n    Checkout\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart_subtotal = context.get('cart_subtotal', UNDEFINED)
        def body_center():
            return render_body_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_total = context.get('cart_total', UNDEFINED)
        cart_shipping = context.get('cart_shipping', UNDEFINED)
        ship_address = context.get('ship_address', UNDEFINED)
        form = context.get('form', UNDEFINED)
        cart_tax = context.get('cart_tax', UNDEFINED)
        usercart = context.get('usercart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <script src="https://checkout.stripe.com/checkout.js"></script>\r\n    <h3> Order Confirmation</h3>\r\n    <p>Please confirm your order details before processing.</p>\r\n\r\n    <table class="table table-striped">\r\n        <caption>Order Items</caption>\r\n        <tr>\r\n            <th>Image</th>\r\n            <th>Name</th>\r\n            <th>Category</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n        </tr>\r\n')
        for item in usercart:
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
            __M_writer(str(item.ext_price))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n\r\n    <div id="cart-summary">\r\n        <table class="table table-striped">\r\n            <caption>Order Summary</caption>\r\n            <tr>\r\n                <td>Subtotal: </td>\r\n                <td>')
        __M_writer(str(cart_subtotal))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Tax:  </td>\r\n                <td>')
        __M_writer(str(cart_tax))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Shipping: </td>\r\n                <td>')
        __M_writer(str(cart_shipping))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Total:</td>\r\n                <td id="cart_total" temp=\'')
        __M_writer(str(cart_total))
        __M_writer("'>")
        __M_writer(str(cart_total))
        __M_writer('</td>\r\n            </tr>\r\n        </table>\r\n\r\n\r\n    </div>\r\n    \r\n    <div id=\'table_ship_address\'>\r\n        <table class="table table-striped">\r\n            <caption>Shipping Address </caption>\r\n            <tr>\r\n                <td>Full name: </td>\r\n                <td>')
        __M_writer(str(ship_address.fullname))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Address:</td>\r\n                <td>')
        __M_writer(str(ship_address.address))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>City: </td>\r\n                <td>')
        __M_writer(str(ship_address.city))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>State:</td>\r\n                <td>')
        __M_writer(str(ship_address.state))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Zipcode:</td>\r\n                <td>')
        __M_writer(str(ship_address.zipcode))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Phone:</td>\r\n                <td>')
        __M_writer(str(ship_address.phone))
        __M_writer('</td>\r\n            </tr>\r\n        </table>\r\n        <a href="/checkout/shipping_edit/')
        __M_writer(str(ship_address.id))
        __M_writer('"class="btn btn-default">Edit</a>\r\n\r\n    </div>\r\n\r\n    ')
        __M_writer(str(form))
        __M_writer('\r\n\r\n    <br>\r\n\r\n    <p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\n    as well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\n    your needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/checkout/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"28": 0, "45": 1, "50": 19, "55": 109, "61": 17, "67": 17, "73": 21, "87": 21, "88": 35, "89": 36, "90": 37, "91": 37, "92": 37, "93": 37, "94": 38, "95": 38, "96": 39, "97": 39, "98": 40, "99": 40, "100": 41, "101": 41, "102": 44, "103": 51, "104": 51, "105": 55, "106": 55, "107": 59, "108": 59, "109": 63, "110": 63, "111": 63, "112": 63, "113": 75, "114": 75, "115": 79, "116": 79, "117": 83, "118": 83, "119": 87, "120": 87, "121": 91, "122": 91, "123": 95, "124": 95, "125": 98, "126": 98, "127": 102, "128": 102, "134": 128}}
__M_END_METADATA
"""
