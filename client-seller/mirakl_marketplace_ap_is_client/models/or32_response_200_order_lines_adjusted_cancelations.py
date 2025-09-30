from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or32_response_200_order_lines_adjusted_cancelations_eco_contributions import (
        OR32Response200OrderLinesAdjustedCancelationsEcoContributions,
    )
    from ..models.or32_response_200_order_lines_adjusted_cancelations_shipping_taxes import (
        OR32Response200OrderLinesAdjustedCancelationsShippingTaxes,
    )
    from ..models.or32_response_200_order_lines_adjusted_cancelations_taxes import (
        OR32Response200OrderLinesAdjustedCancelationsTaxes,
    )


T = TypeVar("T", bound="OR32Response200OrderLinesAdjustedCancelations")


@_attrs_define
class OR32Response200OrderLinesAdjustedCancelations:
    """
    Attributes:
        amount (Union[Unset, float]): The offer part amount canceled
        currency_iso_code (Union[Unset, str]):
        eco_contributions (Union[Unset, list['OR32Response200OrderLinesAdjustedCancelationsEcoContributions']]): List of
            eco-contribution amounts and corresponding producer identifiers, if applicable<br/>
            Only available if the operator activates the circular economy information collection.
        quantity (Union[Unset, int]): The quantity of goods canceled
        reason_code (Union[Unset, str]): Cancellation's reason code
        shipping_amount (Union[Unset, float]): The shipping charges part amount canceled
        shipping_taxes (Union[Unset, list['OR32Response200OrderLinesAdjustedCancelationsShippingTaxes']]): The taxes
            canceled on the shipping price
        taxes (Union[Unset, list['OR32Response200OrderLinesAdjustedCancelationsTaxes']]): The taxes canceled on the
            product price
    """

    amount: Union[Unset, float] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    eco_contributions: Union[Unset, list["OR32Response200OrderLinesAdjustedCancelationsEcoContributions"]] = UNSET
    quantity: Union[Unset, int] = UNSET
    reason_code: Union[Unset, str] = UNSET
    shipping_amount: Union[Unset, float] = UNSET
    shipping_taxes: Union[Unset, list["OR32Response200OrderLinesAdjustedCancelationsShippingTaxes"]] = UNSET
    taxes: Union[Unset, list["OR32Response200OrderLinesAdjustedCancelationsTaxes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency_iso_code = self.currency_iso_code

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        quantity = self.quantity

        reason_code = self.reason_code

        shipping_amount = self.shipping_amount

        shipping_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_taxes, Unset):
            shipping_taxes = []
            for shipping_taxes_item_data in self.shipping_taxes:
                shipping_taxes_item = shipping_taxes_item_data.to_dict()
                shipping_taxes.append(shipping_taxes_item)

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if shipping_amount is not UNSET:
            field_dict["shipping_amount"] = shipping_amount
        if shipping_taxes is not UNSET:
            field_dict["shipping_taxes"] = shipping_taxes
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or32_response_200_order_lines_adjusted_cancelations_eco_contributions import (
            OR32Response200OrderLinesAdjustedCancelationsEcoContributions,
        )
        from ..models.or32_response_200_order_lines_adjusted_cancelations_shipping_taxes import (
            OR32Response200OrderLinesAdjustedCancelationsShippingTaxes,
        )
        from ..models.or32_response_200_order_lines_adjusted_cancelations_taxes import (
            OR32Response200OrderLinesAdjustedCancelationsTaxes,
        )

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR32Response200OrderLinesAdjustedCancelationsEcoContributions.from_dict(
                eco_contributions_item_data
            )

            eco_contributions.append(eco_contributions_item)

        quantity = d.pop("quantity", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        shipping_amount = d.pop("shipping_amount", UNSET)

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR32Response200OrderLinesAdjustedCancelationsShippingTaxes.from_dict(
                shipping_taxes_item_data
            )

            shipping_taxes.append(shipping_taxes_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR32Response200OrderLinesAdjustedCancelationsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        or32_response_200_order_lines_adjusted_cancelations = cls(
            amount=amount,
            currency_iso_code=currency_iso_code,
            eco_contributions=eco_contributions,
            quantity=quantity,
            reason_code=reason_code,
            shipping_amount=shipping_amount,
            shipping_taxes=shipping_taxes,
            taxes=taxes,
        )

        or32_response_200_order_lines_adjusted_cancelations.additional_properties = d
        return or32_response_200_order_lines_adjusted_cancelations

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
