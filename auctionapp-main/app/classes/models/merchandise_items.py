from peewee import (
    BooleanField,
    CharField,
    DecimalField,
    AutoField
)

# Models import
from app.classes.models.base_model import BaseModel

# Helpers import
from app.classes.helpers.db_helpers import DatabaseHelpers

# Merchandise Items Model
class MerchandiseItems(BaseModel):
    merch_id = AutoField(primary_key=True, unique=True)
    merch_title = CharField(default="", max_length = 100)
    merch_description = CharField(default = "", max_length = 255)
    merch_price = DecimalField(default = 0)
    merch_image = CharField(default = "", max_length = 1000)
    is_active = BooleanField(default = True)

    class Meta:
        table_name = "MerchandiseItems"

# Merchandise Items Class/Methods
class MerchandiseItems_Methods:
    def __init__(self, database):
        self.database = database

    @staticmethod
    def create_item(
        merch_title: str,
        merch_description: str,
        merch_price: float,
        merch_image: str,
        is_active: bool = True
    ) -> int:
        """
        Creates a merchandise item in the database

        Args:
            merch_title: The name/title of the merch item
            merch_description: A brief description of the item
            merch_price: The price (in dollars) of the item
            merch_image: The path to the item image
        
        Returns:
            int: The numeric ID of the new item

        Raises:
            PeeweeException: If the item ID already exists
        """
        return MerchandiseItems.create(
            merch_title=merch_title,
            merch_description=merch_description,
            merch_price=merch_price,
            merch_image=merch_image,
            is_active=is_active
        ).merch_id
    
    @staticmethod
    def get_all_items():
        query = MerchandiseItems.select()
        return DatabaseHelpers.get_rows(query)
    
    @staticmethod
    def get_item_by_id(merch_id: int):
        return MerchandiseItems.select().where(MerchandiseItems.merch_id == merch_id).get()
    
    @staticmethod
    def update_item(item_obj: object):
        return item_obj.save()
    
    @staticmethod
    def remove_item(item_id):
        MerchandiseItems.delete().where(MerchandiseItems.merch_id == item_id).execute()
        return True