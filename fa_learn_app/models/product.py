import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseProduct(BaseModel):
    # Базовый класс для описания продукта

    name :str
    description :Optional[str] = None

class ProductIn(BaseProduct):
    # Класс описывает продукт, отправленный от пользователя

    secret_token :str

class ProductOut(BaseProduct):
    # Класс описывает продукт, который отправляется пользователю (без секретной информации)

    id :uuid.UUID
    created_at :datetime.datetime

class ProductStorage(BaseProduct):
    # Класс описывает хранение продукта в хранилище

    id :uuid.UUID
    created_at :datetime.datetime
    secret_token :str

