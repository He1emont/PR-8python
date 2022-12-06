from typing import List, Dict, Optional
import uuid
from fa_learn_app.models.product import ProductIn, ProductOut, ProductStorage
from fa_learn_app.utils.repository_utils import \
    convert_product_storage_to_out, \
    convert_product_in_to_storage, \
    update_product_in_storage


class BaseProductRepository:
    # Базовый класс для реализации функционала работы с продуктами

    def get_by_id(self, id: uuid.UUID) -> ProductOut:
        raise NotImplementedError

    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        raise NotImplementedError

    def create(self, product: ProductIn) -> ProductOut:
        raise NotImplementedError

    def update_by_id(self, id: uuid.UUID, product: ProductIn) -> ProductStorage:
        raise NotImplementedError

    def delete_by_id(self, id: uuid.UUID) -> ProductOut:
        raise NotImplementedError


class ProductTmpRepository(BaseProductRepository):
    # Реализация продукта с временным хранилищем в объекте Dict

    def __init__(self):

        # Временное хранилище
        self._dict_products: Dict[uuid.UUID, ProductStorage] = {}

    def get_by_id(self, id: uuid.UUID) -> Optional[ProductOut]:
        # Получение продукта по id

        product: ProductStorage = self._dict_products.get(id)
        if product is None:
            return "Продукт не найден"
        product_out: ProductOut = convert_product_storage_to_out(product)
        return product_out

    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        # Получение всех продуктов

        product_out_list: List[ProductOut] = []
        for _, product in self._dict_products.items():
            product_out_list.append(convert_product_storage_to_out(product))
        return product_out_list[skip:skip + limit]

    def create(self, product: ProductIn) -> ProductOut:
        # Создание продукта

        product_storage: ProductStorage = convert_product_in_to_storage(product)
        self._dict_products.update({product_storage.id: product_storage})
        product_out: ProductOut = convert_product_storage_to_out(product_storage)
        return product_out

    def update_by_id(self, id: uuid.UUID, product_new: ProductIn) -> Optional[ProductOut]:
        # Получение продукта по id для обновления данных

        product_old: ProductStorage = self._dict_products.get(id)
        if product_old is None:
            return "Продукт не найден"

        product_update: ProductOut = update_product_in_storage(id, product_new)
        self._dict_products.update({product_update.id: product_update})
        product_out: ProductOut = convert_product_storage_to_out(product_update)
        return product_out

    def delete_by_id(self, id: uuid.UUID) -> str:
        # Получение продукта по id

        product: ProductStorage = self._dict_products.get(id)
        if product is None:
            return "Продукт не найден"
        self._dict_products.pop(id, None)
        return "Продукт успешно удален"