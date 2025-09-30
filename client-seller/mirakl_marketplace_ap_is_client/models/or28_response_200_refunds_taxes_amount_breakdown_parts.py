from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR28Response200RefundsTaxesAmountBreakdownParts")


@_attrs_define
class OR28Response200RefundsTaxesAmountBreakdownParts:
    """
    Attributes:
        amount (Union[Unset, float]): Part's amount. The sum of each part's amount is equal to the total amount.
        commissionable (Union[Unset, bool]): Should this amount be applied to the sellers commissions calculation.
        debitable_from_customer (Union[Unset, bool]): Should this amount be debited to the customer. <br/>If true, the
            amount is taken into account when generating the debit file.<br/>If false, the amount is not taken into account
            when generating the debit file.
        payable_to_shop (Union[Unset, bool]): Should this amount be paid to the shop. <br/>If true, the amount is taken
            into account when generating the shop payment voucher.<br/>If false, the amount is not taken into account when
            generating the shop payment voucher.
    """

    amount: Union[Unset, float] = UNSET
    commissionable: Union[Unset, bool] = UNSET
    debitable_from_customer: Union[Unset, bool] = UNSET
    payable_to_shop: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        commissionable = self.commissionable

        debitable_from_customer = self.debitable_from_customer

        payable_to_shop = self.payable_to_shop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if commissionable is not UNSET:
            field_dict["commissionable"] = commissionable
        if debitable_from_customer is not UNSET:
            field_dict["debitable_from_customer"] = debitable_from_customer
        if payable_to_shop is not UNSET:
            field_dict["payable_to_shop"] = payable_to_shop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        commissionable = d.pop("commissionable", UNSET)

        debitable_from_customer = d.pop("debitable_from_customer", UNSET)

        payable_to_shop = d.pop("payable_to_shop", UNSET)

        or28_response_200_refunds_taxes_amount_breakdown_parts = cls(
            amount=amount,
            commissionable=commissionable,
            debitable_from_customer=debitable_from_customer,
            payable_to_shop=payable_to_shop,
        )

        or28_response_200_refunds_taxes_amount_breakdown_parts.additional_properties = d
        return or28_response_200_refunds_taxes_amount_breakdown_parts

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
