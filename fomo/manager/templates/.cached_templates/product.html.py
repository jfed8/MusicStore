# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1489038799.8164203
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/manager/templates/product.html'
_template_uri = 'product.html'
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
        form = context.get('form', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n\r\n-->\r\n\r\n')
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
        __M_writer('\r\n    Edit Product\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h3>Edit Product</h3>\r\n<p>Please edit the selected product below</p>\r\n')
        __M_writer(str( form ))
        __M_writer("\r\n<p>Our support teams and account management teams provide the best service in the industry. We're passionate about our\r\n    products as well as our employees and it shows in the level of service that we provide. We're always happy to help\r\n    find the solution for your needs. If you are in need of support, reach out to our support team (@fomo_support) on\r\n    the company Slack channel.</p>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/manager/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 19, "48": 29, "54": 17, "60": 17, "66": 21, "73": 21, "74": 24, "75": 24, "81": 75}}
__M_END_METADATA
"""
