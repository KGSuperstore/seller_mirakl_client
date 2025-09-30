from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_response_200_updated_orders_updated_order_lines import (
        OR04Response200UpdatedOrdersUpdatedOrderLines,
    )
    from ..models.or04_response_200_updated_orders_updated_references import (
        OR04Response200UpdatedOrdersUpdatedReferences,
    )


T = TypeVar("T", bound="OR04Response200UpdatedOrdersUpdated")


@_attrs_define
class OR04Response200UpdatedOrdersUpdated:
    """
    Attributes:
        order_lines (Union[Unset, list['OR04Response200UpdatedOrdersUpdatedOrderLines']]): Details of the modified order
            line
        references (Union[Unset, OR04Response200UpdatedOrdersUpdatedReferences]):
    """

    order_lines: Union[Unset, list["OR04Response200UpdatedOrdersUpdatedOrderLines"]] = UNSET
    references: Union[Unset, "OR04Response200UpdatedOrdersUpdatedReferences"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            order_lines = []
            for order_lines_item_data in self.order_lines:
                order_lines_item = order_lines_item_data.to_dict()
                order_lines.append(order_lines_item)

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_lines is not UNSET:
            field_dict["order_lines"] = order_lines
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_response_200_updated_orders_updated_order_lines import (
            OR04Response200UpdatedOrdersUpdatedOrderLines,
        )
        from ..models.or04_response_200_updated_orders_updated_references import (
            OR04Response200UpdatedOrdersUpdatedReferences,
        )

        d = dict(src_dict)
        order_lines = []
        _order_lines = d.pop("order_lines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = OR04Response200UpdatedOrdersUpdatedOrderLines.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        _references = d.pop("references", UNSET)
        references: Union[Unset, OR04Response200UpdatedOrdersUpdatedReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = OR04Response200UpdatedOrdersUpdatedReferences.from_dict(_references)

        or04_response_200_updated_orders_updated = cls(
            order_lines=order_lines,
            references=references,
        )

        or04_response_200_updated_orders_updated.additional_properties = d
        return or04_response_200_updated_orders_updated

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
