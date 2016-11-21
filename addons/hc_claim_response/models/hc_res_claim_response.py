# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ClaimResponse(models.Model):    
    _name = "hc.res.claim.response"    
    _description = "Claim Response"        

    identifier_ids = fields.One2many(
        comodel_name="hc.claim.response.identifier", 
        inverse_name="claim_response_id", 
        string="Identifiers", 
        help="Response number.")                
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the resource instance.")                
    request_id = fields.Many2one(
        comodel_name="hc.res.claim", 
        string="Request", 
        help="Id of resource triggering adjudication.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Ruleset", 
        help="Resource version.")                
    original_ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Original Ruleset", 
        help="Original version.")                
    created = fields.Datetime(
        string="Created Date", 
        help="Creation date.")                
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Insurer.")                
    request_provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Request Provider", 
        help="Responsible practitioner.")                
    request_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Request Organization", 
        help="Responsible organization.")                
    outcome = fields.Selection(
        string="Claim Response Outcome", 
        selection=[
            ("complete", "Complete"), 
            ("error", "Error")], 
        help="Transaction status: error, complete.")                
    disposition = fields.Char(
        string="Disposition", 
        help="Disposition Message.")                
    payee_type_id = fields.Many2one(
        comodel_name="hc.vs.payee.type", 
        string="Payee Type", 
        help="Party to be paid any benefits payable.")                
    total_cost = fields.Float(
        string="Total Cost", 
        help="Total Cost of service from the Claim.")                
    unallocated_deductable = fields.Float(
        string="Unallocated Deductable", 
        help="Unallocated deductable.")                
    total_benefit = fields.Float(
        string="Total Benefit", 
        help="Total benefit payable for the Claim.")                
    reserved_id = fields.Many2one(
        comodel_name="hc.vs.funds.reserve", 
        string="Reserved", 
        help="Funds reserved status.")                
    form_id = fields.Many2one(
        comodel_name="hc.vs.forms", 
        string="Form", 
        help="Printed Form Identifier.")                
    error_ids = fields.One2many(
        comodel_name="hc.claim.response.error", 
        inverse_name="claim_response_id", 
        string="Error", 
        help="Processing errors.")                
    note_ids = fields.One2many(
        comodel_name="hc.claim.response.note", 
        inverse_name="claim_response_id", 
        string="Note", 
        help="Processing notes.")                
    item_ids = fields.One2many(
        comodel_name="hc.claim.response.item", 
        inverse_name="claim_response_id", 
        string="Item", 
        help="Line items.")                
    added_item_ids = fields.One2many(
        comodel_name="hc.claim.response.added.item", 
        inverse_name="claim_response_id", 
        string="Added Item", 
        help="Insurer added line items.")                
    payment_id = fields.Many2one(
        comodel_name="hc.claim.response.payment", 
        string="Payment", 
        help="Payment details, if paid.")                
    coverage_ids = fields.One2many(
        comodel_name="hc.claim.response.coverage", 
        inverse_name="claim_response_id", 
        string="Coverage", 
        help="Insurance or medical plan.")                

class ClaimResponseItem(models.Model):    
    _name = "hc.claim.response.item"    
    _description = "Claim Response Item"        

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Item.")                
    sequence_link_id = fields.Integer(
        string="Sequence Link Id", 
        required="True", 
        help="Service instance.")                
    note_number_ids = fields.One2many(
        comodel_name="hc.claim.response.item.note.number", 
        inverse_name="item_id", 
        string="Note Numbers", 
        help="List of note numbers which apply.")                
    adjudication_ids = fields.One2many(
        comodel_name="hc.claim.response.item.adjudication", 
        inverse_name="item_id", 
        string="Adjudication", 
        help="Adjudication details.")                
    detail_ids = fields.One2many(
        comodel_name="hc.claim.response.item.detail", 
        inverse_name="item_id", 
        string="Detail", 
        help="Detail line items.")                

class ClaimResponseItemAdjudication(models.Model):    
    _name = "hc.claim.response.item.adjudication"    
    _description = "Claim Response Item Adjudication"        

    item_id = fields.Many2one(
        comodel_name="hc.claim.response.item", 
        string="Item", 
        help="Item associated with this Claim Response Item Adjudication.")                
    detail_id = fields.Many2one(
        comodel_name="hc.claim.response.item.detail", 
        string="Detail", 
        help="Detail associated with this Claim Response Item Adjudication.")                
    sub_detail_id = fields.Many2one(
        comodel_name="hc.claim.response.item.detail.sub.detail", 
        string="Sub Detail", 
        help="Sub Detail associated with this Claim Response Item Adjudication.")                
    added_item_id = fields.Many2one(
        comodel_name="hc.claim.response.added.item", 
        string="Added Item", 
        help="Added Item associated with this Claim Response Item Adjudication.")                
    added_items_detail_id = fields.Many2one(
        comodel_name="hc.claim.response.added.items.detail", 
        string="Added Item Detail", 
        help="Added Item Detail associated with this Claim Response Item Adjudication.")               
    category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.sub.category", 
        string="Category", 
        required="True", 
        help="Adjudication category such as co-pay, eligible, benefit, etc..")                
    reason_id = fields.Many2one(
        comodel_name="hc.vs.adjudication.reason", 
        string="Reason", 
        help="Coding who is adjudication reason.")                
    amount = fields.Float(
        string="Amount", 
        help="Monetary amount.")                
    value = fields.Float(
        string="Non-Monetary Value", 
        help="Non-monitory value.")                

