# -*- coding: utf-8 -*-
import datetime
from odoo import models, api


class PaymentReportModel(models.AbstractModel):
    _name = 'payment.report'
    _description = 'Payment Report '
    # _inherit = 'report.abstract_report'

    def _get_report_values(self, docids, data=None):
        # Fetch data from 'data' and return it
        return {
            'doc_ids': docids,
            'doc_model': 'payment.report',
            'docs': self.env['payment.report'].browse(docids),
            'data': data,
        }