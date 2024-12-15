from peewee import (
    AutoField,
    ForeignKeyField
)

# Models import
from app.classes.models.base_model import BaseModel
from app.classes.models.main_cart import MainCart
from app.classes.models.merchandise_items import MerchandiseItems

# Helpers import
from app.classes.helpers.db_helpers import DatabaseHelpers

# Auction Items Model
class CartMerchItems(BaseModel):
    entry_id = AutoField(primary_key=True, unique=True)
    cart_id = ForeignKeyField(MainCart, to_field="cart_id")
    merch_id = ForeignKeyField(MerchandiseItems, to_field="merch_id")
    class Meta:
        table_name = "CartMerchItems"

# CartMerchItems Class/Methods
class CartMerchItems_Methods:
    def __init__(self, database):
        self.database = database

    @staticmethod
    def create_entry(
        cart_id: int,
        merch_id: int
    ) -> int:
        """
        Creates an merch item cart record in the database

        Args:
            cart_id: the numeric ID of the associated card
            merch_id: the numeric ID of the merchandise item
        
        Returns:
            int: The numeric ID of the cart entry

        Raises:
            PeeweeException: If the entry ID already exists or if cart_id/merch_id fail foreign key constraints
        """
        return CartMerchItems.create(
            cart_id=cart_id,
            merch_id=merch_id,
        ).entry_id
    
    @staticmethod
    def get_all_entries():
        query = CartMerchItems.select()
        return DatabaseHelpers.get_rows(query)
    
    @staticmethod
    def get_entry_by_id(entry_id: int):
        return CartMerchItems.select().where(CartMerchItems.entry_id == entry_id).get()
    
    @staticmethod
    def update_entry(item_obj: object):
        return item_obj.save()
    
    @staticmethod
    def remove_entry(entry_id: int):
        CartMerchItems.delete().where(CartMerchItems.entry_id == entry_id).execute()
        return True
    
    @staticmethod
    def get_entries_by_cart(cart_id: int):
        query = CartMerchItems.select().where(CartMerchItems.cart_id == cart_id)
        return DatabaseHelpers.get_rows(query)