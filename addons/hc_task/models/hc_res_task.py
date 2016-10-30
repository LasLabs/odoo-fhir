# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Task(models.Model):    
    _name = "hc.res.task"    
    _description = "Task"        

    identifier_id = fields.Many2one(comodel_name="hc.task.identifier", string="Identifier", help="Task Instance Identifier.")                
    based_on_ids = fields.One2many(comodel_name="hc.task.based.on", inverse_name="task_id", string="Based Ons", help="Request fulfilled by this request.")                
    requisition_id = fields.Many2one(comodel_name="hc.task.requisition", string="Requisition", help="Composite request this is part of.")                
    parent_ids = fields.One2many(comodel_name="hc.task.parent", inverse_name="task_id", string="Parents", help="Composite task.")                
    status = fields.Selection(string="Task Status", required="True", selection=[("draft", "Draft"), ("requested", "Requested"), ("received", "Received"), ("accepted", "Accepted"), ("+", "+")], help="The current status of the task.")                
    status_reason_id = fields.Many2one(comodel_name="hc.vs.task.status.reason", string="Status Reason", help="Reason for current status.")                
    business_status_id = fields.Many2one(comodel_name="hc.vs.task.business.status", string="Business Status", help="E.g. Specimen collected, IV prepped.")                
    stage_id = fields.Many2one(comodel_name="hc.vs.task.stage", string="Stage", required="True", 
        help='Indicates the "level" of actionability associated with the Task. I.e. Is this a proposed task, a planned task, an actionable task, etc.')                
    code_id = fields.Many2one(comodel_name="hc.vs.task.type", string="Code", help="A name or code (or both) briefly describing what the task involves..")                
    priority = fields.Selection(string="Task Priority", selection=[("low", "Low"), ("normal", "Normal"), ("high", "High")], help="The priority of the task among other tasks of the same type.")                
    description = fields.Text( help="Task Description.")                
    focus_id = fields.Many2one(comodel_name="hc.task.focus", string="Focus", help="What task is acting on.")
    for_id = fields.Many2one(comodel_name="hc.task.for", string="For", help="Beneficiary of the Task.")            
    context_type = fields.Selection(string="Context Type", selection=[("Encounter", "Encounter"), ("Episode of Care", "Episode Of Care")], help="Type of supplemental instruction.")                
    context_name = fields.Char(string="Context", compute="_compute_context_name", store="True", help="Healthcare event during which this task originated .")                
    created = fields.Datetime(string="Created", required="True", help="Task Creation Date.")                
    last_modified = fields.Datetime(string="Last Modified", required="True", help="Task Last Modified Date.")                
    requester_type = fields.Selection(string="Requester Type", required="True", selection=[("Device", "Device"), ("Organization", "Organization"), ("Patient", "Patient"), ("Practitioner", "Practitioner"), ("Related Person", "Related Person")], help="Type of task creator.")                
    requester_name = fields.Char(string="Requester", compute="_compute_requester_name", store="True", help="Task Creator .")                
    owner_type = fields.Selection(string="Owner Type", selection=[("Device", "Device"), ("Organization", "Organization"), ("Patient", "Patient"), ("Practitioner", "Practitioner"), ("Related Person", "Related Person")], help="Type of task owner.")                
    owner_name = fields.Char(string="Owner", compute="_compute_owner_name", store="True", help="Task Owner .")                
    performer_type_ids = fields.Many2many(comodel_name="hc.vs.task.performer.type", string="Performer Types", help="The type of participant that can execute the task.")                
    reason_id = fields.Many2one(comodel_name="hc.vs.task.reason", string="Reason", help="Why task is needed.")                
    note_ids = fields.One2many(comodel_name="hc.task.note", inverse_name="task_id", string="Notes", help="Comments made about the task.")                
    fulfillment_ids = fields.One2many(comodel_name="hc.task.fulfillment", inverse_name="task_id", string="Fulfillments", help="Constraints on fulfillment tasks.")                
    input_ids = fields.One2many(comodel_name="hc.task.input", inverse_name="task_id", string="Inputs", help="Task Input.")                
    output_ids = fields.One2many(comodel_name="hc.task.output", inverse_name="task_id", string="Outputs", help="Task Output.")                

