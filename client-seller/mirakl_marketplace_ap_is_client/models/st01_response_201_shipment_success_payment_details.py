import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ST01Response201ShipmentSuccessPaymentDetails")


@_attrs_define
class ST01Response201ShipmentSuccessPaymentDetails:
    """
    Attributes:
        customer_debited_date (Union[Unset, datetime.datetime]): Payment's date of the shipment by the customer
        transaction_date (Union[Unset, datetime.datetime]): Payment transaction date
        transaction_number (Union[Unset, str]): Payment transaction number
    """

    customer_debited_date: Union[Unset, datetime.datetime] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_debited_date: Union[Unset, str] = UNSET
        if not isinstance(self.customer_debited_date, Unset):
            customer_debited_date = self.customer_debited_date.isoformat()

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        transaction_number = self.transaction_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_debited_date is not UNSET:
            field_dict["customer_debited_date"] = customer_debited_date
        if transaction_date is not UNSET:
            field_dict["transaction_date"] = transaction_date
        if transaction_number is not UNSET:
            field_dict["transaction_number"] = transaction_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _customer_debited_date = d.pop("customer_debited_date", UNSET)
        customer_debited_date: Union[Unset, datetime.datetime]
        if isinstance(_customer_debited_date, Unset):
            customer_debited_date = UNSET
        else:
            customer_debited_date = isoparse(_customer_debited_date)

        _transaction_date = d.pop("transaction_date", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        transaction_number = d.pop("transaction_number", UNSET)

        st01_response_201_shipment_success_payment_details = cls(
            customer_debited_date=customer_debited_date,
            transaction_date=transaction_date,
            transaction_number=transaction_number,
        )

        st01_response_201_shipment_success_payment_details.additional_properties = d
        return st01_response_201_shipment_success_payment_details

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
