# -*- coding: utf-8 -*-
# from odoo import http


# class Relaciones(http.Controller):
#     @http.route('/relaciones/relaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/relaciones/relaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('relaciones.listing', {
#             'root': '/relaciones/relaciones',
#             'objects': http.request.env['relaciones.relaciones'].search([]),
#         })

#     @http.route('/relaciones/relaciones/objects/<model("relaciones.relaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('relaciones.object', {
#             'object': obj
#         })
