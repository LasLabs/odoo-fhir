# -*- coding: utf-8 -*-

from openerp import models, fields, api

class NutritionRequest(models.Model):    
    _name = "hc.res.nutrition.request"    
    _description = "Nutrition Request"        

    identifier_ids = fields.One2many(comodel_name="hc.nutr.req.identifier", inverse_name="nutrition_request_id", string="Identifiers", help="Identifiers assigned to this order.")                
    status = fields.Selection(string="Nutrition Request Status", selection=[("proposed", "Proposed"), ("draft", "Draft"), ("planned", "Planned"), ("requested", "Requested"), ("active", "Active"), ("on-hold", "On-Hold"), ("completed", "Completed"), ("cancelled", "Cancelled")], help="The workflow status of the nutrition order/request.")                
    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", required="True", help="The person who requires the diet, formula or nutritional supplement.")                
    encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Encounter", help="The encounter associated with that this nutrition order.")                
    date_time = fields.Datetime(string="Date Time", required="True", help="Date and time the nutrition order was requested.")                
    orderer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Orderer Practitioner", help="Who ordered the diet, formula or nutritional supplement.")                
    allergy_intolerance_ids = fields.One2many(comodel_name="hc.nutr.req.allergy.intolerance", inverse_name="nutrition_request_id", string="Allergy Intolerances", help="List of the patient's food and nutrition-related allergies and intolerances.")                
    food_preference_modifier_ids = fields.One2many(comodel_name="hc.nutr.req.food.pref.mod", inverse_name="nutrition_request_id", string="Food Preference Modifiers", help="Order-specific modifier about the type of food that should be given.")                
    exclude_food_modifier_ids = fields.One2many(comodel_name="hc.nutr.req.excl.food.mod", inverse_name="nutrition_request_id", string="Exclude Food Modifiers", help="Order-specific modifier about the type of food that should not be given.")                
    oral_diet_ids = fields.One2many(comodel_name="hc.nutr.req.oral.diet", inverse_name="nutrition_request_id", string="Oral Diets", help="Oral diet components.")                
    supplement_ids = fields.One2many(comodel_name="hc.nutr.req.suppl", inverse_name="nutrition_request_id", string="Supplements", help="Supplement components.")                
    enteral_formula_ids = fields.One2many(comodel_name="hc.nutr.req.ent.for", inverse_name="nutrition_request_id", string="Enteral Formulas", help="Enteral formula components.")                

class NutrReqOralDiet(models.Model):    
    _name = "hc.nutr.req.oral.diet"    
    _description = "Nutrition Request Oral Diet"        

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this oral diet.")                
    type_ids = fields.One2many(comodel_name="hc.nutr.req.oral.diet.type", inverse_name="oral_diet_id", string="Types", help="Type of oral diet or diet restrictions that describe what can be consumed orally.")                
    schedule_ids = fields.One2many(comodel_name="hc.nutr.req.oral.diet.sched", inverse_name="oral_diet_id", string="Schedules", help="Scheduled frequency of diet.")                
    fluid_consistency_type_ids = fields.One2many(comodel_name="hc.nutr.req.oral.diet.fluid.consistency", inverse_name="oral_diet_id", string="Fluid Consistency Types", help="The required consistency of fluids and liquids provided to the patient.")                
    instruction = fields.Text(string="Instruction", help="Instructions or additional information about the oral diet.")                
    nutrient_ids = fields.One2many(comodel_name="hc.nutr.req.oral.diet.nutrient", inverse_name="oral_diet_id", string="Nutrients", help="Required nutrient modifications.")                
    texture_ids = fields.One2many(comodel_name="hc.nutr.req.oral.diet.texture", inverse_name="oral_diet_id", string="Textures", help="Required texture modifications.")                

class NutrReqOralDietNutrient(models.Model):    
    _name = "hc.nutr.req.oral.diet.nutrient"    
    _description = "Nutrition Request Oral Diet Nutrient"        

    oral_diet_id = fields.Many2one(comodel_name="hc.nutr.req.oral.diet", string="Oral Diet", help="Oral Diet associated with this nutrient.")                
    modifier_id = fields.Many2one(comodel_name="hc.vs.nutrient.code", string="Modifier", help="Type of nutrient that is being modified.")                
    amount = fields.Float(string="Amount", help="Quantity of the specified nutrient.")                
    amount_uom_id = fields.Many2one(comodel_name="product.uom", string="Amount UOM", help="Amount unit of measure.")                

class NutrReqOralDietTexture(models.Model):    
    _name = "hc.nutr.req.oral.diet.texture"    
    _description = "Nutrition Request Oral Diet Texture"        

    oral_diet_id = fields.Many2one(comodel_name="hc.nutr.req.oral.diet", string="Oral Diet", help="Oral Diet associated with this texture.")                
    modifier_id = fields.Many2one(comodel_name="hc.vs.texture.code", string="Modifier", help="Code to indicate how to alter the texture of the foods, e.g., pureed.")                
    food_type_id = fields.Many2one(comodel_name="hc.vs.food.type", string="Food Type", help="Concepts that are used to identify an entity that is ingested for nutritional purposes.")                

