# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491332330.3185031
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'header', 'message', 'menu_items', 'body_main', 'body_above', 'body_left', 'body_center', 'body_right']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def body_main():
            return render_body_main(context._locals(__M_locals))
        def body_right():
            return render_body_right(context._locals(__M_locals))
        def body_left():
            return render_body_left(context._locals(__M_locals))
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def body_above():
            return render_body_above(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def message():
            return render_message(context._locals(__M_locals))
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\n-->\r\n\r\n\r\n\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.full.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/simplex.css">\r\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.min.css">\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n')
        __M_writer('    <link rel="icon" type="image/png" sizes="32x32"href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/FOMOLogo-03.png">\r\n\r\n')
        __M_writer('    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(' | Family Oriented Music Organization</title>\r\n\r\n  </head>\r\n  <body>\r\n\r\n      <div class="container-fluid">\r\n          <div id="maintenance-row" class="row text-center">\r\n              <div class="alert alert-danger" role="alert">\r\n                  <p><span class="bold">Warning!</span> This is a dev site and we will do maintenace at anytime without notice.</p>\r\n              </div>\r\n          </div><!--maintenance-row-->\r\n      </div><!--container-fluid, maintenance-->\r\n\r\n\r\n\r\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_main'):
            context['self'].body_main(**pageargs)
        

        __M_writer('\r\n\r\n<footer id="footer" class="footer">\r\n      <div class="container">\r\n\r\n            ')

        from datetime import datetime, date
        now = datetime.now()
                    
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['date','now','datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n            <p class="text-muted"> &copy; ')
        __M_writer(str( now.year ))
        __M_writer('. All rights reserved. </p>\r\n      </div>\r\n</footer>\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        request = context.get('request', UNDEFINED)
        def message():
            return render_message(context)
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n      <header>\r\n          <div class="container-fluid">\r\n              <div class="row">\r\n                  <div id="message" >                                                                   <!--Can\'t get it to float right-->\r\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'message'):
            context['self'].message(**pageargs)
        

        __M_writer('\r\n                  </div>\r\n              </div>\r\n          </div> <!--container-fluid, message-->\r\n\r\n\r\n          <div class="container-fluid">\r\n              <div class="row">\r\n                  <nav class="navbar navbar-default">\r\n                      <!-- Brand and toggle get grouped for better mobile display -->\r\n                      <div class="navbar-header">\r\n                          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n                              <span class="sr-only">Toggle navigation</span>\r\n                              <span class="icon-bar"></span>\r\n                              <span class="icon-bar"></span>\r\n                              <span class="icon-bar"></span>\r\n                          </button>\r\n                          <a class="navbar-left" id="logo"href="/"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/FOMOLogo-01.png" alt="FOMO Logo"></a>\r\n                      </div>\r\n\r\n        <!-- Collect the nav links, forms, and other content for toggling -->\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                <ul class="nav navbar-nav">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\r\n                </ul>\r\n\r\n                <ul class="nav navbar-nav navbar-right">\r\n')
        if request.user.is_authenticated:
            __M_writer('\r\n                    <li><span id=\'cart-count\' class="badge">')
            __M_writer(str(request.user.get_cart_count()))
            __M_writer('</span><a id="cart"  href="/checkout/cart"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/cart.png" alt="Shopping Cart"></a></li>\r\n\r\n                        <li class="dropdown">\r\n\r\n                                <a href="#" class=" dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Hi ')
            __M_writer(str( request.user.first_name ))
            __M_writer('<span class="caret"></span></a>\r\n                                    <ul class="dropdown-menu">\r\n                                        <li><a href="/account/myaccount">My Account</a></li>\r\n                                        <li><a href="/account/logout">Log Out</a></li>\r\n\r\n                                    </ul>\r\n\r\n                        </li>\r\n')
        else:
            __M_writer('                        <li><a href="/account/signup">Signup</a></li>\r\n                        <li><a id=\'login-modal-button\' >Log In</a></li>\r\n')
        __M_writer('\r\n                </ul>\r\n            </div><!-- /.navbar-collapse -->\r\n                </nav>\r\n            </div>\r\n        </div> <!--container-fluid, navbar-->\r\n        </header>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def message():
            return render_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_main():
            return render_body_main(context)
        def body_left():
            return render_body_left(context)
        def body_right():
            return render_body_right(context)
        request = context.get('request', UNDEFINED)
        def body_center():
            return render_body_center(context)
        def body_above():
            return render_body_above(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <div class="container-fluid">\r\n                <div id="row-above"class="row">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_above'):
            context['self'].body_above(**pageargs)
        

        __M_writer('\r\n                </div>\r\n                <div id="body-row" class="row is-table-row">\r\n                    <div id="body-left" class="col-md-2">\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

        __M_writer('\r\n                    </div>\r\n\r\n                    <div id="body-center" class="col-md-8">\r\n\r\n\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n                    </div>\r\n                    <div id="body-right" class="col-md-2">\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_right'):
            context['self'].body_right(**pageargs)
        

        __M_writer('\r\n                    </div>\r\n                </div> <!--body-row-->\r\n            </div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_above(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_above():
            return render_body_above(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        <br/>\r\n\r\n                        <br/>\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_right():
            return render_body_right(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n                            <ul class="nav nav-stacked panel">\r\n                                <li class="panel-title text-center">Recent Products:</li>\r\n')
        if request.user.is_authenticated:
            for prod in request.user.displayHistory():
                __M_writer('                                    <li><a href="/catalog/detail/')
                __M_writer(str( prod.id ))
                __M_writer('"> ')
                __M_writer(str( prod.name ))
                __M_writer(' </a></li>\r\n')
        else:
            __M_writer('                                    <p><a href="/account/login/">Sign in</a> to view your recent products.</p>\r\n')
        __M_writer('                            </ul>\r\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"17": 4, "19": 0, "45": 2, "46": 4, "47": 32, "48": 34, "49": 34, "50": 35, "51": 35, "52": 36, "53": 36, "54": 37, "55": 37, "56": 38, "57": 38, "58": 41, "59": 41, "60": 41, "61": 44, "62": 44, "63": 44, "64": 47, "69": 47, "74": 123, "79": 164, "80": 169, "87": 172, "88": 173, "89": 173, "90": 179, "91": 179, "92": 179, "98": 47, "104": 47, "110": 62, "122": 62, "127": 69, "128": 86, "129": 86, "134": 94, "135": 98, "136": 99, "137": 100, "138": 100, "139": 100, "140": 100, "141": 104, "142": 104, "143": 112, "144": 113, "145": 116, "151": 67, "157": 67, "163": 92, "169": 92, "175": 125, "190": 125, "195": 132, "200": 138, "205": 146, "210": 160, "216": 128, "222": 128, "228": 136, "234": 136, "240": 144, "246": 144, "252": 149, "259": 149, "260": 152, "261": 153, "262": 154, "263": 154, "264": 154, "265": 154, "266": 154, "267": 156, "268": 157, "269": 159, "275": 269}}
__M_END_METADATA
"""
