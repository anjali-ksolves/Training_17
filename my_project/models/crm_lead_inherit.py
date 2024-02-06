# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date, datetime, time
from datetime import timedelta


class CRMLeadInherit(models.Model):
    _inherit = 'crm.lead'

    sale_order_tag_ids = fields.Many2one('sale.order.template', string="Sale Order Tags")

    def new_so(self):
        two_hours_ago = datetime.now() - timedelta(hours=2)
        sale_order = self.env['sale.order'].search([('create_date', '>', two_hours_ago)])
        for line in sale_order:
            card = self.env['crm.lead'].search([('partner_id', '=', line.partner_id.id), ('type', '=', 'opportunity')])
            if card:
                line.opportunity_id = card.id
            else:
                new = self.create({
                    'name': line.partner_id.name,
                    'type': 'opportunity',
                    'partner_id': line.partner_id.id,
                })
                line.opportunity_id = new.id

    def action_cancel_so(self):
        # canceled_sale_orders = self.env['sale.order'].search([
        #     ('partner_id', '=', self.partner_id.id),
        #     ('state', '=', 'cancel')
        # ])
        # print(canceled_sale_orders)
        return {
            'type': 'ir.actions.act_window',
            'name': _("Cancelled Sale Orders"),
            'res_model': 'sale.order',
            'view_mode': 'tree',
            'target': 'new',
            'domain': [('partner_id', '=', self.partner_id.id), ('state', '=', 'cancel')],
        }
