# -*- coding: utf-8 -*-
{
    'name': "Nutrition Request",

    'summary': """
        Request for a diet, formula feeding (enteral) or oral nutritional supplement
        """,

    'description': """
        A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.

        **Scope and Usage**
        
        This resource is a request resource from a FHIR workflow perspective - see Workflow. 
        It is the intent of the Orders and Observation Workgroup to align this resource with the workflow pattern 
        for request resources.

        The NutritionRequest resource describes a request for oral diets (including general diets such as General Healthy 
        diet, or therapeutic diets such as Consistent Carbohydrate, 2 gram Sodium, or Fluid Restricted), 
        oral nutrition supplements (such as nutritionally complete pre-packed drinks), enteral nutrition (tube feedings) 
        nd infant formula which govern the distribution of food and nutritional products used to feed patients within an 
        in-patient setting. It does not cover orders for parenteral (IV) nutrition which are typically filled by pharmacy. 
        These nutrition orders are combined with information on a patient's food allergies and intolerances, and ethnic 
        or cultural food preferences (e.g. Kosher or Vegetarian) to inform healthcare personnel about the type, texture, 
        and/or quantity of foods that the patient should receive or consume.

        Enteral orders are distinguished from supplements because they have some unique attributes and typically include 
        administration information whereas oral nutritional supplements may simply be supplied (e.g. home health or 
        outpatient settings). In a simple case, the requestor may designate type of product, product name and the 
        route of administration along with free text instructions without a having to complete the additional structured 
        details.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/nutritionrequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_nutrition_request_views.xml',
        'views/hc_res_nutrition_request_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}