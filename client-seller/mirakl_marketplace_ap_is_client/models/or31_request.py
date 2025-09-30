from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or31_request_order_additional_fields import OR31RequestOrderAdditionalFields
    from ..models.or31_request_order_lines import OR31RequestOrderLines


T = TypeVar("T", bound="OR31Request")


@_attrs_define
class OR31Request:
    """
    Attributes:
        order_additional_fields (Union[Unset, list['OR31RequestOrderAdditionalFields']]): Order custom fields
        order_lines (Union[Unset, list['OR31RequestOrderLines']]): Order lines custom fields
    """

    order_additional_fields: Union[Unset, list["OR31RequestOrderAdditionalFields"]] = UNSET
    order_lines: Union[Unset, list["OR31RequestOrderLines"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_additional_fields, Unset):
            order_additional_fields = []
            for order_additional_fields_item_data in self.order_additional_fields:
                order_additional_fields_item = order_additional_fields_item_data.to_dict()
                order_additional_fields.append(order_additional_fields_item)

        order_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            order_lines = []
            for order_lines_item_data in self.order_lines:
                order_lines_item = order_lines_item_data.to_dict()
                order_lines.append(order_lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_additional_fields is not UNSET:
            field_dict["order_additional_fields"] = order_additional_fields
        if order_lines is not UNSET:
            field_dict["order_lines"] = order_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or31_request_order_additional_fields import OR31RequestOrderAdditionalFields
        from ..models.or31_request_order_lines import OR31RequestOrderLines

        d = dict(src_dict)
        order_additional_fields = []
        _order_additional_fields = d.pop("order_additional_fields", UNSET)
        for order_additional_fields_item_data in _order_additional_fields or []:
            order_additional_fields_item = OR31RequestOrderAdditionalFields.from_dict(order_additional_fields_item_data)

            order_additional_fields.append(order_additional_fields_item)

        order_lines = []
        _order_lines = d.pop("order_lines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = OR31RequestOrderLines.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        or31_request = cls(
            order_additional_fields=order_additional_fields,
            order_lines=order_lines,
        )

        or31_request.additional_properties = d
        return or31_request

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
