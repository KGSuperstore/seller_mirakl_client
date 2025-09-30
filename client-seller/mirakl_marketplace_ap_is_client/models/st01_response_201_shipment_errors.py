from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ST01Response201ShipmentErrors")


@_attrs_define
class ST01Response201ShipmentErrors:
    """
    Attributes:
        message (Union[Unset, str]): Shipment error creation message
        order_id (Union[Unset, str]): Order id of the shipment creation error
    """

    message: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        order_id = self.order_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if order_id is not UNSET:
            field_dict["order_id"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        order_id = d.pop("order_id", UNSET)

        st01_response_201_shipment_errors = cls(
            message=message,
            order_id=order_id,
        )

        st01_response_201_shipment_errors.additional_properties = d
        return st01_response_201_shipment_errors

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
