# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    def index(self, **kw): #index nombre arbitrario de la función
        return http.request.render('Academy.index', { #nombre del módulo e index es por la página default
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })

