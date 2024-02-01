# -*- coding: utf-8 -*-

{
    'name': 'Device Management',
    'depends': ['base', 'hr', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/device_management_settings.xml',
        'views/menu.xml',
        'views/device_type.xml',
        'views/device_attribute.xml',
        'views/employee.xml',
        'views/device_assignment.xml',
        'views/device_view.xml',
        'views/device_model.xml',
        'views/device_brand.xml',
        'views/device_attribute_value.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'device_management/static/src/xml/device_button.xml',
            'device_management/static/src/xml/approved.xml',
            'device_management/static/src/js/device_button.js',
            # 'device_management/static/src/js/device_extend.js',
            'device_management/static/src/js/approved.js',
        ]
    },
    'installable': True,
    'application': True,
    'auto-install': False,
}
