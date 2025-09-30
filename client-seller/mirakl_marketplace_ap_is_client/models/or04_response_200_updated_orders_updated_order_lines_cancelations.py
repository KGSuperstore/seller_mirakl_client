from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_response_200_updated_orders_updated_order_lines_cancelations_eco_contributions import (
        OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions,
    )


T = TypeVar("T", bound="OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations")


@_attrs_define
class OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations:
    """
    Attributes:
        cancelation_id (Union[Unset, str]): Cancelation identifier
        eco_contributions (Union[Unset,
            list['OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions']]): List of eco-contribution
            amounts and corresponding producer identifiers, if applicable
    """

    cancelation_id: Union[Unset, str] = UNSET
    eco_contributions: Union[
        Unset, list["OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelation_id = self.cancelation_id

        eco_contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eco_contributions, Unset):
            eco_contributions = []
            for eco_contributions_item_data in self.eco_contributions:
                eco_contributions_item = eco_contributions_item_data.to_dict()
                eco_contributions.append(eco_contributions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancelation_id is not UNSET:
            field_dict["cancelation_id"] = cancelation_id
        if eco_contributions is not UNSET:
            field_dict["eco_contributions"] = eco_contributions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_response_200_updated_orders_updated_order_lines_cancelations_eco_contributions import (
            OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions,
        )

        d = dict(src_dict)
        cancelation_id = d.pop("cancelation_id", UNSET)

        eco_contributions = []
        _eco_contributions = d.pop("eco_contributions", UNSET)
        for eco_contributions_item_data in _eco_contributions or []:
            eco_contributions_item = (
                OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions.from_dict(
                    eco_contributions_item_data
                )
            )

            eco_contributions.append(eco_contributions_item)

        or04_response_200_updated_orders_updated_order_lines_cancelations = cls(
            cancelation_id=cancelation_id,
            eco_contributions=eco_contributions,
        )

        or04_response_200_updated_orders_updated_order_lines_cancelations.additional_properties = d
        return or04_response_200_updated_orders_updated_order_lines_cancelations

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
