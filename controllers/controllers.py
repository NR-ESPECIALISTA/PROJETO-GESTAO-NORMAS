# -*- coding: utf-8 -*-
# from odoo import http


# class CrmDemo(http.Controller):
#     @http.route('/crm_demo/crm_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_demo/crm_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_demo.listing', {
#             'root': '/crm_demo/crm_demo',
#             'objects': http.request.env['crm_demo.crm_demo'].search([]),
#         })

#     @http.route('/crm_demo/crm_demo/objects/<model("crm_demo.crm_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_demo.object', {
#             'object': obj
#         })
