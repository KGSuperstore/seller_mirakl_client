from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p31_response_200_products import P31Response200Products


T = TypeVar("T", bound="P31Response200")


@_attrs_define
class P31Response200:
    """
    Attributes:
        products (Union[Unset, list['P31Response200Products']]): Products list
    """

    products: Union[Unset, list["P31Response200Products"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p31_response_200_products import P31Response200Products

        d = dict(src_dict)
        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = P31Response200Products.from_dict(products_item_data)

            products.append(products_item)

        p31_response_200 = cls(
            products=products,
        )

        p31_response_200.additional_properties = d
        return p31_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
