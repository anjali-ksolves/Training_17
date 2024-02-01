# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    name = fields.Char(string="Name", copy=False)
    required = fields.Boolean(string="Required")
    device_type_id = fields.Many2one('device.type', string="Device Type Id")
    device_attribute_value_ids = fields.One2many('device.attribute.value', 'device_attribute_id', string= "Device Attribute Value")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]