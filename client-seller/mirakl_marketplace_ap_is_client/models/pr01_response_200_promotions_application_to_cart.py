from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PR01Response200PromotionsApplicationToCart")


@_attrs_define
class PR01Response200PromotionsApplicationToCart:
    """
    Attributes:
        promo_code (Union[Unset, str]): Promo code associated to the promotion
    """

    promo_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        promo_code = self.promo_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promo_code is not UNSET:
            field_dict["promo_code"] = promo_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        promo_code = d.pop("promo_code", UNSET)

        pr01_response_200_promotions_application_to_cart = cls(
            promo_code=promo_code,
        )

        pr01_response_200_promotions_application_to_cart.additional_properties = d
        return pr01_response_200_promotions_application_to_cart

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
