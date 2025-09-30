import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="P11Response200ProductsOffersShippingTypesDeliveryTime")


@_attrs_define
class P11Response200ProductsOffersShippingTypesDeliveryTime:
    """
    Attributes:
        earliest_days (Union[Unset, int]): Earliest order delivery time
        earliest_delivery_date (Union[Unset, datetime.datetime]): Earliest order delivery date
        latest_days (Union[Unset, int]): Latest order delivery time
        latest_delivery_date (Union[Unset, datetime.datetime]): Latest order delivery date
    """

    earliest_days: Union[Unset, int] = UNSET
    earliest_delivery_date: Union[Unset, datetime.datetime] = UNSET
    latest_days: Union[Unset, int] = UNSET
    latest_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        earliest_days = self.earliest_days

        earliest_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.earliest_delivery_date, Unset):
            earliest_delivery_date = self.earliest_delivery_date.isoformat()

        latest_days = self.latest_days

        latest_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_delivery_date, Unset):
            latest_delivery_date = self.latest_delivery_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if earliest_days is not UNSET:
            field_dict["earliest_days"] = earliest_days
        if earliest_delivery_date is not UNSET:
            field_dict["earliest_delivery_date"] = earliest_delivery_date
        if latest_days is not UNSET:
            field_dict["latest_days"] = latest_days
        if latest_delivery_date is not UNSET:
            field_dict["latest_delivery_date"] = latest_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        earliest_days = d.pop("earliest_days", UNSET)

        _earliest_delivery_date = d.pop("earliest_delivery_date", UNSET)
        earliest_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_earliest_delivery_date, Unset):
            earliest_delivery_date = UNSET
        else:
            earliest_delivery_date = isoparse(_earliest_delivery_date)

        latest_days = d.pop("latest_days", UNSET)

        _latest_delivery_date = d.pop("latest_delivery_date", UNSET)
        latest_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_delivery_date, Unset):
            latest_delivery_date = UNSET
        else:
            latest_delivery_date = isoparse(_latest_delivery_date)

        p11_response_200_products_offers_shipping_types_delivery_time = cls(
            earliest_days=earliest_days,
            earliest_delivery_date=earliest_delivery_date,
            latest_days=latest_days,
            latest_delivery_date=latest_delivery_date,
        )

        p11_response_200_products_offers_shipping_types_delivery_time.additional_properties = d
        return p11_response_200_products_offers_shipping_types_delivery_time

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
