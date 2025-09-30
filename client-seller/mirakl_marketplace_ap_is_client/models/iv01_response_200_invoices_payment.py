import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IV01Response200InvoicesPayment")


@_attrs_define
class IV01Response200InvoicesPayment:
    """
    Attributes:
        failure_reason (Union[Unset, str]): Failure reason
        reference (Union[Unset, str]): Transaction reference
        state (Union[Unset, str]): Payment status
        transaction_date (Union[Unset, datetime.datetime]): Transaction date
    """

    failure_reason: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failure_reason = self.failure_reason

        reference = self.reference

        state = self.state

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if reference is not UNSET:
            field_dict["reference"] = reference
        if state is not UNSET:
            field_dict["state"] = state
        if transaction_date is not UNSET:
            field_dict["transaction_date"] = transaction_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failure_reason = d.pop("failure_reason", UNSET)

        reference = d.pop("reference", UNSET)

        state = d.pop("state", UNSET)

        _transaction_date = d.pop("transaction_date", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        iv01_response_200_invoices_payment = cls(
            failure_reason=failure_reason,
            reference=reference,
            state=state,
            transaction_date=transaction_date,
        )

        iv01_response_200_invoices_payment.additional_properties = d
        return iv01_response_200_invoices_payment

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
