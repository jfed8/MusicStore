# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490754236.7929316
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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
        __M_writer('\r\n    Terms\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Terms and Conditions</h3>\r\n\r\n      <ol>\r\n          <li>Introduction\r\n              <p>\r\n                  These Website Standard Terms and Conditions written on this webpage shall manage your use of this website. These Terms\r\n                  will be applied fully and affect to your use of this Website. By using this Website, you agreed to accept all terms and\r\n                  conditions written in here. You must not use this Website if you disagree with any of these Website Standard Terms and\r\n                  Conditions.\r\n              </p>\r\n              <p></p>\r\n          </li>\r\n          <li>Intellectual Property Rights\r\n              <p>\r\n                  Other than the content you own, under these Terms, Family Oriented Music Organization and/or its licensors own all the intellectual property rights and materials contained in this Website.\r\n              </p>\r\n          </li>\r\n          <li>Restrictions\r\n              <p>You are specifically restricted from all of the following:</p>\r\n              <ul>\r\n                  <li>publishing any Website material in any other media;</li>\r\n                  <li>selling, sublicensing and/or otherwise commercializing any Website material;</li>\r\n                  <li>publicly performing and/or showing any Website material;</li>\r\n                  <li>using this Website in any way that is or may be damaging to this Website;</li>\r\n                  <li>using this Website in any way that impacts user access to this Website;</li>\r\n                  <li>using this Website contrary to applicable laws and regulations,\r\n                      or in any way may cause harm to the Website, or to any person or business entity;</li>\r\n                  <li>engaging in any data mining, data harvesting, data extracting or any\r\n                      other similar activity in relation to this Website;</li>\r\n                  <li>using this Website to engage in any advertising or marketing.</li>\r\n              </ul>\r\n              <p>Certain areas of this Website are restricted from being access by you and Family Oriented Music Organization may further restrict access by you to any areas of this Website, at any time, in absolute discretion. Any user ID and password you may have for this Website are confidential and you must maintain confidentiality as well.</p>\r\n          </li>\r\n          <li>Your Content\r\n              <p>In these Website Standard Terms and Conditions, “Your Content” shall mean any audio, video text, images or other material you choose to display on this Website. By displaying Your Content, you grant Family Oriented Music Organization a non-exclusive, worldwide irrevocable, sub licensable license to use, reproduce, adapt, publish, translate and distribute it in any and all media.</p>\r\n              <p>Your Content must be your own and must not be invading any third-party’s rights. Family Oriented Music Organization reserves the right to remove any of Your Content from this Website at any time without notice.</p>\r\n          </li>\r\n          <li>No warranties\r\n              <p>This Website is provided “as is,” with all faults, and Family Oriented Music Organization express no representations or warranties, of any kind related to this Website or the materials contained on this Website. Also, nothing contained on this Website shall be interpreted as advising you.</p>\r\n          </li>\r\n          <li>Limitation of liability\r\n              <p>In no event shall Family Oriented Music Organization, nor any of its officers, directors and employees, shall be held liable for anything arising out of or in any way connected with your use of this Website whether such liability is under contract.  Family Oriented Music Organization, including its officers, directors and employees shall not be held liable for any indirect, consequential or special liability arising out of or in any way related to your use of this Website.</p>\r\n          </li>\r\n          <li>Indemnification\r\n              <p>You hereby indemnify to the fullest extent Family Oriented Music Organization from and against any and/or all liabilities, costs, demands, causes of action, damages and expenses arising in any way related to your breach of any of the provisions of these Terms.</p>\r\n          </li>\r\n          <li>Severability\r\n              <p>If any provision of these Terms is found to be invalid under any applicable law, such provisions shall be deleted without affecting the remaining provisions herein.</p>\r\n          </li>\r\n          <li>Variation of Terms\r\n              <p>Family Oriented Music Organization is permitted to revise these Terms at any time as it sees fit, and by using this Website you are expected to review these Terms on a regular basis.</p>\r\n          </li>\r\n          <li>Assignment\r\n              <p>The Family Oriented Music Organization is allowed to assign, transfer, and subcontract its rights and/or obligations under these Terms without any notification. However, you are not allowed to assign, transfer, or subcontract any of your rights and/or obligations under these Terms.</p>\r\n          </li>\r\n          <li>Entire Agreement\r\n              <p>These Terms constitute the entire agreement between Family Oriented Music Organization and you in relation to your use of this Website, and supersede all prior agreements and understandings.</p>\r\n          </li>\r\n          <li>Governing Law &amp; Jurisdiction\r\n              <p>These Terms will be governed by and interpreted in accordance with the laws of the State of UT, and you submit to the non-exclusive jurisdiction of the state and federal courts located in UT for the resolution of any disputes.</p>\r\n              <p>These terms and conditions have been generated at termsandcondiitionssample.com.</p>\r\n          </li>\r\n      </ol>\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/terms.html", "uri": "terms.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 19, "47": 88, "53": 17, "59": 17, "65": 21, "71": 21, "77": 71}}
__M_END_METADATA
"""
