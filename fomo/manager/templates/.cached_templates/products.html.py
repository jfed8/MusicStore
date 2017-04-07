# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490749278.5422626
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/manager/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
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
        products = context.get('products', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        hasattr = context.get('hasattr', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
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
        __M_writer('\r\n    Products\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def body_center():
            return render_body_center(context)
        hasattr = context.get('hasattr', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3> Products List </h3>\r\n    <p> Below is a table of the current inventory</p>\r\n    <table class="table table-striped">\r\n        <tr>\r\n            <th> Category</th>\r\n            <th>Name</th>\r\n            <th>Price</th>\r\n            <th>Quantity</th>\r\n            <th>Serial Number</th>\r\n            <th>Barcode</th>\r\n            <th>Action</th>\r\n        </tr>\r\n')
        for p in products:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str(p.category.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(p.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(p.price))
            __M_writer('</td>\r\n                <td>\r\n                    <!-- possible solution  % if isinstance(p, cmod.BulkProduct): but have to import catalog.models-->\r\n')
            if hasattr(p, 'quantity'): ##<!--This is duck typing-->
                __M_writer('                        <span class="quantity_text">')
                __M_writer(str(p.quantity))
                __M_writer('</span>\r\n                        <button data-pid=')
                __M_writer(str(p.id))
                __M_writer(' class="update_quantity_button btn btn-info btn-xs" name="button">Update</button>\r\n')
            else:
                __M_writer('                        -\r\n')
            __M_writer('                </td>\r\n                <td>\r\n')
            if hasattr(p, 'serial_number'): ##<!--This is duck typing-->
                __M_writer('                        ')
                __M_writer(str(p.serial_number))
                __M_writer('\r\n')
            else:
                __M_writer('                        -\r\n')
            __M_writer('                </td>\r\n                <td>\r\n')
            if hasattr(p, 'barcode'): ##<!--This is duck typing-->
                __M_writer('                        ')
                __M_writer(str(p.barcode))
                __M_writer('\r\n')
            else:
                __M_writer('                        -\r\n')
            __M_writer('                </td>\r\n                <td>\r\n')
            if request.user.has_perm('catalog.change_product'):
                __M_writer("                        <a href='/manager/product/")
                __M_writer(str(p.id))
                __M_writer("'>Edit</a>\r\n")
            if request.user.has_perm('account.delete_product'):
                __M_writer("                        |\r\n                        <a class='delete_link'  href='/manager/product.delete/")
                __M_writer(str(p.id))
                __M_writer("'>Delete</a>\r\n")
            __M_writer('                </td>\r\n            </tr>\r\n\r\n')
        __M_writer('    </table>\r\n\r\n    <!-- Modal -->\r\n    <div class="modal fade" id="DeleteConfirm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n      <div class="modal-dialog" role="document">\r\n        <div class="modal-content">\r\n          <div class="modal-header">\r\n            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n            <h4 class="modal-title" id="myModalLabel">Confirm</h4>\r\n          </div>\r\n          <div class="modal-body">\r\n            Are you sure you want to delete this product?\r\n          </div>\r\n          <div class="modal-footer">\r\n            <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n            <a id=\'finalize_delete\' href=\'\' class="btn btn-danger">Yes</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n\r\n    <div class="text-center">\r\n        <a class="btn btn-default" href="/manager/createproduct">Create Product</a>\r\n    </div>\r\n    <br>\r\n    <p>Our support teams and account management teams provide the best service in the industry. We\'re passionate about our\r\n        products as well as our employees and it shows in the level of service that we provide. We\'re always happy to help\r\n        find the solution for your needs. If you are in need of support, reach out to our support team (@fomo_support) on\r\n        the company Slack channel.</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/manager/templates/products.html", "uri": "products.html", "source_encoding": "utf-8", "line_map": {"17": 1, "30": 0, "42": 1, "43": 2, "48": 20, "53": 105, "59": 18, "65": 18, "71": 22, "80": 22, "81": 35, "82": 36, "83": 37, "84": 37, "85": 38, "86": 38, "87": 39, "88": 39, "89": 42, "90": 43, "91": 43, "92": 43, "93": 44, "94": 44, "95": 45, "96": 46, "97": 48, "98": 50, "99": 51, "100": 51, "101": 51, "102": 52, "103": 53, "104": 55, "105": 57, "106": 58, "107": 58, "108": 58, "109": 59, "110": 60, "111": 62, "112": 64, "113": 65, "114": 65, "115": 65, "116": 67, "117": 68, "118": 69, "119": 69, "120": 71, "121": 75, "127": 121}}
__M_END_METADATA
"""
