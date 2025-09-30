from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF24RequestOffersAllPricesVolumePrices")


@_attrs_define
class OF24RequestOffersAllPricesVolumePrices:
    """The volume prices applicable for the offer.

    Attributes:
        quantity_threshold (Union[Unset, int]): The quantity threshold from which the volume price is applicable
        unit_discount_price (Union[Unset, float]): The unit discount price, i.e. the unit price when the discount
            applies
        unit_origin_price (Union[Unset, float]): The unit original price, i.e. the unit price excluding discounts
    """

    quantity_threshold: Union[Unset, int] = UNSET
    unit_discount_price: Union[Unset, float] = UNSET
    unit_origin_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity_threshold = self.quantity_threshold

        unit_discount_price = self.unit_discount_price

        unit_origin_price = self.unit_origin_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity_threshold is not UNSET:
            field_dict["quantity_threshold"] = quantity_threshold
        if unit_discount_price is not UNSET:
            field_dict["unit_discount_price"] = unit_discount_price
        if unit_origin_price is not UNSET:
            field_dict["unit_origin_price"] = unit_origin_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity_threshold = d.pop("quantity_threshold", UNSET)

        unit_discount_price = d.pop("unit_discount_price", UNSET)

        unit_origin_price = d.pop("unit_origin_price", UNSET)

        of24_request_offers_all_prices_volume_prices = cls(
            quantity_threshold=quantity_threshold,
            unit_discount_price=unit_discount_price,
            unit_origin_price=unit_origin_price,
        )

        of24_request_offers_all_prices_volume_prices.additional_properties = d
        return of24_request_offers_all_prices_volume_prices

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
