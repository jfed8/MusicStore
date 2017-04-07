# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1489884962.98806
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/catalog/templates/detailmodal.html'
_template_uri = 'detailmodal.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        pictures = context.get('pictures', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_center():
            return render_body_center(context)
        pictures = context.get('pictures', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for pic in pictures:
            __M_writer('        <img class="product_picture" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str(pic.path))
            __M_writer('" alt="')
            __M_writer(str(pic.product.name))
            __M_writer('">\r\n')
        __M_writer('    <button id="btn_previous" class="btn btn-default">Previous</button>\r\n    <button id="btn_next" class="btn btn-default">Next</button>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/catalog/templates/detailmodal.html", "uri": "detailmodal.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 11, "48": 3, "56": 3, "57": 5, "58": 6, "59": 6, "60": 6, "61": 6, "62": 6, "63": 6, "64": 8, "70": 64}}
__M_END_METADATA
"""
