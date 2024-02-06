# -*- coding: utf-8 -*-

{
    'name': 'My Project',
    'author': 'Anjali',
    'depends': ['base', 'hr', 'web', 'project', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_order_wizard.xml',
        'views/project_task_inherit.xml',
        'views/sale_order_inherit.xml',
        'views/crm_lead_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False,
    'sequence': -100,
}
