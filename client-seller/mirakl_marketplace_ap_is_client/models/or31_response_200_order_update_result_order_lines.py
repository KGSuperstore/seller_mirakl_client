from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or31_response_200_order_update_result_order_lines_order_line_additional_fields import (
        OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields,
    )


T = TypeVar("T", bound="OR31Response200OrderUpdateResultOrderLines")


@_attrs_define
class OR31Response200OrderUpdateResultOrderLines:
    """
    Attributes:
        order_line_additional_fields (Union[Unset,
            list['OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields']]): Order line custom fields
        order_line_id (Union[Unset, str]): Order line identifier
    """

    order_line_additional_fields: Union[
        Unset, list["OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields"]
    ] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_line_additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_line_additional_fields, Unset):
            order_line_additional_fields = []
            for order_line_additional_fields_item_data in self.order_line_additional_fields:
                order_line_additional_fields_item = order_line_additional_fields_item_data.to_dict()
                order_line_additional_fields.append(order_line_additional_fields_item)

        order_line_id = self.order_line_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_line_additional_fields is not UNSET:
            field_dict["order_line_additional_fields"] = order_line_additional_fields
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or31_response_200_order_update_result_order_lines_order_line_additional_fields import (
            OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields,
        )

        d = dict(src_dict)
        order_line_additional_fields = []
        _order_line_additional_fields = d.pop("order_line_additional_fields", UNSET)
        for order_line_additional_fields_item_data in _order_line_additional_fields or []:
            order_line_additional_fields_item = (
                OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields.from_dict(
                    order_line_additional_fields_item_data
                )
            )

            order_line_additional_fields.append(order_line_additional_fields_item)

        order_line_id = d.pop("order_line_id", UNSET)

        or31_response_200_order_update_result_order_lines = cls(
            order_line_additional_fields=order_line_additional_fields,
            order_line_id=order_line_id,
        )

        or31_response_200_order_update_result_order_lines.additional_properties = d
        return or31_response_200_order_update_result_order_lines

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
