# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SupplyDelivery(models.Model):    
    _name = "hc.res.supply.delivery"    
    _description = "Supply Delivery"        

    identifier_id = fields.Many2one(
        comodel_name="hc.supply.delivery.identifier", 
        string="Identifier", 
        help="External identifier.")                
    status = fields.Selection(
        string="Supply Delivery Status", 
        selection=[
            ("in-progress", "In-Progress"), 
            ("completed", "Completed"), 
            ("abandoned", "Abandoned")], 
        help="A code specifying the state of the dispense event.")                
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient for whom the item is supplied.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.supply.delivery.type", 
        string="Type", 
        help="Category of dispense event.")                
    quantity = fields.Float(
        string="Quantity", 
        help="Amount dispensed.")                
    quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Quantity UOM", 
        help="Quantity unit of measure.")                
    supplied_item_type = fields.Selection(
        string="Supplied Item Type", 
        selection=[
            ("code", "Code"), 
            ("Medication", "Medication"), 
            ("Substance", "Substance"), 
            ("Device", "Device")], 
        help="Type of medication, substance, or device supplied.")                
    supplied_item_name = fields.Char(
        string="Supplied Item Name", 
        compute="_compute_supplied_item_name", 
        store="True", 
        help="Medication, Substance, or Device supplied.")                
    supplied_item_code_id = fields.Many2one(
        comodel_name="hc.vs.supply.item", 
        string="Supplied Item Code", 
        help="Code of supplied item.")                
    supplied_item_medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Supplied Item Medication", 
        help="Medication supplied.")                
    supplied_item_substance_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Supplied Item Substance", 
        help="Substance supplied.")                
    supplied_item_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Supplied Item Device", 
        help="Device supplied.")                
    supplier_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Supplier", 
        help="Dispenser.")                
    when_prepared_start_date = fields.Datetime(
        string="When Prepared Start Date", 
        help="Start of the dispensing time.")                
    when_prepared_end_date = fields.Datetime(
        string="When Prepared End Date", 
        help="End of the dispensing time.")                
    handover_time = fields.Datetime(
        string="Handover time", 
        help="Handover time.")                
    destination_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Destination", 
        help="Where the Supply was sent.")                
    receiver_ids = fields.One2many(
        comodel_name="hc.supply.delivery.receiver", 
        inverse_name="supply_delivery_id", 
        string="Receivers", 
        help="Who collected the Supply.")                

class SupplyDeliveryIdentifier(models.Model):    
    _name = "hc.supply.delivery.identifier"    
    _description = "Supply Delivery Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class SupplyDeliveryReceiver(models.Model):    
    _name = "hc.supply.delivery.receiver"    
    _description = "Supply Delivery Receiver"        
    _inherit = ["hc.basic.association"]

    supply_delivery_id = fields.Many2one(
        comodel_name="hc.res.supply.delivery", 
        string="Supply Delivery", 
        help="Supply Delivery associated with this Supply Delivery Receiver.")                
    receiver_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Receiver", 
        help="Practitioner associated with this Supply Delivery Receiver.")                

class SupplyDeliveryType(models.Model):    
    _name = "hc.vs.supply.delivery.type"    
    _description = "Supply Delivery Type"        
    _inherit = ["hc.value.set.contains"]
