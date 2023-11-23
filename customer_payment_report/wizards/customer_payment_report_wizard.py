from odoo import models, fields

class CustomerPaymentReportWizard(models.TransientModel):
    _name = 'customer.payment.report.wizard'
    _description = 'Customer Payment Report Wizard'

    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To', default=fields.Date.today)
    report_id = fields.Many2one('customer.payment.report')

    def generate_report(self):
        query = """
            SELECT
                c.id as customer_id,
                MIN(s.date_order) as first_sales_date,
                COUNT(s.id) as total_sale_count,
                SUM(s.amount_total) as total_amount,
                COALESCE(SUM(p.amount), 0) as paid_amount,
                SUM(s.amount_total) - COALESCE(SUM(p.amount), 0) as balance_amount
            FROM
                sale_order c
            LEFT JOIN
                sale_order s ON c.id = s.partner_id
            LEFT JOIN
                account_payment p ON s.id = p.id
            WHERE
                s.date_order BETWEEN %s AND %s
            GROUP BY
                c.id
        """
        # query ="""
        #     select customer_id,first_sales_date,total_sale_count,total_amount,paid_amount,balance_amount from customer_payment_report """ 
     
        self.env.cr.execute(query, (self.date_from, self.date_to))
        result = self.env.cr.dictfetchall()
        report_data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'data': result,
        }
        return self.env.ref('customer_payment_report.report_customer_payment').report_action(self, data=report_data)
        
