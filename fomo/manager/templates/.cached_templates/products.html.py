# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492096958.9789581
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/manager/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'body_center']


from catalog import models as cmod 

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
        hasattr = context.get('hasattr', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n\n-->\n\n')
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
        __M_writer('\n    Products\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        request = context.get('request', UNDEFINED)
        products = context.get('products', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h3> Products List </h3>\n    <p> Below is a table of the current inventory</p>\n    <table class="table table-striped">\n        <tr>\n            <th>Category</th>\n            <th>Name</th>\n            <th>Price</th>\n            <th>Quantity</th>\n            <th>Serial Number</th>\n            <th>Barcode</th>\n            <th>Action</th>\n        </tr>\n')
        for p in products:
            __M_writer('            <tr>\n                <td>')
            __M_writer(str(p.category.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(p.name))
            __M_writer('</td>\n                <td>')
            __M_writer(str(p.price))
            __M_writer('</td>\n                <td>\n                    <!-- possible solution  % if isinstance(p, cmod.BulkProduct): but have to import catalog.models-->\n')
            if hasattr(p, 'quantity'): ##<!--This is duck typing-->
                __M_writer('                        <span class="quantity_text">')
                __M_writer(str(p.quantity))
                __M_writer('</span>\n')
            else:
                __M_writer('                        -\n')
            __M_writer('                </td>\n                <td>\n')
            if hasattr(p, 'serial_number'): ##<!--This is duck typing-->
                __M_writer('                        ')
                __M_writer(str(p.serial_number))
                __M_writer('\n')
            else:
                __M_writer('                        -\n')
            __M_writer('                </td>\n                <td>\n')
            if hasattr(p, 'barcode'): ##<!--This is duck typing-->
                __M_writer('                        ')
                __M_writer(str(p.barcode))
                __M_writer('\n')
            else:
                __M_writer('                        -\n')
            __M_writer('                </td>\n                <td>\n')
            if request.user.has_perm('catalog.change_product'):
                __M_writer("                        <a href='/manager/product/")
                __M_writer(str(p.id))
                __M_writer("'>Edit</a>\n")
            if request.user.has_perm('account.delete_product'):
                __M_writer("                        |\n                        <a class='delete_link'  href='/manager/product.delete/")
                __M_writer(str(p.id))
                __M_writer("'>Delete</a>\n")
            __M_writer('                </td>\n            </tr>\n\n')
        __M_writer('    </table>\n\n    <!-- Modal -->\n    <div class="modal fade" id="DeleteConfirm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n      <div class="modal-dialog" role="document">\n        <div class="modal-content">\n          <div class="modal-header">\n            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n            <h4 class="modal-title" id="myModalLabel">Confirm</h4>\n          </div>\n          <div class="modal-body">\n            Are you sure you want to delete this product?\n          </div>\n          <div class="modal-footer">\n            <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\n            <a id=\'finalize_delete\' href=\'\' class="btn btn-danger">Yes</a>\n          </div>\n        </div>\n      </div>\n    </div>\n\n\n    <div class="text-center">\n        <a class="btn btn-primary" href="/manager/createproduct">Create Product</a>\n    </div>\n    <br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/manager/templates/products.html", "uri": "products.html", "source_encoding": "utf-8", "line_map": {"19": 1, "32": 0, "44": 1, "45": 2, "50": 20, "55": 100, "61": 18, "67": 18, "73": 22, "82": 22, "83": 35, "84": 36, "85": 37, "86": 37, "87": 38, "88": 38, "89": 39, "90": 39, "91": 42, "92": 43, "93": 43, "94": 43, "95": 44, "96": 45, "97": 47, "98": 49, "99": 50, "100": 50, "101": 50, "102": 51, "103": 52, "104": 54, "105": 56, "106": 57, "107": 57, "108": 57, "109": 58, "110": 59, "111": 61, "112": 63, "113": 64, "114": 64, "115": 64, "116": 66, "117": 67, "118": 68, "119": 68, "120": 70, "121": 74, "127": 121}}
__M_END_METADATA
"""
