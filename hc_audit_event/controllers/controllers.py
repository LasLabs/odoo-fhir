# -*- coding: utf-8 -*-
from openerp import http

# class HcAuditEvent(http.Controller):
#     @http.route('/hc_audit_event/hc_audit_event/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_audit_event/hc_audit_event/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_audit_event.listing', {
#             'root': '/hc_audit_event/hc_audit_event',
#             'objects': http.request.env['hc_audit_event.hc_audit_event'].search([]),
#         })

#     @http.route('/hc_audit_event/hc_audit_event/objects/<model("hc_audit_event.hc_audit_event"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_audit_event.object', {
#             'object': obj
#         })