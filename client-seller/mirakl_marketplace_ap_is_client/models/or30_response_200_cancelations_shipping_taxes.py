from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or30_response_200_cancelations_shipping_taxes_amount_breakdown import (
        OR30Response200CancelationsShippingTaxesAmountBreakdown,
    )
    from ..models.or30_response_200_cancelations_shipping_taxes_purchase_tax import (
        OR30Response200CancelationsShippingTaxesPurchaseTax,
    )


T = TypeVar("T", bound="OR30Response200CancelationsShippingTaxes")


@_attrs_define
class OR30Response200CancelationsShippingTaxes:
    """
    Attributes:
        amount (Union[Unset, float]): Tax amount
        amount_breakdown (Union[Unset, OR30Response200CancelationsShippingTaxesAmountBreakdown]):
        code (Union[Unset, str]): Tax code
        purchase_tax (Union[Unset, OR30Response200CancelationsShippingTaxesPurchaseTax]):
        rate (Union[Unset, float]): Tax rate
    """

    amount: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "OR30Response200CancelationsShippingTaxesAmountBreakdown"] = UNSET
    code: Union[Unset, str] = UNSET
    purchase_tax: Union[Unset, "OR30Response200CancelationsShippingTaxesPurchaseTax"] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.amount_breakdown, Unset):
            amount_breakdown = self.amount_breakdown.to_dict()

        code = self.code

        purchase_tax: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_tax, Unset):
            purchase_tax = self.purchase_tax.to_dict()

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_breakdown is not UNSET:
            field_dict["amount_breakdown"] = amount_breakdown
        if code is not UNSET:
            field_dict["code"] = code
        if purchase_tax is not UNSET:
            field_dict["purchase_tax"] = purchase_tax
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or30_response_200_cancelations_shipping_taxes_amount_breakdown import (
            OR30Response200CancelationsShippingTaxesAmountBreakdown,
        )
        from ..models.or30_response_200_cancelations_shipping_taxes_purchase_tax import (
            OR30Response200CancelationsShippingTaxesPurchaseTax,
        )

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _amount_breakdown = d.pop("amount_breakdown", UNSET)
        amount_breakdown: Union[Unset, OR30Response200CancelationsShippingTaxesAmountBreakdown]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = OR30Response200CancelationsShippingTaxesAmountBreakdown.from_dict(_amount_breakdown)

        code = d.pop("code", UNSET)

        _purchase_tax = d.pop("purchase_tax", UNSET)
        purchase_tax: Union[Unset, OR30Response200CancelationsShippingTaxesPurchaseTax]
        if isinstance(_purchase_tax, Unset):
            purchase_tax = UNSET
        else:
            purchase_tax = OR30Response200CancelationsShippingTaxesPurchaseTax.from_dict(_purchase_tax)

        rate = d.pop("rate", UNSET)

        or30_response_200_cancelations_shipping_taxes = cls(
            amount=amount,
            amount_breakdown=amount_breakdown,
            code=code,
            purchase_tax=purchase_tax,
            rate=rate,
        )

        or30_response_200_cancelations_shipping_taxes.additional_properties = d
        return or30_response_200_cancelations_shipping_taxes

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
