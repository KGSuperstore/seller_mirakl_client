from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or30_response_200_cancelations_purchase_information_purchase_commission_on_fees import (
        OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees,
    )
    from ..models.or30_response_200_cancelations_purchase_information_purchase_fee_amount import (
        OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount,
    )


T = TypeVar("T", bound="OR30Response200CancelationsPurchaseInformation")


@_attrs_define
class OR30Response200CancelationsPurchaseInformation:
    """
    Attributes:
        purchase_commission_on_fees (Union[Unset,
            OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees]):
        purchase_commission_on_price (Union[Unset, float]): Cancelation’s purchase commission amount
        purchase_commission_on_shipping (Union[Unset, float]): Cancelation’s purchase commission amount on shipping
        purchase_fee_amount (Union[Unset, OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount]):
        purchase_price (Union[Unset, float]): Cancelation’s purchase price excluding shipping charges and fees
        purchase_shipping_price (Union[Unset, float]): Cancelation’s purchase shipping charges
    """

    purchase_commission_on_fees: Union[
        Unset, "OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees"
    ] = UNSET
    purchase_commission_on_price: Union[Unset, float] = UNSET
    purchase_commission_on_shipping: Union[Unset, float] = UNSET
    purchase_fee_amount: Union[Unset, "OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount"] = UNSET
    purchase_price: Union[Unset, float] = UNSET
    purchase_shipping_price: Union[Unset, float] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or30_response_200_cancelations_purchase_information_purchase_commission_on_fees import (
            OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees,
        )
        from ..models.or30_response_200_cancelations_purchase_information_purchase_fee_amount import (
            OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount,
        )

        d = dict(src_dict)
        _purchase_commission_on_fees = d.pop("purchase_commission_on_fees", UNSET)
        purchase_commission_on_fees: Union[
            Unset, OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees
        ]
        if isinstance(_purchase_commission_on_fees, Unset):
            purchase_commission_on_fees = UNSET
        else:
            purchase_commission_on_fees = (
                OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees.from_dict(
                    _purchase_commission_on_fees
                )
            )

        purchase_commission_on_price = d.pop("purchase_commission_on_price", UNSET)

        purchase_commission_on_shipping = d.pop("purchase_commission_on_shipping", UNSET)

        _purchase_fee_amount = d.pop("purchase_fee_amount", UNSET)
        purchase_fee_amount: Union[Unset, OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount]
        if isinstance(_purchase_fee_amount, Unset):
            purchase_fee_amount = UNSET
        else:
            purchase_fee_amount = OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount.from_dict(
                _purchase_fee_amount
            )

        purchase_price = d.pop("purchase_price", UNSET)

        purchase_shipping_price = d.pop("purchase_shipping_price", UNSET)

        or30_response_200_cancelations_purchase_information = cls(
            purchase_commission_on_fees=purchase_commission_on_fees,
            purchase_commission_on_price=purchase_commission_on_price,
            purchase_commission_on_shipping=purchase_commission_on_shipping,
            purchase_fee_amount=purchase_fee_amount,
            purchase_price=purchase_price,
            purchase_shipping_price=purchase_shipping_price,
        )

        or30_response_200_cancelations_purchase_information.additional_properties = d
        return or30_response_200_cancelations_purchase_information

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
