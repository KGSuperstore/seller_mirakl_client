from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF21Response200OffersDiscountRanges")


@_attrs_define
class OF21Response200OffersDiscountRanges:
    """
    Attributes:
        price (Union[Unset, float]): Price of the offer if the quantity threshold is reached
        quantity_threshold (Union[Unset, int]): Minimum quantity to order for the given price to be applied
    """

    price: Union[Unset, float] = UNSET
    quantity_threshold: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        quantity_threshold = self.quantity_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if quantity_threshold is not UNSET:
            field_dict["quantity_threshold"] = quantity_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price", UNSET)

        quantity_threshold = d.pop("quantity_threshold", UNSET)

        of21_response_200_offers_discount_ranges = cls(
            price=price,
            quantity_threshold=quantity_threshold,
        )

        of21_response_200_offers_discount_ranges.additional_properties = d
        return of21_response_200_offers_discount_ranges

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
