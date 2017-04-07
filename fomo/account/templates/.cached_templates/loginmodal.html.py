# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490207465.6205401
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/account/templates/loginmodal.html'
_template_uri = 'loginmodal.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['body_center']


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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3 class="text-center">Log-in to your account</h3>\r\n      <div id=\'login-modal-form\'>\r\n          ')
        __M_writer(str( form ))
        __M_writer('\r\n      </div>\r\n\r\n      <br/>\r\n      <p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\n      as well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\n      your needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/account/templates/loginmodal.html", "uri": "loginmodal.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 29, "47": 17, "54": 17, "55": 21, "56": 21, "62": 56}}
__M_END_METADATA
"""
