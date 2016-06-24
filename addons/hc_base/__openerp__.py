# -*- coding: utf-8 -*-
{
    'name': "Health Care Base",

    'summary': """
        Module needed by all Health Care modules.""",

    'description': """
        Contains: FHIR Complex Types, common definitions
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/datatypes.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/hc_base_data.xml',
        # 'data/l10n_au/country_pl.xml',
        # 'data/l10n_ph/country_pl.xml',
        'data/l10n_us/country_pl.xml',
        'data/l10n_us/res.country.state.csv',
        'data/l10n_us/hc.vs.country.city.type.csv',
        'views/hc_value_set_views.xml',
        'views/views.xml',
        'views/hc_address_views.xml',
        'views/hc_annotation_views.xml',
        'views/hc_attachment_views.xml',
        'views/hc_human_name_views.xml',
        'views/hc_identifier_views.xml',
        'views/hc_telecom_views.xml',
        'views/templates.xml',    
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        # 'demo/hc.vs.country.city.csv',
    ],
}
