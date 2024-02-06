# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date, datetime, time
from datetime import timedelta


class CRMLeadInherit(models.Model):
    _inherit = 'crm.lead'

    so_ids = fields.Many2one('sale.order', string="Sale Orders")
    so_tag_ids = fields.Many2many('sale.order.template', string="Sale Order Tags")

    # @api.depends('so_ids')
    # def _compute_tags(self):
    #     pass
        # for lead in self:
        #     tag_ids = []
        #     if lead.so_ids:
        #         tag_ids = lead.so_ids.sale_order_template_id
        #     lead.tag_ids = tag_ids

    def action_cancel_so(self):
        pass

    def new_so(self):
        two_hours_ago = datetime.now() - timedelta(hours=2)
        sale_order = self.env['sale.order'].search([('create_date', '>', two_hours_ago)], limit=1)

        if sale_order:
            # tag_ids = [(6, 0, [sale_order.sale_order_template_id.id])] if sale_order.sale_order_template_id else False

            opportunity = self.create({
                'name': sale_order.name,
                # 'partner_id': sale_order.partner_id
                'so_ids': sale_order.id,
                # 'tag_ids': tag_ids,
            })

            return opportunity

    # @api.model
    # def create(self, vals_list):
    #     opportunity = self.env['crm.lead'].create({
    #         'name': vals_list.get('name', ''),
    #         'partner_id': vals_list.get('partner_id', False),
    #     })
    #     vals_list['opportunity_id'] = opportunity.id
    #     quotation = super(SaleInheritance, self).create(vals_list)
    #     return quotation
