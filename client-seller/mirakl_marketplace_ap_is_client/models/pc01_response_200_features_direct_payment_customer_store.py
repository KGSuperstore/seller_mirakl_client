from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200FeaturesDirectPaymentCustomerStore")


@_attrs_define
class PC01Response200FeaturesDirectPaymentCustomerStore:
    """
    Attributes:
        activated (Union[Unset, bool]): Direct payment customer store activated
        refund_cancel_authorized (Union[Unset, bool]): Allows refund and cancelation for transactions taking place
            outside of Mirakl between customers and sellers
    """

    activated: Union[Unset, bool] = UNSET
    refund_cancel_authorized: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activated = self.activated

        refund_cancel_authorized = self.refund_cancel_authorized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activated is not UNSET:
            field_dict["activated"] = activated
        if refund_cancel_authorized is not UNSET:
            field_dict["refund_cancel_authorized"] = refund_cancel_authorized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activated = d.pop("activated", UNSET)

        refund_cancel_authorized = d.pop("refund_cancel_authorized", UNSET)

        pc01_response_200_features_direct_payment_customer_store = cls(
            activated=activated,
            refund_cancel_authorized=refund_cancel_authorized,
        )

        pc01_response_200_features_direct_payment_customer_store.additional_properties = d
        return pc01_response_200_features_direct_payment_customer_store

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
