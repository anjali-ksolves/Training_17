# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    def write(self, values):
        orders = self.mapped('order_id')
        for order in orders:
            order_lines = self.filtered(lambda x: x.order_id == order)
            msg = "The ordered quantity has been updated."
            for line in order_lines:
                msg += _(
                    "Ordered Quantity: %(old_qty)s -> %(new_qty)s",
                    old_qty=line.product_uom_qty,
                    new_qty=values["product_uom_qty"]
                )
            order.message_post(body=msg)
        return super(SaleOrderLineInherit, self).write(values)
