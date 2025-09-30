from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IV01Response200InvoicesIssuingUser")


@_attrs_define
class IV01Response200InvoicesIssuingUser:
    """
    Attributes:
        information (Union[Unset, str]): User name if user type is OPERATOR or PARTNER, "Automatic action" if user type
            is BATCH
        type_ (Union[Unset, str]): User type (OPERATOR, BATCH or PARTNER)
    """

    information: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        information = self.information

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if information is not UNSET:
            field_dict["information"] = information
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        information = d.pop("information", UNSET)

        type_ = d.pop("type", UNSET)

        iv01_response_200_invoices_issuing_user = cls(
            information=information,
            type_=type_,
        )

        iv01_response_200_invoices_issuing_user.additional_properties = d
        return iv01_response_200_invoices_issuing_user

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
