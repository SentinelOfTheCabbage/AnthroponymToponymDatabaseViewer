from enum import Enum


class MetaEnum(str, Enum):
    def __str__(self):
        return self.value


class Cat(MetaEnum):
    ANTHROPONYM = 'Антропонимы'
    TOPONYM = 'Топоним'
    OTHER = 'Остальное'


class AnthTables(MetaEnum):
    ANTHROPONYM = 'Антропонимы'
    IMAGE = 'Изображения'
    REFERENCE = 'Референсы'


class ToponTables(MetaEnum):
    TOPONYM = 'Топонимы'
    IMAGE = 'Изображения'
    REFERENCE = 'Референсы'