class ClaimResponseItemDetail(models.Model):    
    _name = "hc.claim.response.item.detail"    
    _description = "Claim Response Item Detail"        

    item_id = fields.Many2one(
        comodel_name="hc.claim.response.item", 
        string="Item", 
        help="Item associated with this Claim Response Item Detail.")                
    sequence_link_id = fields.Integer(
        string="Sequence Link Id", 
        required="True", 
        help="Service instance.")                
    note_number_ids = fields.One2many(
        comodel_name="hc.claim.response.item.detail.note.number", 
        inverse_name="detail_id", 
        string="Note Numbers", 
        help="List of note numbers which apply.")                
    adjudication_ids = fields.One2many(
        comodel_name="hc.claim.response.item.adjudication", 
        inverse_name="detail_id", 
        string="Adjudication", 
        help="Detail adjudication.")                
    sub_detail_ids = fields.One2many(
        comodel_name="hc.claim.response.item.detail.sub.detail", 
        inverse_name="detail_id", 
        string="Sub Detail", 
        help="Sub detail line items.")                

class ClaimResponseItemDetailSubDetail(models.Model):    
    _name = "hc.claim.response.item.detail.sub.detail"    
    _description = "Claim Response Item Detail Sub Detail"        

    detail_id = fields.Many2one(
        comodel_name="hc.claim.response.item.detail", 
        string="Detail", 
        help="Detail associated with this Claim Response Item Detail Sub Detail.")                
    sequence_link_id = fields.Integer(
        string="Sequence Link Id", 
        required="True", 
        help="Service instance.")                
    note_number_ids = fields.One2many(
        comodel_name="hc.claim.response.item.detail.sub.detail.note.number", 
        inverse_name="sub_detail_id", 
        string="Note Numbers", 
        help="List of note numbers which apply.")                
    adjudication_ids = fields.One2many(
        comodel_name="hc.claim.response.item.adjudication", 
        inverse_name="sub_detail_id", 
        string="Adjudication", 
        help="Subdetail adjudication.")                

class ClaimResponseAddedItem(models.Model):    
    _name = "hc.claim.response.added.item"    
    _description = "Claim Response Added Item"        

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Added Item.")                
    sequence_link_id_ids = fields.One2many(
        comodel_name="hc.claim.response.added.item.sequence.link.id", 
        inverse_name="added_item_id", 
        string="Sequence Link Ids", 
        help="Service instances.")                
    revenue_id = fields.Many2one(
        comodel_name="hc.vs.ex.revenue.center", 
        string="Revenue", 
        help="Revenue or cost center code.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.sub.category", 
        string="Category", 
        help="Type of service or product.")                
    service_id = fields.Many2one(
        comodel_name="hc.vs.service.uscls", 
        string="Service", 
        required="True", 
        help="Group, Service or Product.")                
    modifier_ids = fields.Many2many(
        comodel_name="hc.vs.claim.modifier", 
        relation="claim_response_added_item_modifier_rel", 
        string="Modifiers", 
        help="Service/Product billing modifiers.")                
    fee = fields.Float(
        string="Fee", 
        help="Professional fee or Product charge.")                
    note_number_ids = fields.One2many(
        comodel_name="hc.claim.response.added.item.note.number", 
        inverse_name="added_item_id", 
        string="Note Numbers", 
        help="List of note numbers which apply.")                
    adjudication_ids = fields.One2many(
        comodel_name="hc.claim.response.item.adjudication", 
        inverse_name="added_item_id", 
        string="Adjudication", 
        help="Added items adjudication.")        
    detail_ids = fields.One2many(
        comodel_name="hc.claim.response.added.items.detail", 
        inverse_name="added_item_id", 
        string="Detail", 
        help="Added items details.")                

