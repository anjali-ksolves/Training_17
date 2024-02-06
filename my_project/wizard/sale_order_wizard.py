# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'

    sale_order_ids = fields.Many2many('sale.order', string="Sale Orders")

    def action_save(self):
        active_id = self.env.context.get('active_id')
        project = self.env['project.task'].browse(active_id)
        for line in self.sale_order_ids:
            project.write({
                'sale_order_ids': [(4, line.id)],
            })


    # name = fields.Char(string="SO Name")
    # # date_order = fields.datetime(string="Order Date")
    # partner_id = fields.Many2one('res.partner', string="Customer")
    # user_id = fields.Many2one('res.users', string="Salesperson")
    # company_id = fields.Many2one('sale.order', string="Company")

    # amount_total = fields.Monetary(string="Total", store=True, compute='_compute_amounts', tracking=4)

    # def action_save(self):
    #     active_id = self.env.context.get('active_id')
    #     project = self.env['project.task'].browse(active_id)
    #     for rec in self.sale_order_ids:
    #         val = {
    #             'name': rec.name,
    #             'partner_id': rec.partner_id.id,
    #             'user_id': rec.user_id.id,
    #             'company_id': rec.company_id.id
    #         }
    #         print(val)
    #         if not rec.id in project.sale_order_ids.ids:
    #             project.sale_order_ids = [(0, 0, val)]


