from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or30_request_cancelations_fees import OR30RequestCancelationsFees
    from ..models.or30_request_cancelations_shipping_taxes import OR30RequestCancelationsShippingTaxes
    from ..models.or30_request_cancelations_taxes import OR30RequestCancelationsTaxes


T = TypeVar("T", bound="OR30RequestCancelations")


@_attrs_define
class OR30RequestCancelations:
    """List of representations of cancellations to be created

    Attributes:
        amount (Union[Unset, float]): The offer part amount to be canceled
        currency_iso_code (Union[Unset, str]): The currency (iso format) used by the shop (the field is required if the
            shop is not using the default Operator platform currency)
        fees (Union[Unset, list['OR30RequestCancelationsFees']]): The fees to be canceled
        order_line_id (Union[Unset, str]): Order line's identifier that must be canceled
        quantity (Union[Unset, int]): The quantity of goods to cancel
        reason_code (Union[Unset, str]): Cancellation's reason code
        shipping_amount (Union[Unset, float]): The shipping charges part amount to be canceled
        shipping_taxes (Union[Unset, list['OR30RequestCancelationsShippingTaxes']]): The taxes to be canceled on the
            shipping price (this field is required if the order has shipping taxes)
        taxes (Union[Unset, list['OR30RequestCancelationsTaxes']]): The taxes to be canceled on the product price (this
            field is required if the order has taxes)
    """

    amount: Union[Unset, float] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    fees: Union[Unset, list["OR30RequestCancelationsFees"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    reason_code: Union[Unset, str] = UNSET
    shipping_amount: Union[Unset, float] = UNSET
    shipping_taxes: Union[Unset, list["OR30RequestCancelationsShippingTaxes"]] = UNSET
    taxes: Union[Unset, list["OR30RequestCancelationsTaxes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency_iso_code = self.currency_iso_code

        fees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)

        order_line_id = self.order_line_id

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
        if fees is not UNSET:
            field_dict["fees"] = fees
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
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
        from ..models.or30_request_cancelations_fees import OR30RequestCancelationsFees
        from ..models.or30_request_cancelations_shipping_taxes import OR30RequestCancelationsShippingTaxes
        from ..models.or30_request_cancelations_taxes import OR30RequestCancelationsTaxes

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = OR30RequestCancelationsFees.from_dict(fees_item_data)

            fees.append(fees_item)

        order_line_id = d.pop("order_line_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        shipping_amount = d.pop("shipping_amount", UNSET)

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR30RequestCancelationsShippingTaxes.from_dict(shipping_taxes_item_data)

            shipping_taxes.append(shipping_taxes_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR30RequestCancelationsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        or30_request_cancelations = cls(
            amount=amount,
            currency_iso_code=currency_iso_code,
            fees=fees,
            order_line_id=order_line_id,
            quantity=quantity,
            reason_code=reason_code,
            shipping_amount=shipping_amount,
            shipping_taxes=shipping_taxes,
            taxes=taxes,
        )

        or30_request_cancelations.additional_properties = d
        return or30_request_cancelations

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
