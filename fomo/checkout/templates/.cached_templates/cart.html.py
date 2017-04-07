# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491530825.195733
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/checkout/templates/cart.html'
_template_uri = 'cart.html'
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
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
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
        __M_writer('\r\n    Cart\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3> Cart Items </h3>\r\n    <p> Below is a table of the current items in your cart</p>\r\n    <a href="/checkout/cart.emptyCart">Empty Cart</a>\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <th>Image</th>\r\n            <th>Name</th>\r\n            <th>Category</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n            <th></th>\r\n        </tr>\r\n')
        for item in request.user.retrieveCart():
            __M_writer('            <tr>\r\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(item.product.graphic))
            __M_writer('" alt=""></td>\r\n                <td><a href="/catalog/detail/')
            __M_writer(str( item.product.id ))
            __M_writer('">')
            __M_writer(str(item.product.name))
            __M_writer('</a></td>\r\n                <td>')
            __M_writer(str(item.product.category.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(item.quantity))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(item.ext_price))
            __M_writer("</td>\r\n                <td><a class='remove_link'  href='/checkout/cart.removeItem/")
            __M_writer(str(item.id))
            __M_writer("'>Remove</a></td>\r\n            </tr>\r\n")
        __M_writer('\r\n    </table>\r\n    <div id="cart-summary">\r\n        <table class="table table-striped">\r\n            <tr>\r\n                <td>Subtotal: </td>\r\n                <td>')
        __M_writer(str(request.user.cartSubtotal()))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Tax:  </td>\r\n                <td>')
        __M_writer(str(request.user.cartTax()))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Shipping: </td>\r\n                <td>')
        __M_writer(str(request.user.cartShipping()))
        __M_writer('</td>\r\n            </tr>\r\n            <tr>\r\n                <td>Total:</td>\r\n                <td>')
        __M_writer(str(request.user.cartTotal()))
        __M_writer('</td>\r\n            </tr>\r\n        </table>\r\n\r\n    </div>\r\n    <div class="text-center">\r\n        <a href="/checkout/shipping" class="btn btn-default">Checkout</a>\r\n    </div>\r\n    <br>\r\n    <p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\n    as well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\n    your needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/checkout/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 19, "49": 74, "55": 17, "61": 17, "67": 21, "75": 21, "76": 34, "77": 35, "78": 36, "79": 36, "80": 36, "81": 36, "82": 37, "83": 37, "84": 37, "85": 37, "86": 38, "87": 38, "88": 39, "89": 39, "90": 40, "91": 40, "92": 41, "93": 41, "94": 44, "95": 50, "96": 50, "97": 54, "98": 54, "99": 58, "100": 58, "101": 62, "102": 62, "108": 102}}
__M_END_METADATA
"""
