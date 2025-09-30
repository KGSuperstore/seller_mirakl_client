from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TL02Response200DataEntitiesOrderPaymentInfo")


@_attrs_define
class TL02Response200DataEntitiesOrderPaymentInfo:
    """
    Attributes:
        imprint_number (Union[Unset, str]): The payment imprint number received by OR01 or SOR01
        payment_type (Union[Unset, str]): The payment's type used by the customer to pay this order
    """

    imprint_number: Union[Unset, str] = UNSET
    payment_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imprint_number = self.imprint_number

        payment_type = self.payment_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if imprint_number is not UNSET:
            field_dict["imprint_number"] = imprint_number
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        imprint_number = d.pop("imprint_number", UNSET)

        payment_type = d.pop("payment_type", UNSET)

        tl02_response_200_data_entities_order_payment_info = cls(
            imprint_number=imprint_number,
            payment_type=payment_type,
        )

        tl02_response_200_data_entities_order_payment_info.additional_properties = d
        return tl02_response_200_data_entities_order_payment_info

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
