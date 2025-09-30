from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_request_orders_order_lines import OR04RequestOrdersOrderLines
    from ..models.or04_request_orders_references import OR04RequestOrdersReferences


T = TypeVar("T", bound="OR04RequestOrders")


@_attrs_define
class OR04RequestOrders:
    """Orders to be updated, maximum number of orders per call: 100

    Attributes:
        order_id (Union[Unset, str]): Order identifier
        order_lines (Union[Unset, list['OR04RequestOrdersOrderLines']]): Order lines to be updated
        references (Union[Unset, OR04RequestOrdersReferences]): Order references
    """

    order_id: Union[Unset, str] = UNSET
    order_lines: Union[Unset, list["OR04RequestOrdersOrderLines"]] = UNSET
    references: Union[Unset, "OR04RequestOrdersReferences"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

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
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_lines is not UNSET:
            field_dict["order_lines"] = order_lines
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_request_orders_order_lines import OR04RequestOrdersOrderLines
        from ..models.or04_request_orders_references import OR04RequestOrdersReferences

        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        order_lines = []
        _order_lines = d.pop("order_lines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = OR04RequestOrdersOrderLines.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        _references = d.pop("references", UNSET)
        references: Union[Unset, OR04RequestOrdersReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = OR04RequestOrdersReferences.from_dict(_references)

        or04_request_orders = cls(
            order_id=order_id,
            order_lines=order_lines,
            references=references,
        )

        or04_request_orders.additional_properties = d
        return or04_request_orders

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
