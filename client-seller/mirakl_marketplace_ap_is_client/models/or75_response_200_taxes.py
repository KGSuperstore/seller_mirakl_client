from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR75Response200Taxes")


@_attrs_define
class OR75Response200Taxes:
    """
    Attributes:
        code (Union[Unset, str]): Tax code
        label (Union[Unset, str]): Tax label
        tax_calculation_rule (Union[Unset, str]): The type of automated calculation done during a partial refund or
            cancellation.<br/>Possible values:<br/>- none: No calculation will be done in case of partial refund or
            cancellation. You must provide the amount of tax you want to refund or cancel when you request a refund or
            cancellation. Otherwise, the tax will not get refunded/cancelled.<br/>- proportional_to_amount: Mirakl will
            automatically calculate the proportional tax amount when a refund or cancellation is requested. You do not need
            to provide the amount of this tax when you request a refund or cancellation.
    """

    code: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    tax_calculation_rule: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        label = self.label

        tax_calculation_rule = self.tax_calculation_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if label is not UNSET:
            field_dict["label"] = label
        if tax_calculation_rule is not UNSET:
            field_dict["tax_calculation_rule"] = tax_calculation_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        label = d.pop("label", UNSET)

        tax_calculation_rule = d.pop("tax_calculation_rule", UNSET)

        or75_response_200_taxes = cls(
            code=code,
            label=label,
            tax_calculation_rule=tax_calculation_rule,
        )

        or75_response_200_taxes.additional_properties = d
        return or75_response_200_taxes

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
