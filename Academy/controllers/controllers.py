# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw): #index nombre arbitrario de la función
        Teachers = http.request.env['academy.teachers']
        return http.request.render('Academy.index', { #nombre del módulo e index es por la página default
            'teachers': Teachers.search([])
        })
    
    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })


