from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_request_orders_order_lines_eco_contributions import OR04RequestOrdersOrderLinesEcoContributions


T = TypeVar("T", bound="OR04RequestOrdersOrderLines")


@_attrs_define
class OR04RequestOrdersOrderLines:
    """Order lines to be updated

    Attributes:
        eco_contributions (Union[Unset, list['OR04RequestOrdersOrderLinesEcoContributions']]): Eco-contributions to add
            or update on the order line - only available if the operator setting Activate data collection related to
            circular economy regulations has been enabled.
        order_line_id (Union[Unset, str]): Order line's identifier
    """

    eco_contributions: Union[Unset, list["OR04RequestOrdersOrderLinesEcoContributions"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        order_line_id = self.order_line_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_request_orders_order_lines_eco_contributions import (
            OR04RequestOrdersOrderLinesEcoContributions,
        )

        d = dict(src_dict)
        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR04RequestOrdersOrderLinesEcoContributions.from_dict(eco_contributions_item_data)

            eco_contributions.append(eco_contributions_item)

        order_line_id = d.pop("order_line_id", UNSET)

        or04_request_orders_order_lines = cls(
            eco_contributions=eco_contributions,
            order_line_id=order_line_id,
        )

        or04_request_orders_order_lines.additional_properties = d
        return or04_request_orders_order_lines

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
