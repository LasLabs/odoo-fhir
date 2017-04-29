# -*- coding: utf-8 -*-
{
    'name': "Device Metric",

    'summary': """
        Medical device measurement, calculation or setting capability
        """,

    'description': """
        Describes a measurement, calculation or setting capability of a medical device.

        **Scope and Usage**

        The DeviceMetric resource describes mandatory static properties that characterize a direct or derived, quantitative or qualitative 
        biosignal measurement, setting, or calculation produced by a medical device. The DeviceMetric resource can also be used to describe 
        he non-static but highly relevant properties to the metric such as metric status, metric last calibration time and type, measurement mode, 
        color, reference link to the parent DeviceComponent to where it belongs, and any capabilities that the metric offers (for example: setting the metric label).
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/devicemetric.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_device_component'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_device_metric_views.xml',
        'views/hc_res_device_metric_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}