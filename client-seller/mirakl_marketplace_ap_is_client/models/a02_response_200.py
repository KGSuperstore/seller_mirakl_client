from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a02_response_200_errors import A02Response200Errors
    from ..models.a02_response_200_updated import A02Response200Updated


T = TypeVar("T", bound="A02Response200")


@_attrs_define
class A02Response200:
    """
    Attributes:
        errors (Union[Unset, list['A02Response200Errors']]): List of errors encountered when updating the shop
        updated (Union[Unset, A02Response200Updated]):
    """

    errors: Union[Unset, list["A02Response200Errors"]] = UNSET
    updated: Union[Unset, "A02Response200Updated"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a02_response_200_errors import A02Response200Errors
        from ..models.a02_response_200_updated import A02Response200Updated

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = A02Response200Errors.from_dict(errors_item_data)

            errors.append(errors_item)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, A02Response200Updated]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = A02Response200Updated.from_dict(_updated)

        a02_response_200 = cls(
            errors=errors,
            updated=updated,
        )

        a02_response_200.additional_properties = d
        return a02_response_200

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
