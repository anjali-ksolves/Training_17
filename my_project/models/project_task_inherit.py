# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'

    sale_order = fields.Integer(string="Sale Order")
    sale_order_ids = fields.One2many('sale.order', 'project_task_id', string="Sale Orders")
    total = fields.Float(compute="_compute_total", store=True)

    @api.depends('sale_order_ids.amount_total')
    def _compute_total(self):
        sum = 0
        for line in self.sale_order_ids:
            sum += line.amount_total
        self.total = sum






