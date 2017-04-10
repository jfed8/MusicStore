# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491840443.299367
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/catalog/scripts/detail-ajax.jsm'
_template_uri = 'detail-ajax.jsm'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('$(function() {\n    console.log(\'Hello ajax\');\n    $("#cart_count").html("')
        __M_writer(str(request.user.get_cart_count()))
        __M_writer('");\n\n    //Ajax Form\n    var options = {\n        target:     \'#purchase_container\',     //target element(s) to be update with server response\n    };//options\n\n    $(\'#formlib-purchaseform\').ajaxForm(options);//Ajax Form\n});//ready\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/catalog/scripts/detail-ajax.jsm", "uri": "detail-ajax.jsm", "source_encoding": "utf-8", "line_map": {"19": 0, "25": 1, "26": 3, "27": 3, "33": 27}}
__M_END_METADATA
"""
