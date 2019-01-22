
#from odoo import tools
from odoo import tools
from odoo import models, fields, api

class CustomReport(models.Model):
    _name = "my.report"
    _description = "my report"
    _auto = False

    name = fields.Char(string='Nombre', readonly=True)
    partner_name = fields.Char(string='Nombre Partner', readonly=True)
    
#    def init(self):
#        tools.drop_view_if_exists(self._cr, self._table)
#        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
#                        SELECT 
#                        id,
#                        concat(name,' | ', amount_total) as name,
#                        amount_total as amount_t
#                        from purchase_order
                        #""")
    
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
                        SELECT purchase_order.id, purchase_order.name as name,res_partner.name as partner_name
                        FROM purchase_order 
                        INNER JOIN res_partner 
                        ON purchase_order.partner_id=res_partner.id;
                        """)