# -*- coding: utf-8 -*-
{
    'name': "Goal",

    'summary': """
        Patient, group or organization objective
        """,

    'description': """
        Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, 
        restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.

        **Scope and Usage** 
        
        A Goal in health care services delivery is generally an expressed desired health state to be achieved by a subject of care (or family/group) over a period or at a specific point of time. This desired target health state may be achieved as a result of health care intervention(s) or resulting from natural recovery over time. For example:

        * A goal of a plan for a condition such as a diabetes might specify desired outcome(s) (e.g. HgbA1c level =<5.6% in 3 months) 
        as a result of interventions such as medication therapy, nutritional management and/or increase physical activity.
        * A goal of a procedure might be to meet the intended objective of the procedure (e.g. wet-dry-dressing changes twice a day; 
        goal: wound healed completely in 2 weeks) or to prevent an unintended complication (e.g. repositioning a patient every two hours: 
        goal to maintain skin integrity)
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/goal.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_procedure_request', 'hc_observation', 'hc_risk_assessment', 'hc_medication_statement', 'hc_nutrition_request'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_goal_views.xml',
        'views/hc_res_goal_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}