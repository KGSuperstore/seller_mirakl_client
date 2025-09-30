import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersDeliveryDate")


@_attrs_define
class OR11Response200OrdersDeliveryDate:
    """
    Attributes:
        earliest (Union[Unset, datetime.datetime]): Earliest order delivery date
        latest (Union[Unset, datetime.datetime]): Latest order delivery date
    """

    earliest: Union[Unset, datetime.datetime] = UNSET
    latest: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        earliest: Union[Unset, str] = UNSET
        if not isinstance(self.earliest, Unset):
            earliest = self.earliest.isoformat()

        latest: Union[Unset, str] = UNSET
        if not isinstance(self.latest, Unset):
            latest = self.latest.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if earliest is not UNSET:
            field_dict["earliest"] = earliest
        if latest is not UNSET:
            field_dict["latest"] = latest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _earliest = d.pop("earliest", UNSET)
        earliest: Union[Unset, datetime.datetime]
        if isinstance(_earliest, Unset):
            earliest = UNSET
        else:
            earliest = isoparse(_earliest)

        _latest = d.pop("latest", UNSET)
        latest: Union[Unset, datetime.datetime]
        if isinstance(_latest, Unset):
            latest = UNSET
        else:
            latest = isoparse(_latest)

        or11_response_200_orders_delivery_date = cls(
            earliest=earliest,
            latest=latest,
        )

        or11_response_200_orders_delivery_date.additional_properties = d
        return or11_response_200_orders_delivery_date

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
