from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or30_response_200_cancelations_amount_breakdown import OR30Response200CancelationsAmountBreakdown
    from ..models.or30_response_200_cancelations_eco_contributions import OR30Response200CancelationsEcoContributions
    from ..models.or30_response_200_cancelations_fees import OR30Response200CancelationsFees
    from ..models.or30_response_200_cancelations_purchase_information import (
        OR30Response200CancelationsPurchaseInformation,
    )
    from ..models.or30_response_200_cancelations_shipping_amount_breakdown import (
        OR30Response200CancelationsShippingAmountBreakdown,
    )
    from ..models.or30_response_200_cancelations_shipping_taxes import OR30Response200CancelationsShippingTaxes
    from ..models.or30_response_200_cancelations_taxes import OR30Response200CancelationsTaxes


T = TypeVar("T", bound="OR30Response200Cancelations")


@_attrs_define
class OR30Response200Cancelations:
    """
    Attributes:
        amount (Union[Unset, float]): The offer part amount of the cancellation
        amount_breakdown (Union[Unset, OR30Response200CancelationsAmountBreakdown]):
        cancelation_id (Union[Unset, str]): The identifier of the created cancellation
        currency_iso_code (Union[Unset, str]): The currency (iso format) used by the shop (the field is required if the
            shop is not using the default Operator platform currency)
        eco_contributions (Union[Unset, list['OR30Response200CancelationsEcoContributions']]): List of eco-contribution
            amounts and corresponding producer identifiers, if applicable<br/>
            Only available if the operator activates the circular economy information collection.
        fees (Union[Unset, list['OR30Response200CancelationsFees']]): List of fees canceled on the order line
        order_line_id (Union[Unset, str]): Order line's identifier on which the cancellation has been created
        purchase_information (Union[Unset, OR30Response200CancelationsPurchaseInformation]):
        quantity (Union[Unset, int]): The quantity of canceled goods
        reason_code (Union[Unset, str]): Cancellation's reason code
        shipping_amount (Union[Unset, float]): The shipping charges part amount of the cancellation
        shipping_amount_breakdown (Union[Unset, OR30Response200CancelationsShippingAmountBreakdown]):
        shipping_taxes (Union[Unset, list['OR30Response200CancelationsShippingTaxes']]): List of taxes canceled on
            shipping charges
        taxes (Union[Unset, list['OR30Response200CancelationsTaxes']]): List of taxes canceled on product price
    """

    amount: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "OR30Response200CancelationsAmountBreakdown"] = UNSET
    cancelation_id: Union[Unset, str] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    eco_contributions: Union[Unset, list["OR30Response200CancelationsEcoContributions"]] = UNSET
    fees: Union[Unset, list["OR30Response200CancelationsFees"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    purchase_information: Union[Unset, "OR30Response200CancelationsPurchaseInformation"] = UNSET
    quantity: Union[Unset, int] = UNSET
    reason_code: Union[Unset, str] = UNSET
    shipping_amount: Union[Unset, float] = UNSET
    shipping_amount_breakdown: Union[Unset, "OR30Response200CancelationsShippingAmountBreakdown"] = UNSET
    shipping_taxes: Union[Unset, list["OR30Response200CancelationsShippingTaxes"]] = UNSET
    taxes: Union[Unset, list["OR30Response200CancelationsTaxes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.amount_breakdown, Unset):
            amount_breakdown = self.amount_breakdown.to_dict()

        cancelation_id = self.cancelation_id

        currency_iso_code = self.currency_iso_code

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        fees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)

        order_line_id = self.order_line_id

        purchase_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_information, Unset):
            purchase_information = self.purchase_information.to_dict()

        quantity = self.quantity

        reason_code = self.reason_code

        shipping_amount = self.shipping_amount

        shipping_amount_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping_amount_breakdown, Unset):
            shipping_amount_breakdown = self.shipping_amount_breakdown.to_dict()

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
        if amount_breakdown is not UNSET:
            field_dict["amount_breakdown"] = amount_breakdown
        if cancelation_id is not UNSET:
            field_dict["cancelation_id"] = cancelation_id
        if currency_iso_code is not UNSET:
            field_dict["currency_iso_code"] = currency_iso_code
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if fees is not UNSET:
            field_dict["fees"] = fees
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if purchase_information is not UNSET:
            field_dict["purchase_information"] = purchase_information
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if shipping_amount is not UNSET:
            field_dict["shipping_amount"] = shipping_amount
        if shipping_amount_breakdown is not UNSET:
            field_dict["shipping_amount_breakdown"] = shipping_amount_breakdown
        if shipping_taxes is not UNSET:
            field_dict["shipping_taxes"] = shipping_taxes
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or30_response_200_cancelations_amount_breakdown import OR30Response200CancelationsAmountBreakdown
        from ..models.or30_response_200_cancelations_eco_contributions import (
            OR30Response200CancelationsEcoContributions,
        )
        from ..models.or30_response_200_cancelations_fees import OR30Response200CancelationsFees
        from ..models.or30_response_200_cancelations_purchase_information import (
            OR30Response200CancelationsPurchaseInformation,
        )
        from ..models.or30_response_200_cancelations_shipping_amount_breakdown import (
            OR30Response200CancelationsShippingAmountBreakdown,
        )
        from ..models.or30_response_200_cancelations_shipping_taxes import OR30Response200CancelationsShippingTaxes
        from ..models.or30_response_200_cancelations_taxes import OR30Response200CancelationsTaxes

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _amount_breakdown = d.pop("amount_breakdown", UNSET)
        amount_breakdown: Union[Unset, OR30Response200CancelationsAmountBreakdown]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = OR30Response200CancelationsAmountBreakdown.from_dict(_amount_breakdown)

        cancelation_id = d.pop("cancelation_id", UNSET)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR30Response200CancelationsEcoContributions.from_dict(eco_contributions_item_data)

            eco_contributions.append(eco_contributions_item)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = OR30Response200CancelationsFees.from_dict(fees_item_data)

            fees.append(fees_item)

        order_line_id = d.pop("order_line_id", UNSET)

        _purchase_information = d.pop("purchase_information", UNSET)
        purchase_information: Union[Unset, OR30Response200CancelationsPurchaseInformation]
        if isinstance(_purchase_information, Unset):
            purchase_information = UNSET
        else:
            purchase_information = OR30Response200CancelationsPurchaseInformation.from_dict(_purchase_information)

        quantity = d.pop("quantity", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        shipping_amount = d.pop("shipping_amount", UNSET)

        _shipping_amount_breakdown = d.pop("shipping_amount_breakdown", UNSET)
        shipping_amount_breakdown: Union[Unset, OR30Response200CancelationsShippingAmountBreakdown]
        if isinstance(_shipping_amount_breakdown, Unset):
            shipping_amount_breakdown = UNSET
        else:
            shipping_amount_breakdown = OR30Response200CancelationsShippingAmountBreakdown.from_dict(
                _shipping_amount_breakdown
            )

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR30Response200CancelationsShippingTaxes.from_dict(shipping_taxes_item_data)

            shipping_taxes.append(shipping_taxes_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR30Response200CancelationsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        or30_response_200_cancelations = cls(
            amount=amount,
            amount_breakdown=amount_breakdown,
            cancelation_id=cancelation_id,
            currency_iso_code=currency_iso_code,
            eco_contributions=eco_contributions,
            fees=fees,
            order_line_id=order_line_id,
            purchase_information=purchase_information,
            quantity=quantity,
            reason_code=reason_code,
            shipping_amount=shipping_amount,
            shipping_amount_breakdown=shipping_amount_breakdown,
            shipping_taxes=shipping_taxes,
            taxes=taxes,
        )

        or30_response_200_cancelations.additional_properties = d
        return or30_response_200_cancelations

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
