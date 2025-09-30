from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RT26RequestReturnsReturnLines")


@_attrs_define
class RT26RequestReturnsReturnLines:
    """Return lines

    Attributes:
        compliant (Union[Unset, bool]): Compliant
        non_compliance_additional_info (Union[Unset, str]): Non-compliance additional information
        non_compliance_reason_code (Union[Unset, str]): Non-compliance reason code
        order_line_id (Union[Unset, str]): Order line id
    """

    compliant: Union[Unset, bool] = UNSET
    non_compliance_additional_info: Union[Unset, str] = UNSET
    non_compliance_reason_code: Union[Unset, str] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compliant = self.compliant

        non_compliance_additional_info = self.non_compliance_additional_info

        non_compliance_reason_code = self.non_compliance_reason_code

        order_line_id = self.order_line_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliant is not UNSET:
            field_dict["compliant"] = compliant
        if non_compliance_additional_info is not UNSET:
            field_dict["non_compliance_additional_info"] = non_compliance_additional_info
        if non_compliance_reason_code is not UNSET:
            field_dict["non_compliance_reason_code"] = non_compliance_reason_code
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        compliant = d.pop("compliant", UNSET)

        non_compliance_additional_info = d.pop("non_compliance_additional_info", UNSET)

        non_compliance_reason_code = d.pop("non_compliance_reason_code", UNSET)

        order_line_id = d.pop("order_line_id", UNSET)

        rt26_request_returns_return_lines = cls(
            compliant=compliant,
            non_compliance_additional_info=non_compliance_additional_info,
            non_compliance_reason_code=non_compliance_reason_code,
            order_line_id=order_line_id,
        )

        rt26_request_returns_return_lines.additional_properties = d
        return rt26_request_returns_return_lines

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
