from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rt26_request_returns_return_lines import RT26RequestReturnsReturnLines


T = TypeVar("T", bound="RT26RequestReturns")


@_attrs_define
class RT26RequestReturns:
    """Mark returns as compliant or non-compliant, maximum number of returns per call: 100

    Attributes:
        id (Union[Unset, str]): Return id
        return_lines (Union[Unset, list['RT26RequestReturnsReturnLines']]): Return lines
    """

    id: Union[Unset, str] = UNSET
    return_lines: Union[Unset, list["RT26RequestReturnsReturnLines"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        return_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.return_lines, Unset):
            return_lines = []
            for return_lines_item_data in self.return_lines:
                return_lines_item = return_lines_item_data.to_dict()
                return_lines.append(return_lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if return_lines is not UNSET:
            field_dict["return_lines"] = return_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rt26_request_returns_return_lines import RT26RequestReturnsReturnLines

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        return_lines = []
        _return_lines = d.pop("return_lines", UNSET)
        for return_lines_item_data in _return_lines or []:
            return_lines_item = RT26RequestReturnsReturnLines.from_dict(return_lines_item_data)

            return_lines.append(return_lines_item)

        rt26_request_returns = cls(
            id=id,
            return_lines=return_lines,
        )

        rt26_request_returns.additional_properties = d
        return rt26_request_returns

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
