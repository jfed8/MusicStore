# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491530979.2682567
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/catalog/templates/detail.html'
_template_uri = 'detail.html'
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
        product = context.get('product', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
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
        __M_writer('\r\n    Product Detail\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        def body_center():
            return render_body_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="text-center">\r\n        <h1>')
        __M_writer(str(product.name))
        __M_writer("</h1>\r\n        <img temp='")
        __M_writer(str( product.id ))
        __M_writer('\' id="prod_graph" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('catalog/media/prod_imgs/')
        __M_writer(str(product.graphic))
        __M_writer('" alt="')
        __M_writer(str(product.name))
        __M_writer('">\r\n        </br>\r\n        <br>\r\n        <div class="panel panel-default">\r\n        <!-- Default panel contents -->\r\n        <div class="panel-heading">Product Details</div>\r\n\r\n        <!-- Table -->\r\n        <table class="table">\r\n            <tr>\r\n                <th>Price</th>\r\n                <th>Category</th>\r\n')
        if hasattr(product, 'condition'):
            __M_writer('                    <th>Condition</th>\r\n')
        if hasattr(product, 'quantity'):
            __M_writer('                    <th>Quantity</th>\r\n')
        __M_writer('            </tr>\r\n            <tr>\r\n                <td class="text-left">')
        __M_writer(str( product.price ))
        __M_writer('</td>\r\n                <td class="text-left">')
        __M_writer(str( product.category.name))
        __M_writer(' </td>\r\n')
        if hasattr(product, 'condition'):
            __M_writer('                    <td class="text-left">')
            __M_writer(str(product.condition))
            __M_writer('</td>\r\n')
        if hasattr(product, 'quantity'):
            __M_writer('                    <td class="text-left">')
            __M_writer(str(product.quantity))
            __M_writer('</td>\r\n')
        __M_writer('            </tr>\r\n        </table>\r\n        </div>\r\n\r\n            <div id=\'purchase_container\' class="text-center">\r\n                 ')
        __M_writer(str(form))
        __M_writer('\r\n            </div>\r\n\r\n\r\n    </div>\r\n\r\n    <p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\n    as well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\n    your needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/catalog/templates/detail.html", "uri": "detail.html", "source_encoding": "utf-8", "line_map": {"28": 0, "41": 1, "46": 19, "51": 67, "57": 17, "63": 17, "69": 22, "79": 22, "80": 24, "81": 24, "82": 25, "83": 25, "84": 25, "85": 25, "86": 25, "87": 25, "88": 25, "89": 25, "90": 37, "91": 38, "92": 40, "93": 41, "94": 43, "95": 45, "96": 45, "97": 46, "98": 46, "99": 47, "100": 48, "101": 48, "102": 48, "103": 50, "104": 51, "105": 51, "106": 51, "107": 53, "108": 58, "109": 58, "115": 109}}
__M_END_METADATA
"""
