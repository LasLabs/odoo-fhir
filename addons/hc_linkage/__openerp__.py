# -*- coding: utf-8 -*-
{
    'name': "Linkage",

    'summary': """
        Relationship between records
        """,

    'description': """
        Identifies two or more records (resource instances) that are referring to the same real-world "occurrence".

        **Scope and Usage** 
        
        This resource allows the assertion of linkages between multiple resource instances (generally of the same type) that are referring 
        to the same underlying business objects. For example, multiple Condition records that refer to the same underlying problem/issue for 
        a particular Patient; multiple AllergyIntolerance records that refer to the same reaction susceptibility; multiple Patient, Practioner 
        and/or RelatedPerson records that refer to the same human being or animal.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/linkage.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_practitioner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_linkage_views.xml',
        'views/hc_res_linkage_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}