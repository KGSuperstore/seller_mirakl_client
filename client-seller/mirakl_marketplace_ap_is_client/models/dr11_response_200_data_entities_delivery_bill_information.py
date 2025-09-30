import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DR11Response200DataEntitiesDeliveryBillInformation")


@_attrs_define
class DR11Response200DataEntitiesDeliveryBillInformation:
    """
    Attributes:
        delivery_bill_date (Union[Unset, datetime.date]): Delivery bill date
        delivery_bill_id (Union[Unset, str]): Delivery bill ID
    """

    delivery_bill_date: Union[Unset, datetime.date] = UNSET
    delivery_bill_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_bill_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_bill_date, Unset):
            delivery_bill_date = self.delivery_bill_date.isoformat()

        delivery_bill_id = self.delivery_bill_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_bill_date is not UNSET:
            field_dict["delivery_bill_date"] = delivery_bill_date
        if delivery_bill_id is not UNSET:
            field_dict["delivery_bill_id"] = delivery_bill_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _delivery_bill_date = d.pop("delivery_bill_date", UNSET)
        delivery_bill_date: Union[Unset, datetime.date]
        if isinstance(_delivery_bill_date, Unset):
            delivery_bill_date = UNSET
        else:
            delivery_bill_date = isoparse(_delivery_bill_date).date()

        delivery_bill_id = d.pop("delivery_bill_id", UNSET)

        dr11_response_200_data_entities_delivery_bill_information = cls(
            delivery_bill_date=delivery_bill_date,
            delivery_bill_id=delivery_bill_id,
        )

        dr11_response_200_data_entities_delivery_bill_information.additional_properties = d
        return dr11_response_200_data_entities_delivery_bill_information

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
