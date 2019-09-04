# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.addons.http_routing.models.ir_http import slug
import werkzeug
import re
from odoo.exceptions import AccessError, MissingError, UserError
from odoo.http import content_disposition, Controller, request, route


class CustomerPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        print("HOLASSSSSS")
        values = super(CustomerPortal,
                       self)._prepare_portal_layout_values()
        contacts = []

        partner = request.env.user or False

        if partner:
            for contacto in partner.contactos_web_ids:
                print("PARTNER::::",partner.name)
                contact_count = request.env['contactos.web'].search_count([
                    ('usuario_id', '=', partner.id)
                ])
                print("CONTADOR:::",contact_count)
                contacts.append({
                    'name': contacto.name,
                    'correo': contacto.correo,
                    'contact_count': contact_count,
                    'url': "/my/contacto/%s" % slug(contacto)
                })
        values.update({
            'contacts': contacts,
        })
        print(contacts)
        return values
