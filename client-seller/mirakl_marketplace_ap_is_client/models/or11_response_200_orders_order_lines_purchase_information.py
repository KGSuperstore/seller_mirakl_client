from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_lines_purchase_information_purchase_commission_on_fees import (
        OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees,
    )
    from ..models.or11_response_200_orders_order_lines_purchase_information_purchase_fee_amount import (
        OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount,
    )


T = TypeVar("T", bound="OR11Response200OrdersOrderLinesPurchaseInformation")


@_attrs_define
class OR11Response200OrdersOrderLinesPurchaseInformation:
    """
    Attributes:
        purchase_commission_on_fees (Union[Unset,
            OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees]):
        purchase_commission_on_price (Union[Unset, float]): Purchase order line’s commission amount
        purchase_commission_on_shipping (Union[Unset, float]): Purchase order line’s commission amount on shipping
        purchase_fee_amount (Union[Unset, OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount]):
        purchase_price (Union[Unset, float]): Purchase order line’s price excluding shipping charges and fees
        purchase_shipping_price (Union[Unset, float]): Purchase order line’s shipping charges
        purchase_unit_price (Union[Unset, float]): Purchase unit price computed from the given offer price
    """

    purchase_commission_on_fees: Union[
        Unset, "OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees"
    ] = UNSET
    purchase_commission_on_price: Union[Unset, float] = UNSET
    purchase_commission_on_shipping: Union[Unset, float] = UNSET
    purchase_fee_amount: Union[Unset, "OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount"] = UNSET
    purchase_price: Union[Unset, float] = UNSET
    purchase_shipping_price: Union[Unset, float] = UNSET
    purchase_unit_price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_commission_on_fees: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_commission_on_fees, Unset):
            purchase_commission_on_fees = self.purchase_commission_on_fees.to_dict()

        purchase_commission_on_price = self.purchase_commission_on_price

        purchase_commission_on_shipping = self.purchase_commission_on_shipping

        purchase_fee_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_fee_amount, Unset):
            purchase_fee_amount = self.purchase_fee_amount.to_dict()

        purchase_price = self.purchase_price

        purchase_shipping_price = self.purchase_shipping_price

        purchase_unit_price = self.purchase_unit_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_commission_on_fees is not UNSET:
            field_dict["purchase_commission_on_fees"] = purchase_commission_on_fees
        if purchase_commission_on_price is not UNSET:
            field_dict["purchase_commission_on_price"] = purchase_commission_on_price
        if purchase_commission_on_shipping is not UNSET:
            field_dict["purchase_commission_on_shipping"] = purchase_commission_on_shipping
        if purchase_fee_amount is not UNSET:
            field_dict["purchase_fee_amount"] = purchase_fee_amount
        if purchase_price is not UNSET:
            field_dict["purchase_price"] = purchase_price
        if purchase_shipping_price is not UNSET:
            field_dict["purchase_shipping_price"] = purchase_shipping_price
        if purchase_unit_price is not UNSET:
            field_dict["purchase_unit_price"] = purchase_unit_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_order_lines_purchase_information_purchase_commission_on_fees import (
            OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees,
        )
        from ..models.or11_response_200_orders_order_lines_purchase_information_purchase_fee_amount import (
            OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount,
        )

        d = dict(src_dict)
        _purchase_commission_on_fees = d.pop("purchase_commission_on_fees", UNSET)
        purchase_commission_on_fees: Union[
            Unset, OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees
        ]
        if isinstance(_purchase_commission_on_fees, Unset):
            purchase_commission_on_fees = UNSET
        else:
            purchase_commission_on_fees = (
                OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees.from_dict(
                    _purchase_commission_on_fees
                )
            )

        purchase_commission_on_price = d.pop("purchase_commission_on_price", UNSET)

        purchase_commission_on_shipping = d.pop("purchase_commission_on_shipping", UNSET)

        _purchase_fee_amount = d.pop("purchase_fee_amount", UNSET)
        purchase_fee_amount: Union[Unset, OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount]
        if isinstance(_purchase_fee_amount, Unset):
            purchase_fee_amount = UNSET
        else:
            purchase_fee_amount = OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount.from_dict(
                _purchase_fee_amount
            )

        purchase_price = d.pop("purchase_price", UNSET)

        purchase_shipping_price = d.pop("purchase_shipping_price", UNSET)

        purchase_unit_price = d.pop("purchase_unit_price", UNSET)

        or11_response_200_orders_order_lines_purchase_information = cls(
            purchase_commission_on_fees=purchase_commission_on_fees,
            purchase_commission_on_price=purchase_commission_on_price,
            purchase_commission_on_shipping=purchase_commission_on_shipping,
            purchase_fee_amount=purchase_fee_amount,
            purchase_price=purchase_price,
            purchase_shipping_price=purchase_shipping_price,
            purchase_unit_price=purchase_unit_price,
        )

        or11_response_200_orders_order_lines_purchase_information.additional_properties = d
        return or11_response_200_orders_order_lines_purchase_information

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
