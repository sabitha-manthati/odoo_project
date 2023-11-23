from odoo import api, models,fields

class PurchaseDashboard(models.AbstractModel):
    _name = 'purchase.dashboard'
    _description = 'Purchase Dashboard'

     
    @api.model
    @api.depends('total_purchase_count', 'total_untaxed_amount', 'total_purchase_amount')
    def get_dashboard_data(self):
        purchase_orders = self.env['purchase.order'].search([])
        total_purchase_count = len(purchase_orders)
        total_untaxed_amount = sum(order.amount_untaxed for order in purchase_orders)
        total_purchase_amount = sum(order.amount_total for order in purchase_orders)

        return {
            'total_purchase_count': total_purchase_count,
            'total_untaxed_amount': total_untaxed_amount,
            'total_purchase_amount': total_purchase_amount,
        }
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_purchase_count = fields.Float('Total Puchase Count')
    total_untaxed_amount = fields.Float('Total untaxed Count')
    total_purchase_amount = fields.Float('Total Puchase Count')
  



