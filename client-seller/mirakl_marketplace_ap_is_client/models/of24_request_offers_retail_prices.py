from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF24RequestOffersRetailPrices")


@_attrs_define
class OF24RequestOffersRetailPrices:
    """The retail prices of the offer, also referred to as selling prices. Applicable only for Dropship offers.

    Attributes:
        discount_end_date (Union[Unset, str]): The end date of the discount. If no discount is desired, set it to null.
        discount_start_date (Union[Unset, str]): The start date of the discount. If no discount is desired, set it to
            null.
        unit_discount_price (Union[Unset, float]): The default unit discount retail price, i.e. the retail unit price
            when the discount applied.
        unit_origin_price (Union[Unset, float]): The default unit original retail price, i.e. the retail unit price
            without discount.
    """

    discount_end_date: Union[Unset, str] = UNSET
    discount_start_date: Union[Unset, str] = UNSET
    unit_discount_price: Union[Unset, float] = UNSET
    unit_origin_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discount_end_date = self.discount_end_date

        discount_start_date = self.discount_start_date

        unit_discount_price = self.unit_discount_price

        unit_origin_price = self.unit_origin_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_end_date is not UNSET:
            field_dict["discount_end_date"] = discount_end_date
        if discount_start_date is not UNSET:
            field_dict["discount_start_date"] = discount_start_date
        if unit_discount_price is not UNSET:
            field_dict["unit_discount_price"] = unit_discount_price
        if unit_origin_price is not UNSET:
            field_dict["unit_origin_price"] = unit_origin_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discount_end_date = d.pop("discount_end_date", UNSET)

        discount_start_date = d.pop("discount_start_date", UNSET)

        unit_discount_price = d.pop("unit_discount_price", UNSET)

        unit_origin_price = d.pop("unit_origin_price", UNSET)

        of24_request_offers_retail_prices = cls(
            discount_end_date=discount_end_date,
            discount_start_date=discount_start_date,
            unit_discount_price=unit_discount_price,
            unit_origin_price=unit_origin_price,
        )

        of24_request_offers_retail_prices.additional_properties = d
        return of24_request_offers_retail_prices

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
