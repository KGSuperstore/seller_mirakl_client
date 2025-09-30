from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="P31Response200Products")


@_attrs_define
class P31Response200Products:
    """
    Attributes:
        category_code (Union[Unset, str]): Product category code
        category_label (Union[Unset, str]): Product category label
        product_id (Union[Unset, str]): Product ID
        product_id_type (Union[Unset, str]): Product ID type
        product_sku (Union[Unset, str]): Product SKU
        product_title (Union[Unset, str]): Product title
    """

    category_code: Union[Unset, str] = UNSET
    category_label: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    product_id_type: Union[Unset, str] = UNSET
    product_sku: Union[Unset, str] = UNSET
    product_title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_code = self.category_code

        category_label = self.category_label

        product_id = self.product_id

        product_id_type = self.product_id_type

        product_sku = self.product_sku

        product_title = self.product_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if category_label is not UNSET:
            field_dict["category_label"] = category_label
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_id_type is not UNSET:
            field_dict["product_id_type"] = product_id_type
        if product_sku is not UNSET:
            field_dict["product_sku"] = product_sku
        if product_title is not UNSET:
            field_dict["product_title"] = product_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_code = d.pop("category_code", UNSET)

        category_label = d.pop("category_label", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_id_type = d.pop("product_id_type", UNSET)

        product_sku = d.pop("product_sku", UNSET)

        product_title = d.pop("product_title", UNSET)

        p31_response_200_products = cls(
            category_code=category_code,
            category_label=category_label,
            product_id=product_id,
            product_id_type=product_id_type,
            product_sku=product_sku,
            product_title=product_title,
        )

        p31_response_200_products.additional_properties = d
        return p31_response_200_products

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
