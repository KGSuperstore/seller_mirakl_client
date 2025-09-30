from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_lines_taxes_amount_breakdown import (
        OR11Response200OrdersOrderLinesTaxesAmountBreakdown,
    )
    from ..models.or11_response_200_orders_order_lines_taxes_purchase_tax import (
        OR11Response200OrdersOrderLinesTaxesPurchaseTax,
    )


T = TypeVar("T", bound="OR11Response200OrdersOrderLinesTaxes")


@_attrs_define
class OR11Response200OrdersOrderLinesTaxes:
    """
    Attributes:
        amount (Union[Unset, float]): Tax amount
        amount_breakdown (Union[Unset, OR11Response200OrdersOrderLinesTaxesAmountBreakdown]):
        code (Union[Unset, str]): Tax code
        origin_unit_amount (Union[Unset, float]): The original tax amount of the offer associated with the order line
            before a discount or a promotion
        purchase_tax (Union[Unset, OR11Response200OrdersOrderLinesTaxesPurchaseTax]):
        rate (Union[Unset, float]): Tax rate
        tax_calculation_rule (Union[Unset, str]): The type of automated calculation done during a partial refund or
            cancellation.<br/>Possible values:<br/>- none: No calculation will be done in case of partial refund or
            cancellation. You must provide the amount of tax you want to refund or cancel when you request a refund or
            cancellation. Otherwise, the tax will not get refunded/cancelled.<br/>- proportional_to_amount: Mirakl will
            automatically calculate the proportional tax amount when a refund or cancellation is requested. You do not need
            to provide the amount of this tax when you request a refund or cancellation.
    """

    amount: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "OR11Response200OrdersOrderLinesTaxesAmountBreakdown"] = UNSET
    code: Union[Unset, str] = UNSET
    origin_unit_amount: Union[Unset, float] = UNSET
    purchase_tax: Union[Unset, "OR11Response200OrdersOrderLinesTaxesPurchaseTax"] = UNSET
    rate: Union[Unset, float] = UNSET
    tax_calculation_rule: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.amount_breakdown, Unset):
            amount_breakdown = self.amount_breakdown.to_dict()

        code = self.code

        origin_unit_amount = self.origin_unit_amount

        purchase_tax: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_tax, Unset):
            purchase_tax = self.purchase_tax.to_dict()

        rate = self.rate

        tax_calculation_rule = self.tax_calculation_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_breakdown is not UNSET:
            field_dict["amount_breakdown"] = amount_breakdown
        if code is not UNSET:
            field_dict["code"] = code
        if origin_unit_amount is not UNSET:
            field_dict["origin_unit_amount"] = origin_unit_amount
        if purchase_tax is not UNSET:
            field_dict["purchase_tax"] = purchase_tax
        if rate is not UNSET:
            field_dict["rate"] = rate
        if tax_calculation_rule is not UNSET:
            field_dict["tax_calculation_rule"] = tax_calculation_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_order_lines_taxes_amount_breakdown import (
            OR11Response200OrdersOrderLinesTaxesAmountBreakdown,
        )
        from ..models.or11_response_200_orders_order_lines_taxes_purchase_tax import (
            OR11Response200OrdersOrderLinesTaxesPurchaseTax,
        )

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _amount_breakdown = d.pop("amount_breakdown", UNSET)
        amount_breakdown: Union[Unset, OR11Response200OrdersOrderLinesTaxesAmountBreakdown]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = OR11Response200OrdersOrderLinesTaxesAmountBreakdown.from_dict(_amount_breakdown)

        code = d.pop("code", UNSET)

        origin_unit_amount = d.pop("origin_unit_amount", UNSET)

        _purchase_tax = d.pop("purchase_tax", UNSET)
        purchase_tax: Union[Unset, OR11Response200OrdersOrderLinesTaxesPurchaseTax]
        if isinstance(_purchase_tax, Unset):
            purchase_tax = UNSET
        else:
            purchase_tax = OR11Response200OrdersOrderLinesTaxesPurchaseTax.from_dict(_purchase_tax)

        rate = d.pop("rate", UNSET)

        tax_calculation_rule = d.pop("tax_calculation_rule", UNSET)

        or11_response_200_orders_order_lines_taxes = cls(
            amount=amount,
            amount_breakdown=amount_breakdown,
            code=code,
            origin_unit_amount=origin_unit_amount,
            purchase_tax=purchase_tax,
            rate=rate,
            tax_calculation_rule=tax_calculation_rule,
        )

        or11_response_200_orders_order_lines_taxes.additional_properties = d
        return or11_response_200_orders_order_lines_taxes

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
