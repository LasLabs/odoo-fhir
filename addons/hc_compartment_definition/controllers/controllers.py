# -*- coding: utf-8 -*-
from openerp import http

# class HcCompartmentDefinition(http.Controller):
#     @http.route('/hc_compartment_definition/hc_compartment_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_compartment_definition/hc_compartment_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_compartment_definition.listing', {
#             'root': '/hc_compartment_definition/hc_compartment_definition',
#             'objects': http.request.env['hc_compartment_definition.hc_compartment_definition'].search([]),
#         })

#     @http.route('/hc_compartment_definition/hc_compartment_definition/objects/<model("hc_compartment_definition.hc_compartment_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_compartment_definition.object', {
#             'object': obj
#         })