class NutrReqSuppl(models.Model):    
    _name = "hc.nutr.req.suppl"    
    _description = "Nutrition Request Supplement"        

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this supplement.")                
    type_id = fields.Many2one(comodel_name="hc.vs.supplement.type", string="Type", help="Type of supplement product requested.")                
    product_name = fields.Char(string="Product Name", help="Product or brand name of the nutritional supplement.")                
    scheduled_ids = fields.One2many(comodel_name="hc.nutr.req.suppl.sched", inverse_name="supplement_id", string="Schedules", help="Scheduled frequency of supplement.")               
    quantity = fields.Float(string="Quantity", help="Amount of the nutritional supplement.")                
    quantity_uom_id = fields.Many2one(comodel_name="product.uom", string="Quantity UOM", help="Quantity unit of measure.")                
    instruction = fields.Text(string="Instruction", help="Instructions or additional information about the oral supplement.")                

class NutrReqEntFor(models.Model):    
    _name = "hc.nutr.req.ent.for"    
    _description = "Nutrition Request Enteral Formula"        

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this enteral formula.")                
    base_formula_type_id = fields.Many2one(comodel_name="hc.vs.ent.formula.type", string="Base Formula Type", help="Type of enteral or infant formula.")                
    base_formula_product_name = fields.Char(string="Base Formula Product Name", help="Product or brand name of the enteral or infant formula.")                
    additive_type_id = fields.Many2one(comodel_name="hc.vs.ent.formula.additive", string="Additive Type", help="Type of modular component to add to the feeding.")                
    additive_product_name = fields.Char(string="Additive Product Name", help="Product or brand name of the modular additive.")                
    caloric_density = fields.Float(string="Caloric Density", help="Amount of energy per specified volume that is required.")                
    caloric_density_uom_id = fields.Many2one(comodel_name="product.uom", string="Caloric Density UOM", help="Caloricdensity unit of measure.")                
    route_of_administration_id = fields.Many2one(comodel_name="hc.vs.enteral.route", string="Route Of Administration", help="How the formula should enter the patient's gastrointestinal tract.")                
    max_volume_to_deliver = fields.Float(string="Max Volume To Deliver", help="Upper limit on formula volume per unit of time.")                
    administration_instructions = fields.Text(string="Administration Instructions", help="Formula feeding instructions expressed as text.")                
    administration_ids = fields.One2many(comodel_name="hc.nutr.req.ent.for.admin", inverse_name="enteral_formula_id", string="Administrations", help="Formula feeding instruction as structured data.")                

class NutrReqEntForAdmin(models.Model):    
    _name = "hc.nutr.req.ent.for.admin"    
    _description = "Nutrition Request Enteral Formula Administration"        

    enteral_formula_id = fields.Many2one(comodel_name="hc.nutr.req.ent.for", string="Enteral Formula", help="Enteral Formula associated with this administration.")                
    schedule_ids = fields.One2many(comodel_name="hc.nutr.req.ent.for.admin.sched", inverse_name="administration_id", string="Schedules", help="Scheduled frequency of enteral feeding.")                
    quantity = fields.Float(string="Quantity", help="The volume of formula to provide.")                
    quantity_uom_id = fields.Many2one(comodel_name="product.uom", string="Quantity UOM", help="Quantity unit of measure.")                
    rate_type = fields.Selection(string="Rate Type", selection=[("Quantity", "Quantity"), ("Ratio", "Ratio")], help="Type of patient observations supporting recommendation.")                
    rate_name = fields.Char(string="Rate", compute="_compute_rate_name", store="True", help="Speed with which the formula is provided per period of time")                
    rate = fields.Float(string="Rate", help="Speed with which the formula is provided per period of time.")                
    rate_uom_id = fields.Many2one(comodel_name="product.uom", string="Rate UOM", help="Rate unit of measure.")                
    rate_adjustment_quantity = fields.Float(string="Rate Adjustment Quantity", help="Numerator value of change in the rate of administration over a given time.")                
    rate_adjustment_time = fields.Float(string="Rate Adjustment Time", help="Denominator value of change in the rate of administration over a given time.")                
    rate_adjustment = fields.Float(string="Rate Adjustment", compute="_compute_rate_adjustment", store="True", help="Change in the rate of administration over a given time.")                
    rate_adjustment_uom_id = fields.Many2one(comodel_name="product.uom", string="Rate Adjustment UOM", help="Change in the rate of administration over a given time unit of measure.")                

class NutrReqAllergyIntolerance(models.Model):    
    _name = "hc.nutr.req.allergy.intolerance"    
    _description = "Nutrition Request Allergy Intolerance"        
    _inherit = ["hc.basic.association"]

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this nutrition request nutrition request.")                
    allergy_intolerance_id = fields.Many2one(comodel_name="hc.res.allergy.intolerance", string="Allergy Intolerance", help="Allergy Intolerance associated with this nutrition request allergy intolerance.")                

class NutrReqIdentifier(models.Model):    
    _name = "hc.nutr.req.identifier"    
    _description = "Nutrition Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this nutrition request identifier.")                

