from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_response_200_updated_orders_updated_order_lines_refunds_eco_contributions import (
        OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions,
    )


T = TypeVar("T", bound="OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds")


@_attrs_define
class OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds:
    """
    Attributes:
        eco_contributions (Union[Unset, list['OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions']]):
            List of eco-contribution amounts and corresponding producer identifiers, if applicable
        refund_id (Union[Unset, str]): Refund identifier
    """

    eco_contributions: Union[Unset, list["OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions"]] = (
        UNSET
    )
    refund_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        refund_id = self.refund_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions
        if refund_id is not UNSET:
            field_dict["refund_id"] = refund_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_response_200_updated_orders_updated_order_lines_refunds_eco_contributions import (
            OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions,
        )

        d = dict(src_dict)
        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions.from_dict(
                eco_contributions_item_data
            )

            eco_contributions.append(eco_contributions_item)

        refund_id = d.pop("refund_id", UNSET)

        or04_response_200_updated_orders_updated_order_lines_refunds = cls(
            eco_contributions=eco_contributions,
            refund_id=refund_id,
        )

        or04_response_200_updated_orders_updated_order_lines_refunds.additional_properties = d
        return or04_response_200_updated_orders_updated_order_lines_refunds

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
