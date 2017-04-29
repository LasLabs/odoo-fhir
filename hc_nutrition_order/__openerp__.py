# -*- coding: utf-8 -*-
{
    'name': "Nutrition Order",

    'summary': """
        Request for a diet, formula feeding (enteral) or oral nutritional supplement
        """,

    'description': """
        A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident. 

        **Scope and Usage**

        The NutritionOrder resource describes a request for oral diets (including general diets such as General Healthy diet, or therapeutic diets 
        such as Consistent Carbohydrate, 2 gram Sodium, or Fluid Restricted), oral nutrition supplements (such as nutritionally complete pre-packed drinks), 
        enteral nutrition (tube feedings) and infant formula which govern the distribution of food and nutritional products used to feed patients within 
        an in-patient setting. It does not cover orders for parenteral (IV) nutrition which are typically filled by pharmacy. These nutrition orders are combined 
        with information on a patient's food allergies and intolerances, and ethnic or cultural food preferences (e.g. Kosher or Vegetarian) to inform healthcare 
        personnel about the type, texture, and/or quantity of foods that the patient should receive or consume. 
        
        Enteral orders are distinguished from supplements because they have some unique attributes and typically include administration information whereas 
        oral nutritional supplements may simply be supplied (e.g. home health or outpatient settings). In a simple case, the requestor may designate type of 
        product, product name and the route of administration along with free text instructions without a having to complete the additional structured details. 
        
        This resource is intended to be used by providers from a variety of specialties such as physicians, dietitian/nutritionists, or speech therapists. 
        One provider may simply order a base element oral diet such as General Healthful diet. Another provider, based on scope of practice, may use 
        other elements to communicate additional therapeutic needs or patient preferences. The optionality included gives an ordering provider the capability 
        to write a simple order for an oral diet, nutritional supplement or formula with minimal requirements beyond that of specifying the diet, supplement 
        or formula product, but also supports the ability to provide more detailed information that may be further augmented by a dietitian or nutrition specialist. 
        For example, a physician may order a 2 g sodium diet. A speech therapist, based on the results of a swallowing evaluation, then orders a mechanically 
        altered texture with nectar thick liquids. 
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/nutritionorder.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_allergy_intolerance', 'hc_encounter'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_nutrition_order_views.xml',
        'views/hc_res_nutrition_order_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}