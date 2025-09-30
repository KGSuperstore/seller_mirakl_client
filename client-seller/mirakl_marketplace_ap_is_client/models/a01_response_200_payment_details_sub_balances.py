from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A01Response200PaymentDetailsSubBalances")


@_attrs_define
class A01Response200PaymentDetailsSubBalances:
    """
    Attributes:
        paid (Union[Unset, float]): Paid balance
        pay_out_psp_code (Union[Unset, str]): Code of the Payment Service Provider (PSP)
        payable (Union[Unset, float]): Payable balance
        pending (Union[Unset, float]): Pending balance
    """

    paid: Union[Unset, float] = UNSET
    pay_out_psp_code: Union[Unset, str] = UNSET
    payable: Union[Unset, float] = UNSET
    pending: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid = self.paid

        pay_out_psp_code = self.pay_out_psp_code

        payable = self.payable

        pending = self.pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paid is not UNSET:
            field_dict["paid"] = paid
        if pay_out_psp_code is not UNSET:
            field_dict["pay_out_psp_code"] = pay_out_psp_code
        if payable is not UNSET:
            field_dict["payable"] = payable
        if pending is not UNSET:
            field_dict["pending"] = pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paid = d.pop("paid", UNSET)

        pay_out_psp_code = d.pop("pay_out_psp_code", UNSET)

        payable = d.pop("payable", UNSET)

        pending = d.pop("pending", UNSET)

        a01_response_200_payment_details_sub_balances = cls(
            paid=paid,
            pay_out_psp_code=pay_out_psp_code,
            payable=payable,
            pending=pending,
        )

        a01_response_200_payment_details_sub_balances.additional_properties = d
        return a01_response_200_payment_details_sub_balances

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
