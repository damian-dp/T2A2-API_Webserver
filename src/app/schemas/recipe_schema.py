from ..extensions import ma
from ..models.recipe import Recipe
from marshmallow import fields
from .recipe_ingredient_schema import RecipeIngredientSchema

class RecipeSchema(ma.SQLAlchemyAutoSchema):
    dog_ids = fields.List(fields.Integer())
    ingredients = fields.Nested(RecipeIngredientSchema, many=True)
    user_id = fields.Integer(allow_none=True)

    class Meta:
        model = Recipe
        load_instance = True
        include_fk = True
        include_relationships = True
        exclude = ('dogs','user')  # Exclude the 'dogs' relationship from serialization

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)