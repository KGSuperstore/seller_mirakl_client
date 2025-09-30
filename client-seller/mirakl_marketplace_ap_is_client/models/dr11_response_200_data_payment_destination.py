from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DR11Response200DataPaymentDestination")


@_attrs_define
class DR11Response200DataPaymentDestination:
    """
    Attributes:
        type_ (Union[Unset, str]):
        payment_reference (Union[Unset, str]): The payment reference for bank transfer
    """

    type_: Union[Unset, str] = UNSET
    payment_reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        payment_reference = self.payment_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["@type"] = type_
        if payment_reference is not UNSET:
            field_dict["payment_reference"] = payment_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("@type", UNSET)

        payment_reference = d.pop("payment_reference", UNSET)

        dr11_response_200_data_payment_destination = cls(
            type_=type_,
            payment_reference=payment_reference,
        )

        dr11_response_200_data_payment_destination.additional_properties = d
        return dr11_response_200_data_payment_destination

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