class ClaimResponseAddedItemsDetail(models.Model):    
    _name = "hc.claim.response.added.items.detail"    
    _description = "Claim Response Added Items Detail"        

    added_item_id = fields.Many2one(
        comodel_name="hc.claim.response.added.item", 
        string="Added Item", 
        help="Added Item associated with this Claim Response Added Items Detail.")                
    revenue_id = fields.Many2one(
        comodel_name="hc.vs.ex.revenue.center", 
        string="Revenue", 
        help="Revenue or cost center code.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.sub.category", 
        string="Category", 
        help="Type of service or product.")                
    service_id = fields.Many2one(
        comodel_name="hc.vs.service.uscls", 
        string="Service", 
        required="True", 
        help="Group, Service or Product.")                
    modifier_ids = fields.Many2many(
        comodel_name="hc.vs.claim.modifier", 
        relation="claim_response_added_items_detail_modifier_rel", 
        string="Modifiers", 
        help="Service/Product billing modifiers.")                
    fee = fields.Float(
        string="Fee", 
        help="Professional fee or Product charge.")                
    note_number_ids = fields.One2many(
        comodel_name="hc.claim.response.added.items.detail.note.number", 
        inverse_name="added_items_detail_id", 
        string="Note Numbers", 
        help="List of note numbers which apply.")                
    adjudication_ids = fields.One2many(
        comodel_name="hc.claim.response.item.adjudication", 
        inverse_name="added_items_detail_id", 
        string="Adjudication", 
        help=" Added items detail adjudication.")                

class ClaimResponseError(models.Model):    
    _name = "hc.claim.response.error"    
    _description = "Claim Response Error"        

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Error.")                
    sequence_link_id = fields.Integer(
        string="Sequence Link Id", 
        help="Item sequence number.")                
    detail_sequence_link_id = fields.Integer(
        string="Detail Sequence Link Id", 
        help="Detail sequence number.")                
    sub_detail_sequence_link_id = fields.Integer(
        string="Sub Detail Sequence Link Id", 
        help="Subdetail sequence number.")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.adjudication.error", 
        string="Code", 
        required="True", 
        help="Error code detailing processing issues.")                

class ClaimResponsePayment(models.Model):    
    _name = "hc.claim.response.payment"    
    _description = "Claim Response Payment"        

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Payment.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.ex.payment.type", 
        string="Type", 
        help="Partial or Complete.")                
    adjustment = fields.Float(
        string="Adjustment", 
        help="Payment adjustment for non-Claim issues.")                
    adjustment_reason_id = fields.Many2one(
        comodel_name="hc.vs.payment.adjustment.reason", 
        string="Adjustment Reason", 
        help="Reason for Payment adjustment.")                
    date = fields.Date(
        string="Date", 
        help="Expected data of Payment.")                
    amount = fields.Float(
        string="Amount", 
        help="Payment amount.")                
    identifier_id = fields.Many2one(
        comodel_name="hc.claim.response.payment.identifier", 
        string="Identifier", 
        help="Payment identifier.")                

class ClaimResponseNote(models.Model):    
    _name = "hc.claim.response.note"    
    _description = "Claim Response Note"        

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Note.")                
    number = fields.Integer(
        string="Number", 
        help="Note Number for this note.")                
    type = fields.Selection(
        string="Note Type", 
        selection=[
            ("display", "Display"), 
            ("print", "Print"), 
            ("printoper", "Printoper")], 
        help="The note purpose: Print/Display.")                
    text = fields.Text(
        string="Text", 
        help="Note explanatory text.")                

class ClaimResponseCoverage(models.Model):    
    _name = "hc.claim.response.coverage"    
    _description = "Claim Response Coverage"        

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Coverage.")                
    sequence = fields.Integer(
        string="Sequence", 
        required="True", 
        help="Service instance identifier.")                
    is_focal = fields.Boolean(
        string="Focal", 
        required="True", 
        help="Is the focal Coverage.")                
    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        required="True", 
        help="Insurance information.")                
    business_arrangement = fields.Char(
        string="Business Arrangement", 
        help="Business agreement.")                
    pre_auth_ref_ids = fields.One2many(
        comodel_name="hc.claim.response.coverage.pre.auth.ref", 
        inverse_name="coverage_id", 
        string="Pre Auth Refs", 
        help="Pre-Authorization/Determination Reference.")                
    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Adjudication results.")                

class ClaimResponseIdentifier(models.Model):    
    _name = "hc.claim.response.identifier"    
    _description = "Claim Response Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Claim Response associated with this Claim Response Identifier.")                

class ClaimResponseItemNoteNumber(models.Model):    
    _name = "hc.claim.response.item.note.number"    
    _description = "Claim Response Item Note Number"        
    _inherit = ["hc.basic.association"]

    item_id = fields.Many2one(
        comodel_name="hc.claim.response.item", 
        string="Item", 
        help="Item associated with this Claim Response Item Note Number.")                
    note_number = fields.Integer(
        string="Note Number", 
        help="Note Number associated with this Claim Response Item Note Number.")                

