from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ST31Response200ShipmentUpdateErrorsErrors")


@_attrs_define
class ST31Response200ShipmentUpdateErrorsErrors:
    """
    Attributes:
        code (Union[Unset, str]): Error code
        field (Union[Unset, str]): Name of the field on the input object. Can be composed, e.g.: address.zip_code
        message (Union[Unset, str]): Error message
    """

    code: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        field = self.field

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        field = d.pop("field", UNSET)

        message = d.pop("message", UNSET)

        st31_response_200_shipment_update_errors_errors = cls(
            code=code,
            field=field,
            message=message,
        )

        st31_response_200_shipment_update_errors_errors.additional_properties = d
        return st31_response_200_shipment_update_errors_errors

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
