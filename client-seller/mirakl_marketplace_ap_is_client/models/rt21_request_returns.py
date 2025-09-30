from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RT21RequestReturns")


@_attrs_define
class RT21RequestReturns:
    """Returns to be accepted, maximum number of returns per call: 100

    Attributes:
        accepted (Union[Unset, bool]): Boolean indicating if the return is accepted or refused
        id (Union[Unset, str]): Return id
        rejection_reason_code (Union[Unset, str]): Return rejection reason code
    """

    accepted: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    rejection_reason_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        id = self.id

        rejection_reason_code = self.rejection_reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if id is not UNSET:
            field_dict["id"] = id
        if rejection_reason_code is not UNSET:
            field_dict["rejection_reason_code"] = rejection_reason_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted", UNSET)

        id = d.pop("id", UNSET)

        rejection_reason_code = d.pop("rejection_reason_code", UNSET)

        rt21_request_returns = cls(
            accepted=accepted,
            id=id,
            rejection_reason_code=rejection_reason_code,
        )

        rt21_request_returns.additional_properties = d
        return rt21_request_returns

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
