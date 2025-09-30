from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or28_request_refunds_fees import OR28RequestRefundsFees
    from ..models.or28_request_refunds_shipping_taxes import OR28RequestRefundsShippingTaxes
    from ..models.or28_request_refunds_taxes import OR28RequestRefundsTaxes


T = TypeVar("T", bound="OR28RequestRefunds")


@_attrs_define
class OR28RequestRefunds:
    """List of representations of refunds to be created

    Attributes:
        amount (Union[Unset, float]): The offer part amount to be refunded.
        currency_iso_code (Union[Unset, str]): The currency (iso format) used by the shop (the field is required if the
            shop is not using the default Operator platform currency)
        excluded_from_shipment (Union[Unset, bool]): Exclude the refunded quantity from shipments
        fees (Union[Unset, list['OR28RequestRefundsFees']]): The fee part amount to be refunded
        order_line_id (Union[Unset, str]): The identifier of the order line that must be refunded
        quantity (Union[Unset, int]): The quantity of products to refund. This quantity is informative only. Default: 0.
        reason_code (Union[Unset, str]): Refund's reason code
        shipping_amount (Union[Unset, float]): The shipping charges part amount to be refunded
        shipping_taxes (Union[Unset, list['OR28RequestRefundsShippingTaxes']]): The taxes to be refunded on the shipping
            price <br/>This field is required if the order has shipping taxes.
        taxes (Union[Unset, list['OR28RequestRefundsTaxes']]): The taxes to be refunded on the product price <br/>This
            field is required if the order has taxes.
    """

    amount: Union[Unset, float] = UNSET
    currency_iso_code: Union[Unset, str] = UNSET
    excluded_from_shipment: Union[Unset, bool] = UNSET
    fees: Union[Unset, list["OR28RequestRefundsFees"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = 0
    reason_code: Union[Unset, str] = UNSET
    shipping_amount: Union[Unset, float] = UNSET
    shipping_taxes: Union[Unset, list["OR28RequestRefundsShippingTaxes"]] = UNSET
    taxes: Union[Unset, list["OR28RequestRefundsTaxes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency_iso_code = self.currency_iso_code

        excluded_from_shipment = self.excluded_from_shipment

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
        if excluded_from_shipment is not UNSET:
            field_dict["excluded_from_shipment"] = excluded_from_shipment
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
        from ..models.or28_request_refunds_fees import OR28RequestRefundsFees
        from ..models.or28_request_refunds_shipping_taxes import OR28RequestRefundsShippingTaxes
        from ..models.or28_request_refunds_taxes import OR28RequestRefundsTaxes

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency_iso_code = d.pop("currency_iso_code", UNSET)

        excluded_from_shipment = d.pop("excluded_from_shipment", UNSET)

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = OR28RequestRefundsFees.from_dict(fees_item_data)

            fees.append(fees_item)

        order_line_id = d.pop("order_line_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        shipping_amount = d.pop("shipping_amount", UNSET)

        shipping_taxes = []
        _shipping_taxes = d.pop("shipping_taxes", UNSET)
        for shipping_taxes_item_data in _shipping_taxes or []:
            shipping_taxes_item = OR28RequestRefundsShippingTaxes.from_dict(shipping_taxes_item_data)

            shipping_taxes.append(shipping_taxes_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR28RequestRefundsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        or28_request_refunds = cls(
            amount=amount,
            currency_iso_code=currency_iso_code,
            excluded_from_shipment=excluded_from_shipment,
            fees=fees,
            order_line_id=order_line_id,
            quantity=quantity,
            reason_code=reason_code,
            shipping_amount=shipping_amount,
            shipping_taxes=shipping_taxes,
            taxes=taxes,
        )

        or28_request_refunds.additional_properties = d
        return or28_request_refunds

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