class ClaimResponseItemDetailNoteNumber(models.Model):    
    _name = "hc.claim.response.item.detail.note.number"    
    _description = "Claim Response Item Detail Note Number"        
    _inherit = ["hc.basic.association"]

    detail_id = fields.Many2one(
        comodel_name="hc.claim.response.item.detail", 
        string="Detail", 
        help="Detail associated with this Claim Response Item Detail Note Number.")                
    note_number = fields.Integer(
        string="Note Number", 
        help="Note Number associated with this Claim Response Item Detail Note Number.")                

class ClaimResponseItemDetailSubDetailNoteNumber(models.Model):    
    _name = "hc.claim.response.item.detail.sub.detail.note.number"    
    _description = "Claim Response Item Detail Sub Detail Note Number"        
    _inherit = ["hc.basic.association"]

    sub_detail_id = fields.Many2one(
        comodel_name="hc.claim.response.item.detail.sub.detail", 
        string="Sub Detail", 
        help="Sub Detail associated with this Claim Response Item Detail Sub Detail Note Number.")                
    note_number = fields.Integer(
        string="Note Number", 
        help="Note Number associated with this Claim Response Item Detail Sub Detail Note Number.")                

class ClaimResponseAddedItemSequenceLinkId(models.Model):    
    _name = "hc.claim.response.added.item.sequence.link.id"    
    _description = "Claim Response Added Item Sequence Link Id"        
    _inherit = ["hc.basic.association"]

    added_item_id = fields.Many2one(
        comodel_name="hc.claim.response.added.item", 
        string="Added Item", 
        help="Added Item associated with this Claim Response Added Item Sequence Link Id.")                
    sequence_link_id = fields.Integer(
        string="Sequence Link Id", 
        help="Sequence Link Id associated with this Claim Response Added Item Sequence Link Id.")                

class ClaimResponseAddedItemNoteNumber(models.Model):    
    _name = "hc.claim.response.added.item.note.number"    
    _description = "Claim Response Added Item Note Number"        
    _inherit = ["hc.basic.association"]

    added_item_id = fields.Many2one(
        comodel_name="hc.claim.response.added.item", 
        string="Added Item", 
        help="Added Item associated with this Claim Response Added Item Note Number.")                
    note_number = fields.Integer(
        string="Note Number", 
        help="Note Number associated with this Claim Response Added Item Note Number.")                

class ClaimResponseAddedItemsDetailNoteNumber(models.Model):    
    _name = "hc.claim.response.added.items.detail.note.number"    
    _description = "Claim Response Added Items Detail Note Number"        
    _inherit = ["hc.basic.association"]

    added_items_detail_id = fields.Many2one(
        comodel_name="hc.claim.response.added.items.detail", 
        string="Added Item Detail", 
        help="Added Item Detail associated with this Claim Response Added Items Detail Note Number.")                
    note_number = fields.Integer(
        string="Note Number", 
        help="Note Number associated with this Claim Response Added Items Detail Note Number.")                

class ClaimResponseCoveragePreAuthRef(models.Model):    
    _name = "hc.claim.response.coverage.pre.auth.ref"    
    _description = "Claim Response Coverage Pre Auth Ref"        
    _inherit = ["hc.basic.association"]

    coverage_id = fields.Many2one(
        comodel_name="hc.claim.response.coverage", 
        string="Coverage", 
        help="Coverage associated with this Claim Response Coverage Pre Auth Ref.")                
    pre_auth_ref = fields.Char(
        string="Pre Auth Ref", 
        help="Pre Auth Ref associated with this Claim Response Coverage Pre Auth Ref.")                

class ClaimResponsePaymentIdentifier(models.Model):    
    _name = "hc.claim.response.payment.identifier"    
    _description = "Claim Response Payment Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class PaymentAdjustmentReason(models.Model):    
    _name = "hc.vs.payment.adjustment.reason"    
    _description = "Payment Adjustment Reason"        
    _inherit = ["hc.value.set.contains"]

class AdjudicationReason(models.Model): 
    _name = "hc.vs.adjudication.reason" 
    _description = "Adjudication Reason"        
    _inherit = ["hc.value.set.contains"]

class AdjudicationError(models.Model):  
    _name = "hc.vs.adjudication.error"  
    _description = "Adjudication Error"     
    _inherit = ["hc.value.set.contains"]

class ExPaymentType(models.Model):  
    _name = "hc.vs.ex.payment.type" 
    _description = "Ex Payment Type"        
    _inherit = ["hc.value.set.contains"]

# External Reference

class ClaimCoverage(models.Model):    
    _inherit = "hc.claim.coverage"

    claim_response_id = fields.Many2one(
        comodel_name="hc.res.claim.response", 
        string="Claim Response", 
        help="Adjudication results.") 