class TaskFulfillment(models.Model):    
    _name = "hc.task.fulfillment"   
    _description = "Task Fulfillment"       

    task_id = fields.Many2one(comodel_name="hc.res.task", string="Task", help="Task associated with this fulfillment." )                
    repetitions = fields.Integer( help="How many times to repeat.")             
    period_start_date = fields.Datetime(string="Scheduled Start Date", help="Start of time period when fulfillment is sought.")             
    period_end_date = fields.Datetime(string="Scheduled End Date", help="End of time period when fulfillment is sought.")               
    recipient_ids = fields.One2many(comodel_name="hc.task.fulfillment.recipient", inverse_name="fulfillment_id", string="Recipients", help="For whom is fulfillment sought?")              
    definition_uri = fields.Char(string="Definition URL", help="Task Definition.")              

class TaskInput(models.Model):  
    _name = "hc.task.input" 
    _description = "Task Input"     

    task_id = fields.Many2one(comodel_name="hc.res.task", string="Task", help="Task associated with this input." )              
    name = fields.Char( required="True", help="Input Name.")                
    value_type = fields.Selection(string="Value Type", required="True", selection=[("string", "String"), ("decimal", "Decimal")], help="Type of input value.")              
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="Input Value .")             
    value_string = fields.Char(string="Value String", help="String input value.")               
    value_decimal = fields.Float(string="Value Decimal", help="Decimal input value.")               
    value_code_id = fields.Many2one(comodel_name="hc.vs.task.input.type", string="Value Code", help="Code input value." )               

class TaskOutput(models.Model): 
    _name = "hc.task.output"    
    _description = "Task Output"        

    task_id = fields.Many2one(comodel_name="hc.res.task", string="Task", help="Task associated with this output." )             
    name = fields.Char( required="True", help="Output Name.")               
    value_type = fields.Selection(string="Value Type", required="True", selection=[("string", "String"), ("decimal", "Decimal")], help="Type of output value.")             
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="Output Value .")                
    value_string = fields.Char(string="Value String", help="String output value.")              
    value_decimal = fields.Float(string="Value Decimal", help="Decimal output value.")              
    value_code_id = fields.Many2one(comodel_name="hc.vs.task.output.type", string="Value Code", help="Code output value." )             

class TaskBasedOn(models.Model):    
    _name = "hc.task.based.on"  
    _description = "Task Based On"      
    _inherit = ["hc.basic.association"]

    task_id = fields.Many2one(comodel_name="hc.res.task", string="Task", help="Task associated with this Task Based On." )              
    based_on_type = fields.Selection(string="Based On Type", selection=[("string", "String"), ("Diagnostic Request", "Diagnostic Request")], help="Type of request fulfilled by this request.")             
    based_on_name = fields.Char(string="Based On", compute="_compute_based_on_name", store="True", help="Request fulfilled by this request .")              
    based_on_string = fields.Char(string="Based On String", help="String request fulfilled by this request.")               
    based_on_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Based On Diagnostic Request", help="Diagnostic Request request fulfilled by this request." )             

class TaskFocus(models.Model):  
    _name = "hc.task.focus" 
    _description = "Task Focus"     
    _inherit = ["hc.basic.association"]

    focus_type = fields.Selection(string="Focus Type", selection=[("string", "String"), ("Diagnostic Request", "Diagnostic Request")], help="Type of what task is acting on.")              
    focus_name = fields.Char(string="Focus", compute="_compute_focus_name", store="True", help="What task is acting on.")               
    focus_string = fields.Char(string="Focus String", help="String what task is acting on.")                
    focus_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Focus Diagnostic Request", help="Diagnostic Request what task is acting on." )              

class TaskFor(models.Model):    
    _name = "hc.task.for"   
    _description = "Task For"       
    _inherit = ["hc.basic.association"]

    for_type = fields.Selection(string="For Type", selection=[("string", "String"), ("Patient", "Patient")], help="Type of beneficiary of the task.")               
    for_name = fields.Char(string="For", compute="_compute_for_name", store="True", help="Beneficiary of the Task .")               
    for_string = fields.Char(string="For String", help="String beneficiary of the task.")               
    for_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="For Patient", help="Patient beneficiary of the task." )             

