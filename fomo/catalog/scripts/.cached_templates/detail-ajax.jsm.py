# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491530981.3030865
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/catalog/scripts/detail-ajax.jsm'
_template_uri = 'detail-ajax.jsm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('$(function() {\r\n    console.log(\'Hello ajax\');\r\n    $("#cart-count").html("')
        __M_writer(str(request.user.get_cart_count()))
        __M_writer('");\r\n\r\n    //Ajax Form\r\n    var options = {\r\n        target:     \'#purchase_container\',     //target element(s) to be update with server response\r\n    };//options\r\n\r\n    $(\'#formlib-purchaseform\').ajaxForm(options);//Ajax Form\r\n});//ready\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/catalog/scripts/detail-ajax.jsm", "uri": "detail-ajax.jsm", "source_encoding": "utf-8", "line_map": {"17": 0, "23": 1, "24": 3, "25": 3, "31": 25}}
__M_END_METADATA
"""
