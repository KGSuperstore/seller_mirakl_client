from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or07_response_200_order_lines_errors import OR07Response200OrderLinesErrors
    from ..models.or07_response_200_order_lines_updated import OR07Response200OrderLinesUpdated


T = TypeVar("T", bound="OR07Response200OrderLines")


@_attrs_define
class OR07Response200OrderLines:
    """
    Attributes:
        errors (Union[Unset, list['OR07Response200OrderLinesErrors']]): List of errors encountered when updating the
            shipping_from data on order line
        id (Union[Unset, str]): Order line identifier
        updated (Union[Unset, OR07Response200OrderLinesUpdated]):
    """

    errors: Union[Unset, list["OR07Response200OrderLinesErrors"]] = UNSET
    id: Union[Unset, str] = UNSET
    updated: Union[Unset, "OR07Response200OrderLinesUpdated"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        id = self.id

        updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if id is not UNSET:
            field_dict["id"] = id
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or07_response_200_order_lines_errors import OR07Response200OrderLinesErrors
        from ..models.or07_response_200_order_lines_updated import OR07Response200OrderLinesUpdated

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = OR07Response200OrderLinesErrors.from_dict(errors_item_data)

            errors.append(errors_item)

        id = d.pop("id", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, OR07Response200OrderLinesUpdated]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = OR07Response200OrderLinesUpdated.from_dict(_updated)

        or07_response_200_order_lines = cls(
            errors=errors,
            id=id,
            updated=updated,
        )

        or07_response_200_order_lines.additional_properties = d
        return or07_response_200_order_lines

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
