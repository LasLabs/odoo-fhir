# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Medication(models.Model):    
    _name = "hc.res.medication"    
    _description = "Medication"            

    name = fields.Char(string="Name", help="Common / Commercial name.")                    
    code_id = fields.Many2one(comodel_name="hc.vs.medication.code", string="Code", help="Codes that identify this medication.")                    
    is_brand = fields.Boolean(string="Is Brand", help="True if a brand.")                    
    manufacturer_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Manufacturer Organization", help="Manufacturer of the item.")                    
    product_ids = fields.One2many(comodel_name="hc.medication.product", inverse_name="medication_id", string="Products", help="Administrable medication details.")                    
    package_ids = fields.One2many(comodel_name="hc.medication.package", inverse_name="medication_id", string="Packages", help="Details about packaged medications.")                    

class MedicationProduct(models.Model):    
    _name = "hc.medication.product"    
    _description = "Medication Product"            

    medication_id = fields.Many2one(comodel_name="hc.res.medication", string="Product Medication", help="Medication associated with this Product.")                    
    form_id = fields.Many2one(comodel_name="hc.vs.medication.form.code", string="Product Form", help="Describes the form of the item. Powder; tablets; carton.")                    
    batch_ids = fields.One2many(comodel_name="hc.medication.product.batch", inverse_name="medication_product_id", string="Batches", help="A group of medication produced or packaged from one production run.")                    
    ingredient_ids = fields.One2many(comodel_name="hc.medication.product.ingredient", inverse_name="medication_product_id", string="Ingredients", help="Active or inactive ingredient.")                    

class MedicationProductIngredient(models.Model):    
    _name = "hc.medication.product.ingredient"  
    _description = "Medication Product Ingredient"      

    medication_product_id = fields.Many2one(comodel_name="hc.medication.product", string="Product", help="Product associated with this Ingredient.")                    
    item_type = fields.Selection(string="Ingredient Item Type", selection=[("codeable concept", "Codeable Concept"), ("substance", "Substance"), ("medication", "Medication")], help="Type of the product contained.")                    
    item_name = fields.Char(string="Item", compute="compute_item_name", required="True", help="The product contained.")                    
    item_id = fields.Many2one(comodel_name="hc.vs.medication.ingredient.code", string="Item", help="Codeable Concept product contained.")                    
    item_substance_id = fields.Many2one(comodel_name="hc.res.substance", string="Item Substance", help="Substance product contained.")                    
    item_medication_id = fields.Many2one(comodel_name="hc.res.medication", string="Item Medication", help="Medication product contained.")                    
    ingredient_quantity_numerator = fields.Float(string="Ingredient Quantity Numerator", help="Numerator value of how much ingredient in product.")                    
    total_quantity_denominator = fields.Float(string="Total Quantity Denominator", help="Denominator value of how much ingredient in product.")                    

class MedicationProductBatch(models.Model): 
    _name = "hc.medication.product.batch"   
    _description = "Medication Product Batch"

    medication_product_id = fields.Many2one(comodel_name="hc.medication.product", string="Product", help="Product associated with this Batch.")                    
    lot_number = fields.Char(string="Lot Number", help="The assigned lot number of a batch of the specified product.")                    
    expiration_date = fields.Date(string="Expiration Date", help="When this specific batch of product will expire.")                    

class MedicationPackage(models.Model):    
    _name = "hc.medication.package"    
    _description = "Medication Package"

    medication_id = fields.Many2one(comodel_name="hc.res.medication", string="Medication", help="Medication associated with this Package.")                    
    container_id = fields.Many2one(comodel_name="hc.vs.medication.package.container", string="Container", help="The kind of container that this package comes as (e.g., box, vial, blister-pack).")                    
    content_ids = fields.One2many(comodel_name="hc.medication.package.content", inverse_name="medication_package_id", string="Contents", help="What is in the package?.")                    

class MedicationPackageContent(models.Model):   
    _name = "hc.medication.package.content" 
    _description = "Medication Package Content"

    medication_package_id = fields.Many2one(comodel_name="hc.medication.package", string="Package", help="Package associated with this Content.")                    
    item_medication_id = fields.Many2one(comodel_name="hc.res.medication", string="Item Medication", required="True", help="A product in the package.")                    
    amount = fields.Float(string="Amount", help="How many are in the package?")                    
    amount_uom_id = fields.Many2one(comodel_name="product.uom", string="Amount UOM", help="Amount unit of measure.")                    

class MedicationCode(models.Model):    
    _name = "hc.vs.medication.code"    
    _description = "Medication Code"        
    _inherit = ["hc.value.set.contains"]    

class MedicationFormCode(models.Model):    
    _name = "hc.vs.medication.form.code"    
    _description = "Medication Form Code"        
    _inherit = ["hc.value.set.contains"]

class MedicationIngredientCode(models.Model):    
    _name = "hc.vs.medication.ingredient.code"    
    _description = "Medication Ingredient Code"        
    _inherit = ["hc.value.set.contains"]

class MedicationPackageContainer(models.Model):    
    _name = "hc.vs.medication.package.container"    
    _description = "Medication Package Container"        
    _inherit = ["hc.value.set.contains"]    
