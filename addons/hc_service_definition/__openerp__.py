# -*- coding: utf-8 -*-
{
    'name': "Service Definition",

    'summary': """
        Decision support functionality
        """,

    'description': """
        The ServiceDefinition describes a unit of decision support functionality that is made available as a service, such as immunization modules or drug-drug interaction checking. 

        **Scope and Usage** 

        The ServiceDefinition defines a module of clinical decision support functionality made available by a decision support service. 
        For example, a service may provide immunization modules, drug-drug interaction checking, or appropriate use assessment.
        
        Each module defines three main features related to its functionality:
        
        * Input and output parameters
        * Data requirements
        * Triggers
        
        Input and output parameters are used to specify any named parameters used by the module. These are typically patient-independent configuration parameters 
        such as an A1C threshold for a diabetes control module, but they may also be used to return calculations performed by the module.
        
        Data requirements are used to specify the set of data that must be provided (or available) to the module in order to achieve a successful evaluation. 
        For example, if the module requires A1C lab results within the last 6 months, or information on bilateral or both left and right amputation at or below the knee.
        
        Triggers are used to advertise when the module should be invoked. On encountering a specific trigger, a clinical application can invoke the modules associated 
        with the trigger using the $evaluate operation. Any data required by the module can be sent as part of the request, and any suggested actions and other output 
        data are returned via the GuidanceResponse resource.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/servicedefinition.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_service_definition_views.xml',
        'views/hc_res_service_definition_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}