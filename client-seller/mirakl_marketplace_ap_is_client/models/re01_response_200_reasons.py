from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RE01Response200Reasons")


@_attrs_define
class RE01Response200Reasons:
    """
    Attributes:
        code (Union[Unset, str]): Reason code
        is_shop_right (Union[Unset, bool]): Indicate if reason is enabled to the shop
        label (Union[Unset, str]): Reason label
        type_ (Union[Unset, str]): Type of the reason
    """

    code: Union[Unset, str] = UNSET
    is_shop_right: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        is_shop_right = self.is_shop_right

        label = self.label

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if is_shop_right is not UNSET:
            field_dict["is_shop_right"] = is_shop_right
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        is_shop_right = d.pop("is_shop_right", UNSET)

        label = d.pop("label", UNSET)

        type_ = d.pop("type", UNSET)

        re01_response_200_reasons = cls(
            code=code,
            is_shop_right=is_shop_right,
            label=label,
            type_=type_,
        )

        re01_response_200_reasons.additional_properties = d
        return re01_response_200_reasons

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
