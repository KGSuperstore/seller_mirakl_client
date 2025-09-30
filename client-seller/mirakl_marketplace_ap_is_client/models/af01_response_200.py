from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.af01_response_200_additional_fields import AF01Response200AdditionalFields


T = TypeVar("T", bound="AF01Response200")


@_attrs_define
class AF01Response200:
    """
    Attributes:
        additional_fields (Union[Unset, list['AF01Response200AdditionalFields']]):
    """

    additional_fields: Union[Unset, list["AF01Response200AdditionalFields"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_fields, Unset):
            additional_fields = []
            for additional_fields_item_data in self.additional_fields:
                additional_fields_item = additional_fields_item_data.to_dict()
                additional_fields.append(additional_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_fields is not UNSET:
            field_dict["additional_fields"] = additional_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.af01_response_200_additional_fields import AF01Response200AdditionalFields

        d = dict(src_dict)
        additional_fields = []
        _additional_fields = d.pop("additional_fields", UNSET)
        for additional_fields_item_data in _additional_fields or []:
            additional_fields_item = AF01Response200AdditionalFields.from_dict(additional_fields_item_data)

            additional_fields.append(additional_fields_item)

        af01_response_200 = cls(
            additional_fields=additional_fields,
        )

        af01_response_200.additional_properties = d
        return af01_response_200

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
