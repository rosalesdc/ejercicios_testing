# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models
from odoo import api
from werkzeug.urls import url_encode

class ContactosWeb(models.Model):
    _name = 'contactos.web'
    #_inherit = ['portal.mixin']
    _description = 'Contactos desde web'

    name = fields.Char(
        string="Nombre",
        required=True
    )

    correo = fields.Char(
        string='Correo-e'
    )

    edad = fields.Selection(
        selection=[
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
            ('24', '24'),
            ('25', '25'),
        ],
        string="Edad"
    )
    usuario_id = fields.Many2one(
        comodel_name='res.users', string='Usuario'
    )

class UsuarioContactoWeb(models.Model):
    _inherit = 'res.users'

    contactos_web_ids = fields.One2many(
        comodel_name='contactos.web',
        inverse_name='usuario_id',
        string = 'Contactos Web'
    )
