from odoo import models, fields

class CustomerPaymentReport(models.Model):
    _name = 'customer.payment.report'
    _description ="Customer Payment Report"

    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', string='Customer')
    first_sales_date = fields.Date(string='First Sales Date')
    total_sale_count = fields.Integer(string='Total Sale Count')
    total_amount = fields.Float(string='Total Amount')
    paid_amount = fields.Float(string='Paid Amount')
    balance_amount = fields.Float(string='Balance Amount')

    