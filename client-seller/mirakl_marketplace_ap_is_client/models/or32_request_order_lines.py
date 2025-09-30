from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR32RequestOrderLines")


@_attrs_define
class OR32RequestOrderLines:
    """Order lines to be updated, maximum number of order lines per call: 100

    Attributes:
        actual_measurement (Union[Unset, float]): Order line's actual measurement
        order_line_id (Union[Unset, str]): Order Line identifier
    """

    actual_measurement: Union[Unset, float] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_measurement = self.actual_measurement

        order_line_id = self.order_line_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_measurement is not UNSET:
            field_dict["actual_measurement"] = actual_measurement
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actual_measurement = d.pop("actual_measurement", UNSET)

        order_line_id = d.pop("order_line_id", UNSET)

        or32_request_order_lines = cls(
            actual_measurement=actual_measurement,
            order_line_id=order_line_id,
        )

        or32_request_order_lines.additional_properties = d
        return or32_request_order_lines

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
