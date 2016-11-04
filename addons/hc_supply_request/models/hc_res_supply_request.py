# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SupplyRequest(models.Model):    
    _name = "hc.res.supply.request"    
    _description = "Supply Request"        

    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", help="Patient for whom the item is supplied.")                
    source_type = fields.Selection(string="Source Type", selection=[("Practitioner", "Practitioner"), ("Organization", "Organization"), ("Patient", "Patient")], help="Type of who initiated this order.")                
    source_name = fields.Char(string="Source", compute="_compute_source_name", store="True", help="Who initiated this order.")                
    source_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Source Practitioner", help="Practitioner who initiated this order.")                
    source_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Source Organization", help="Organization who initiated this order.")                
    source_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Source Patient", help="Patient who initiated this order.")                
    date = fields.Datetime(string="Date", help="the request was made.")                
    identifier_id = fields.Many2one(comodel_name="hc.supply.request.identifier", string="Identifier", help="Unique identifier.")                
    status = fields.Selection(string="Status", selection=[("requested", "Requested"), ("completed", "Completed"), ("failed", "Failed"), ("cancelled", "Cancelled")], help="Status of the supply request.")                
    kind_id = fields.Many2one(comodel_name="hc.vs.supply.request.kind", string="Kind", help="The kind of supply (central, non-stock, etc).")                
    ordered_type = fields.Selection(string="Ordered Type", selection=[("code", "Code"), ("Medication", "Medication"), ("Substance", "Substance"), ("Device", "Device")], help="Type of medication, substance, or device requested to be supplied.")                
    ordered_item_name = fields.Char(string="Ordered Item Name", compute="_compute_ordered_item_name", store="True", help="code|Medication|Substance|Device.")                
    ordered_item_code_id = fields.Many2one(comodel_name="hc.vs.supply.item", string="Ordered Item Code", help="Code of item requested to be supplied.")                
    ordered_item_medication_id = fields.Many2one(comodel_name="hc.res.medication", string="Ordered Item Medication", help="Medication requested to be supplied.")                
    ordered_item_substance_id = fields.Many2one(comodel_name="hc.res.substance", string="Ordered Item Substance", help="Substance requested to be supplied.")                
    ordered_item_device_id = fields.Many2one(comodel_name="hc.res.device", string="Ordered Item Device", help="Device requested to be supplied.")                
    supplier_ids = fields.One2many(comodel_name="hc.supply.request.supplier", inverse_name="supply_request_id", string="Suppliers", help="Who is intended to fulfill the request.")                
    reason_type = fields.Selection(string="Reason Type", selection=[("code", "Code"), ("string", "String")], help="Type of why the supply item was requested.")                
    reason_name = fields.Char(string="Reason Name", compute="_compute_reason_name", store="True", help="Why the supply item was requested.")                
    reason_code_id = fields.Many2one(comodel_name="hc.vs.supply.request.reason", string="Reason Code", help="CodeableConcept why the supply item was requested.")                
    reason_string = fields.Text(string="Reason", help="String of why the supply item was requested.")                
    when_ids = fields.One2many(comodel_name="hc.supply.request.when", inverse_name="supply_request_id", string="Whens", help="When the request should be fulfilled.")                

class SupplyRequestWhen(models.Model):    
    _name = "hc.supply.request.when"    
    _description = "Supply Request When"        

    supply_request_id = fields.Many2one(comodel_name="hc.res.supply.request", string="Supply Request", help="Supply Request associated with this Supply Request When.")                
    code_id = fields.Many2one(comodel_name="hc.vs.supply.request.when", string="Code", help="Fulfilment code." )                
    schedule_id = fields.Many2one(comodel_name="hc.supply.request.when.schedule", string="Schedule", help="Formal fulfillment schedule.")                

class SupplyRequestIdentifier(models.Model):    
    _name = "hc.supply.request.identifier"    
    _description = "Supply Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class SupplyRequestWhenSchedule(models.Model):  
    _name = "hc.supply.request.when.schedule"   
    _description = "Supply Request When Schedule"       
    _inherit = ["hc.basic.association", "hc.timing"]

class SupplyRequestSupplier(models.Model):    
    _name = "hc.supply.request.supplier"    
    _description = "Supply Request Supplier"        
    _inherit = ["hc.basic.association"]

    supply_request_id = fields.Many2one(comodel_name="hc.res.supply.request", string="Supply Request", help="Supply Request associated with this Supply Request Supplier.")                
    supplier_id = fields.Many2one(comodel_name="hc.res.organization", string="Supplier", help="Organization associated with this Supply Request Supplier.")                

class SupplyRequestKind(models.Model):    
    _name = "hc.vs.supply.request.kind"    
    _description = "Supply Request Kind"        
    _inherit = ["hc.value.set.contains"]

class SupplyItem(models.Model):    
    _name = "hc.vs.supply.item"    
    _description = "Supply Item"        
    _inherit = ["hc.value.set.contains"]

class SupplyRequestReason(models.Model):    
    _name = "hc.vs.supply.request.reason"    
    _description = "Supply Request Reason"        
    _inherit = ["hc.value.set.contains"]

class SupplyRequestWhen(models.Model):  
    _name = "hc.vs.supply.request.when" 
    _description = "Supply Request When"        
    _inherit = ["hc.value.set.contains"]
