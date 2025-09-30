from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or21_request_order_lines import OR21RequestOrderLines


T = TypeVar("T", bound="OR21Request")


@_attrs_define
class OR21Request:
    """
    Attributes:
        order_lines (Union[Unset, list['OR21RequestOrderLines']]): List of representations of order line for acceptance
    """

    order_lines: Union[Unset, list["OR21RequestOrderLines"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            order_lines = []
            for order_lines_item_data in self.order_lines:
                order_lines_item = order_lines_item_data.to_dict()
                order_lines.append(order_lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_lines is not UNSET:
            field_dict["order_lines"] = order_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or21_request_order_lines import OR21RequestOrderLines

        d = dict(src_dict)
        order_lines = []
        _order_lines = d.pop("order_lines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = OR21RequestOrderLines.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        or21_request = cls(
            order_lines=order_lines,
        )

        or21_request.additional_properties = d
        return or21_request

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
