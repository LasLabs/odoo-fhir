# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ImplementationGuide(models.Model):    
    _name = "hc.res.implementation.guide"    
    _description = "Implementation Guide"                

    url = fields.Char(string="URL", required="True", help="Absolute URL used to reference this Implementation Guide.")                        
    version = fields.Char( help="Logical id for this version of the Implementation Guide.")                        
    name = fields.Char( required="True", help="Informal name for this Implementation Guide.")                        
    status = fields.Selection(string="Status", required="True", selection=[("draft", "Draft"), ("active", "Active"), ("retired", "Retired")], help="The status of this implementation guide. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(string="Experimental", help="If for testing purposes, not real usage.")                        
    publisher = fields.Char( help="Name of the publisher (Organization or individual).")                        
    contact_ids = fields.One2many(comodel_name="hc.implementation.guide.contact", inverse_name="implementation_guide_id", string="Contacts", help="Contact details for the publisher.")                        
    date = fields.Datetime(string="Date", help="Date for this version of the Implementation Guide.")                        
    description = fields.Text( help="Natural language description of the Implementation Guide.")                        
    use_context_ids = fields.One2many(comodel_name="hc.implementation.guide.use.context", inverse_name="implementation_guide_id", string="Use Contexts", help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(comodel_name="hc.vs.jurisdiction", relation="implementation_guide_jurisdiction_rel", string="Jurisdictions", help="Intended jurisdiction for implementation guide (if applicable).")                        
    copyright = fields.Char( help="Use and/or publishing restrictions.")                        
    fhir_version = fields.Char( help="FHIR Version this Implementation Guide targets.")                        
    binary_ids = fields.One2many(comodel_name="hc.implementation.guide.binary", inverse_name="implementation_guide_id", string="Binary URIs", help="URI of image, css, script, etc..")                        
    dependency_ids = fields.One2many(comodel_name="hc.implementation.guide.dependency", inverse_name="implementation_guide_id", string="Dependencies", help="Another Implementation guide this depends on.")                        
    package_ids = fields.One2many(comodel_name="hc.implementation.guide.package", inverse_name="implementation_guide_id", string="Packages", required="True", help="Group of resources as used in .page.package.")                        
    global_ids = fields.One2many(comodel_name="hc.implementation.guide.global", inverse_name="implementation_guide_id", string="Globals", help="Profiles that apply globally.")                        
    page_ids = fields.One2many(comodel_name="hc.implementation.guide.page", inverse_name="implementation_guide_id", string="Pages", required="True", help="Page/Section in the Guide.")                        

class ImplementationGuideDependency(models.Model):    
    _name = "hc.implementation.guide.dependency"    
    _description = "Implementation Guide Dependency"                

    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Dependency.")                        
    type = fields.Selection(string="Type", required="True", selection=[("reference", "Reference"), ("inclusion", "Inclusion")], help="How the dependency is represented when the guide is published.")                        
    uri = fields.Char(string="URI", required="True", help="Where to find dependency.")                        

class ImplementationGuidePackage(models.Model):    
    _name = "hc.implementation.guide.package"    
    _description = "Implementation Guide Package"                

    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Package.")                        
    name = fields.Char( required="True", help="Name used .page.package.")                        
    description = fields.Text( help="Human readable text describing the package.")                        
    resource_ids = fields.One2many(comodel_name="hc.implementation.guide.package.resource", inverse_name="package_id", string="Resources", required="True", help="Resource in the implementation guide.")                        

class ImplementationGuidePackageResource(models.Model):    
    _name = "hc.implementation.guide.package.resource"    
    _description = "Implementation Guide Package Resource"                

    package_id = fields.Many2one(comodel_name="hc.implementation.guide.package", string="Package", 
        help="Group of resources as used in .page.package.")                        
    example = fields.Boolean(string="Example", required="True", help="If not an example, has it's normal meaning.")                        
    name = fields.Char( help="Human Name for the resource.")                        
    description = fields.Text( help="Reason why included in guide.")                        
    acronym = fields.Char( help="Short code to identify the resource.")                        
    source_type = fields.Selection(string="Source Type", required="True", selection=[("uri", "URI"), ("string", "String"), ("Resource Type", "Resource Type")], help="Type of location of the resource.")                        
    source_name = fields.Char(string="Source", compute="_compute_source_name", store="True", help="Location of the resource.")                        
    source = fields.Char(string="Source URL", help="URI that location of the resource.")                        
    source_string = fields.Char(string="Source String", help="String of location of the resource.")                        
    source_code_id = fields.Many2one(comodel_name="hc.vs.resource.type", string="Reason Resource", help="Resource type of location of the resource.")                        
    example_for_id = fields.Many2one(comodel_name="hc.res.structure.definition", string="Example For", help="Resource this is an example of (if applicable).")                        

class ImplementationGuideGlobal(models.Model):    
    _name = "hc.implementation.guide.global"    
    _description = "Implementation Guide Global"                

    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Global.")                        
    type_id = fields.Many2one(comodel_name="hc.vs.resource.type", string="Type", required="True", help="Type this profiles applies to.")                        
    profile_id = fields.Many2one(comodel_name="hc.res.structure.definition", string="Profile", required="True", help="Profile that all resources must conform to.")                        

class ImplementationGuidePage(models.Model):    
    _name = "hc.implementation.guide.page"    
    _description = "Implementation Guide Page"                

    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Page.")                        
    source = fields.Char(string="Source", required="True", help="Where to find that page.")                        
    title = fields.Char( required="True", help="Short title shown for navigational assistance.")                        
    kind = fields.Selection(string="Kind", required="True", selection=[("page", "Page"), ("example", "Example"), ("list", "List"), ("include", "Include"), ("directory | dictionary | toc | resource", "Directory | Dictionary | Toc | Resource")], help="The kind of page that this is. Some pages are autogenerated (list, example), and other kinds are of interest so that tools can navigate the user to the page of interest.")                        
    type_ids = fields.Many2many(comodel_name="hc.vs.resource.type", relation="implementation_guide_page_type_rel", string="Types", help="Kind of resource to include in the list.")                        
    package_ids = fields.One2many(comodel_name="hc.implementation.guide.page.package", inverse_name="page_id", string="Packages", help="Name of package to include.")                        
    format_id = fields.Many2one(comodel_name="hc.vs.mime.type", string="Format", help="Format of the page (e.g. html, markdown, etc.).")                        
    page_ids = fields.One2many(comodel_name="hc.implementation.guide.page", inverse_name="page_id", string="Pages", help="Nested Pages / Sections.")                        

class ImplementationGuideContact(models.Model):    
    _name = "hc.implementation.guide.contact"    
    _description = "Implementation Guide Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(comodel_name="hc.contact.detail", string="Contact", ondelete="restrict", required="True", help="Contact Detail associated with this Implementation Guide Contact.")                        
    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Contact.")                        

class ImplementationGuideUseContext(models.Model):    
    _name = "hc.implementation.guide.use.context"    
    _description = "Implementation Guide Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Use Context.")                        

class ImplementationGuideBinary(models.Model):    
    _name = "hc.implementation.guide.binary"    
    _description = "Implementation Guide Binary"            
    _inherit = ["hc.basic.association"]    

    implementation_guide_id = fields.Many2one(comodel_name="hc.res.implementation.guide", string="Implementation Guide", help="Implementation Guide associated with this Implementation Guide Binary.")                        
    binary = fields.Char(string="Binary URL", help="Image, css, script, etc..")                        

class ImplementationGuidePagePackage(models.Model):    
    _name = "hc.implementation.guide.page.package"    
    _description = "Implementation Guide Page Package"            
    _inherit = ["hc.basic.association"]    

    page_id = fields.Many2one(comodel_name="hc.implementation.guide.page", string="Page", help="Page associated with this Implementation Guide Page Package.")                        
    package = fields.Char(string="Package", help="Name of package to include.")                        