class TaskFulfillmentRecipient(models.Model):   
    _name = "hc.task.fulfillment.recipient" 
    _description = "Task Fulfillment Recipient"     
    _inherit = ["hc.basic.association"]

    fulfillment_id = fields.Many2one(comodel_name="hc.task.fulfillment", string="Fulfillment", help="Fulfillment associated with this Task Fulfillment Recipient.")             
    recipient_type = fields.Selection(string="Recipient Type", selection=[("Patient", "Patient"), ("Practitioner", "Practitioner"), ("Related Person", "Related Person"), ("Group", "Group"), ("Organization", "Organization")], help="Type for whom is fulfillment sought.")               
    recipient_name = fields.Char(string="Recipient", compute="_compute_recipient_name", store="True", help="For whom is fulfillment sought? ")              
    recipient_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Recipient Patient", help="Patient for whom is fulfillment sought?")               
    recipient_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Recipient Organization", help="Organization for whom is fulfillment sought?")               
    recipient_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Recipient Patient", help="Patient for whom is fulfillment sought?")               
    recipient_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Recipient Practitioner", help="Practitioner for whom is fulfillment sought?")               
    recipient_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Recipient Related Person", help="Related Person for whom is fulfillment sought?")               

class TaskIdentifier(models.Model): 
    _name = "hc.task.identifier"    
    _description = "Task Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class TaskNote(models.Model):   
    _name = "hc.task.note"  
    _description = "Task Note"      
    _inherit = ["hc.basic.association", "hc.annotation"]

    task_id = fields.Many2one(comodel_name="hc.res.task", string="Task", help="Task associated with this Task Note." )              

class TaskParent(models.Model): 
    _name = "hc.task.parent"    
    _description = "Task Parent"        
    _inherit = ["hc.basic.association"]

    task_id = fields.Many2one(comodel_name="hc.res.task", string="Task", help="Task associated with this Task Parent." )                
    parent_id = fields.Many2one(comodel_name="hc.res.task", string="Parent", help="Composite task.")                

class TaskRequisition(models.Model):    
    _name = "hc.task.requisition"   
    _description = "Task Requisition"       
    _inherit = ["hc.basic.association", "hc.identifier"]

class TaskBusinessStatus(models.Model): 
    _name = "hc.vs.task.business.status"    
    _description = "Task Business Status"       
    _inherit = ["hc.value.set.contains"]

class TaskInputType(models.Model):  
    _name = "hc.vs.task.input.type" 
    _description = "Task Input Type"        
    _inherit = ["hc.value.set.contains"]

class TaskOutputType(models.Model): 
    _name = "hc.vs.task.output.type"    
    _description = "Task Output Type"       
    _inherit = ["hc.value.set.contains"]

class TaskPerformerType(models.Model):  
    _name = "hc.vs.task.performer.type" 
    _description = "Task Performer Type"        
    _inherit = ["hc.value.set.contains"]

class TaskPriority(models.Model):   
    _name = "hc.vs.task.priority"   
    _description = "Task Priority"      
    _inherit = ["hc.value.set.contains"]

class TaskReason(models.Model): 
    _name = "hc.vs.task.reason" 
    _description = "Task Reason"        
    _inherit = ["hc.value.set.contains"]

class TaskStage(models.Model):  
    _name = "hc.vs.task.stage"  
    _description = "Task Stage"     
    _inherit = ["hc.value.set.contains"]

class TaskStatus(models.Model): 
    _name = "hc.vs.task.status" 
    _description = "Task Status"        
    _inherit = ["hc.value.set.contains"]

class TaskStatusReason(models.Model):   
    _name = "hc.vs.task.status.reason"  
    _description = "Task Status Reason"     
    _inherit = ["hc.value.set.contains"]

class TaskType(models.Model):   
    _name = "hc.vs.task.type"   
    _description = "Task Type"      
    _inherit = ["hc.value.set.contains"]
