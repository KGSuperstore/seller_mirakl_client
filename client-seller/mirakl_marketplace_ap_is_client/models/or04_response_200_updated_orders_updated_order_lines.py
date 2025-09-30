from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_response_200_updated_orders_updated_order_lines_cancelations import (
        OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations,
    )
    from ..models.or04_response_200_updated_orders_updated_order_lines_eco_contributions import (
        OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions,
    )
    from ..models.or04_response_200_updated_orders_updated_order_lines_refunds import (
        OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds,
    )


T = TypeVar("T", bound="OR04Response200UpdatedOrdersUpdatedOrderLines")


@_attrs_define
class OR04Response200UpdatedOrdersUpdatedOrderLines:
    """
    Attributes:
        cancelations (Union[Unset, list['OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations']]): List of the
            cancelations
        eco_contributions (Union[Unset, list['OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions']]): List of
            eco-contribution amounts and corresponding producer identifiers, if applicable
        order_line_id (Union[Unset, str]): Order line's identifier
        refunds (Union[Unset, list['OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds']]): List of the refunds
    """

    cancelations: Union[Unset, list["OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations"]] = UNSET
    eco_contributions: Union[Unset, list["OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    refunds: Union[Unset, list["OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cancelations, Unset):
            cancelations = []
            for cancelations_item_data in self.cancelations:
                cancelations_item = cancelations_item_data.to_dict()
                cancelations.append(cancelations_item)

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        order_line_id = self.order_line_id

        refunds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = []
            for refunds_item_data in self.refunds:
                refunds_item = refunds_item_data.to_dict()
                refunds.append(refunds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancelations is not UNSET:
            field_dict["cancelations"] = cancelations
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if refunds is not UNSET:
            field_dict["refunds"] = refunds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_response_200_updated_orders_updated_order_lines_cancelations import (
            OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations,
        )
        from ..models.or04_response_200_updated_orders_updated_order_lines_eco_contributions import (
            OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions,
        )
        from ..models.or04_response_200_updated_orders_updated_order_lines_refunds import (
            OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds,
        )

        d = dict(src_dict)
        cancelations = []
        _cancelations = d.pop("cancelations", UNSET)
        for cancelations_item_data in _cancelations or []:
            cancelations_item = OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations.from_dict(
                cancelations_item_data
            )

            cancelations.append(cancelations_item)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions.from_dict(
                eco_contributions_item_data
            )

            eco_contributions.append(eco_contributions_item)

        order_line_id = d.pop("order_line_id", UNSET)

        refunds = []
        _refunds = d.pop("refunds", UNSET)
        for refunds_item_data in _refunds or []:
            refunds_item = OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        or04_response_200_updated_orders_updated_order_lines = cls(
            cancelations=cancelations,
            eco_contributions=eco_contributions,
            order_line_id=order_line_id,
            refunds=refunds,
        )

        or04_response_200_updated_orders_updated_order_lines.additional_properties = d
        return or04_response_200_updated_orders_updated_order_lines

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
