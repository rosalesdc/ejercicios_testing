
#from odoo import tools
from odoo import tools
from odoo import models, fields, api

class CustomReport(models.Model):
    _name = "my.report"
    _description = "my report"
    _auto = False

    name = fields.Char(string='Name', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
                        SELECT 
                        id,
                        concat(name,' | ', amount_total) as name
                        from purchase_order
                        """)