# -*- coding: utf-8 -*-
{
    'name': "Imaging Manifest",

    'summary': """
        DICOM images and other content
        """,

    'description': """
        A manifest of a set of DICOM Service-Object Pair Instances (SOP Instances). The referenced SOP Instances 
        (images or other content) are for a single patient, and may be from one or more studies. 
        The referenced SOP Instances may have been selected for a purpose, such as conference, or consult. 
        Reflecting a range of sharing purposes, typical ImagingManifest resources may include all SOP Instances 
        in a study (perhaps for sharing through a Health Information Exchange); key images from multiple studies 
        (for reference by a referring or treating physician); both a multi-frame ultrasound instance 
        ("cine" video clip) and a set of measurements taken from that instance (for inclusion in a teaching file); 
        and so on.

        **Scope and Usage**
        This resource provides information on a selected set of imaging objects, along with information on how to 
        retrieve those instances (either in native DICOM format, or in a rendered format, such as JPEG), or launch 
        an image viewer. The ImagingManifest is used to make available information concerning images etc. that are 
        intended to be exchanged into other clinical contexts such as diagnostic reports, Care Plans, etc.
    """,

    'author': "Luigi Sison",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_imaging_study'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_imaging_manifest_views.xml',
        'views/hc_res_imaging_manifest_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
    }