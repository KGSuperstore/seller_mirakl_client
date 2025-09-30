from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or32_response_200_order_lines_adjusted import OR32Response200OrderLinesAdjusted


T = TypeVar("T", bound="OR32Response200")


@_attrs_define
class OR32Response200:
    """
    Attributes:
        order_lines_adjusted (Union[Unset, list['OR32Response200OrderLinesAdjusted']]): A list of updated order lines
            and orders in error objects
    """

    order_lines_adjusted: Union[Unset, list["OR32Response200OrderLinesAdjusted"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_lines_adjusted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines_adjusted, Unset):
            order_lines_adjusted = []
            for order_lines_adjusted_item_data in self.order_lines_adjusted:
                order_lines_adjusted_item = order_lines_adjusted_item_data.to_dict()
                order_lines_adjusted.append(order_lines_adjusted_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_lines_adjusted is not UNSET:
            field_dict["order_lines_adjusted"] = order_lines_adjusted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or32_response_200_order_lines_adjusted import OR32Response200OrderLinesAdjusted

        d = dict(src_dict)
        order_lines_adjusted = []
        _order_lines_adjusted = d.pop("order_lines_adjusted", UNSET)
        for order_lines_adjusted_item_data in _order_lines_adjusted or []:
            order_lines_adjusted_item = OR32Response200OrderLinesAdjusted.from_dict(order_lines_adjusted_item_data)

            order_lines_adjusted.append(order_lines_adjusted_item)

        or32_response_200 = cls(
            order_lines_adjusted=order_lines_adjusted,
        )

        or32_response_200.additional_properties = d
        return or32_response_200

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
