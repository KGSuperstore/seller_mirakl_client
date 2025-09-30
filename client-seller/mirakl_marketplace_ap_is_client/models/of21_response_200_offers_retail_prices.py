import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF21Response200OffersRetailPrices")


@_attrs_define
class OF21Response200OffersRetailPrices:
    """
    Attributes:
        discount_end_date (Union[Unset, datetime.datetime]): End date of the discount, or null if no discount exists or
            if the discount does not have an end date.
        discount_start_date (Union[Unset, datetime.datetime]): Start date of the discount, or null if no discount exists
            or if the discount does not have a start date.
        price (Union[Unset, float]): Retail price of the offer, also referred to as selling price.
            <br/>
            If a discount is defined and is currently active (within the validity interval), it represents the
            unit_discount_price.
            <br/>
            In other cases, it represents the unit_origin_price.
        unit_discount_price (Union[Unset, float]): Discount retail price for a quantity of one, i.e. the discount retail
            price for a quantity of one.
            <br/>
            Set to null if no discount is defined or if no discount retail price for a quantity of one is defined or if the
            discount is not currently active (within the validity interval).
        unit_origin_price (Union[Unset, float]): Original retail price for a quantity of one, i.e. the retail price for
            a quantity of one regardless of the discounts.
    """

    discount_end_date: Union[Unset, datetime.datetime] = UNSET
    discount_start_date: Union[Unset, datetime.datetime] = UNSET
    price: Union[Unset, float] = UNSET
    unit_discount_price: Union[Unset, float] = UNSET
    unit_origin_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discount_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.discount_end_date, Unset):
            discount_end_date = self.discount_end_date.isoformat()

        discount_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.discount_start_date, Unset):
            discount_start_date = self.discount_start_date.isoformat()

        price = self.price

        unit_discount_price = self.unit_discount_price

        unit_origin_price = self.unit_origin_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_end_date is not UNSET:
            field_dict["discount_end_date"] = discount_end_date
        if discount_start_date is not UNSET:
            field_dict["discount_start_date"] = discount_start_date
        if price is not UNSET:
            field_dict["price"] = price
        if unit_discount_price is not UNSET:
            field_dict["unit_discount_price"] = unit_discount_price
        if unit_origin_price is not UNSET:
            field_dict["unit_origin_price"] = unit_origin_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _discount_end_date = d.pop("discount_end_date", UNSET)
        discount_end_date: Union[Unset, datetime.datetime]
        if isinstance(_discount_end_date, Unset):
            discount_end_date = UNSET
        else:
            discount_end_date = isoparse(_discount_end_date)

        _discount_start_date = d.pop("discount_start_date", UNSET)
        discount_start_date: Union[Unset, datetime.datetime]
        if isinstance(_discount_start_date, Unset):
            discount_start_date = UNSET
        else:
            discount_start_date = isoparse(_discount_start_date)

        price = d.pop("price", UNSET)

        unit_discount_price = d.pop("unit_discount_price", UNSET)

        unit_origin_price = d.pop("unit_origin_price", UNSET)

        of21_response_200_offers_retail_prices = cls(
            discount_end_date=discount_end_date,
            discount_start_date=discount_start_date,
            price=price,
            unit_discount_price=unit_discount_price,
            unit_origin_price=unit_origin_price,
        )

        of21_response_200_offers_retail_prices.additional_properties = d
        return of21_response_200_offers_retail_prices

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
