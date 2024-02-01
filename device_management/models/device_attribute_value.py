# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    name = fields.Char(string="Name")
    device_attribute_id = fields.Many2one('device.attribute', string="Device Attribute")