class NutrReqOralDietSched(models.Model):    
    _name = "hc.nutr.req.oral.diet.sched"    
    _description = "Nutrition Request Oral Diet Schedule"        
    _inherit = ["hc.basic.association", "hc.timing"]

    oral_diet_id = fields.Many2one(comodel_name="hc.nutr.req.oral.diet", string="Oral Diet", help="Oral Diet associated with this nutrition request oral diet.")                

class NutrReqOralDietType(models.Model):    
    _name = "hc.nutr.req.oral.diet.type"    
    _description = "Nutrition Request Oral Diet Type"        
    _inherit = ["hc.basic.association"]

    oral_diet_id = fields.Many2one(comodel_name="hc.nutr.req.oral.diet", string="Oral Diet", help="Oral Diet associated with this nutrition request oral diet.")                
    type_id = fields.Many2one(comodel_name="hc.vs.diet.type", string="Type", help="Diet Type associated with this nutrition request type.")                

class NutrReqOralDietFluidConsistency(models.Model):    
    _name = "hc.nutr.req.oral.diet.fluid.consistency"    
    _description = "Nutrition Request Oral Diet Fluid Consistency"        
    _inherit = ["hc.basic.association"]

    oral_diet_id = fields.Many2one(comodel_name="hc.nutr.req.oral.diet", string="Oral Diet", help="Oral Diet associated with this nutrition request oral diet.")                
    fluid_consistency_type_id = fields.Many2one(comodel_name="hc.vs.consistency.type", string="Fluid Consistency Type", help="Consistency Type associated with this nutrition request fluid consistency type.")                

class NutrReqSupplSched(models.Model):    
    _name = "hc.nutr.req.suppl.sched"    
    _description = "Nutrition Request Supplement Schedule"        
    _inherit = ["hc.basic.association", "hc.timing"]

    supplement_id = fields.Many2one(comodel_name="hc.nutr.req.suppl", string="Supplement", help="Supplement associated with this nutrition request supplement.")                

class NutrReqFoodPrefMod(models.Model):    
    _name = "hc.nutr.req.food.pref.mod"    
    _description = "Nutrition Request Food Preference Modifier"        
    _inherit = ["hc.basic.association"]

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this nutrition request food preference modifier.")                
    food_preference_modifier_id = fields.Many2one(comodel_name="hc.vs.encounter.diet", string="Food Preference Modifier", help="Encounter Diet associated with this nutrition request food preference modifier.")                

class NutrReqExclFoodMod(models.Model):    
    _name = "hc.nutr.req.excl.food.mod"    
    _description = "Nutrition Request Exclude Food Modifier"        
    _inherit = ["hc.basic.association"]

    nutrition_request_id = fields.Many2one(comodel_name="hc.res.nutrition.request", string="Nutrition Request", help="Nutrition Request associated with this nutrition request nutrition request.")                
    exclude_food_modifier_id = fields.Many2one(comodel_name="hc.vs.food.type", string="Exclude Food Modifier", help="Food Type associated with this nutrition request exclude food modifier.")                

class NutrReqEntForAdminSched(models.Model):    
    _name = "hc.nutr.req.ent.for.admin.sched"    
    _description = "Nutrition Request Enteral Formula Administration Schedule"        
    _inherit = ["hc.basic.association", "hc.timing"]

    administration_id = fields.Many2one(comodel_name="hc.nutr.req.ent.for.admin", string="Administration", help="Administration associated with this nutrition request enteral formula administration schedule.")                

class ConsistencyType(models.Model):    
    _name = "hc.vs.consistency.type"    
    _description = "Consistency Type"        
    _inherit = ["hc.value.set.contains"]

class DietType(models.Model):    
    _name = "hc.vs.diet.type"    
    _description = "Diet Type"        
    _inherit = ["hc.value.set.contains"]

class EncounterDiet(models.Model):    
    _name = "hc.vs.encounter.diet"    
    _description = "Encounter Diet"        
    _inherit = ["hc.value.set.contains"]

class EntFormulaAdditive(models.Model):    
    _name = "hc.vs.ent.formula.additive"    
    _description = "Ent Formula Additive"        
    _inherit = ["hc.value.set.contains"]

class EntFormulaType(models.Model):    
    _name = "hc.vs.ent.formula.type"    
    _description = "Ent Formula Type"        
    _inherit = ["hc.value.set.contains"]

class EnteralRoute(models.Model):    
    _name = "hc.vs.enteral.route"    
    _description = "Enteral Route"        
    _inherit = ["hc.value.set.contains"]

class FoodType(models.Model):    
    _name = "hc.vs.food.type"    
    _description = "Food Type"        
    _inherit = ["hc.value.set.contains"]

class NutrientCode(models.Model):    
    _name = "hc.vs.nutrient.code"    
    _description = "Nutrient Code"        
    _inherit = ["hc.value.set.contains"]

class SupplementType(models.Model):    
    _name = "hc.vs.supplement.type"    
    _description = "Supplement Type"        
    _inherit = ["hc.value.set.contains"]

class TextureCode(models.Model):    
    _name = "hc.vs.texture.code"    
    _description = "Texture Code"        
    _inherit = ["hc.value.set.contains"]
