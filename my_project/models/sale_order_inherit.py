# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    project_task_id = fields.Many2one('project.task', string="Tasks")
    sale_order_wizard = fields.Many2many('sale.order.wizard', string="SO Wizard")

    def remove_task(self):
        self.project_task_id = False


