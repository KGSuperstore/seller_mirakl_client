from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_promotions_applied_promotions import (
        OR11Response200OrdersPromotionsAppliedPromotions,
    )


T = TypeVar("T", bound="OR11Response200OrdersPromotions")


@_attrs_define
class OR11Response200OrdersPromotions:
    """
    Attributes:
        applied_promotions (Union[Unset, list['OR11Response200OrdersPromotionsAppliedPromotions']]): The promotions
            applied on this order
        total_deduced_amount (Union[Unset, float]): The total amount deduced on this order thanks to the promotions
    """

    applied_promotions: Union[Unset, list["OR11Response200OrdersPromotionsAppliedPromotions"]] = UNSET
    total_deduced_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_promotions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.applied_promotions, Unset):
            applied_promotions = []
            for applied_promotions_item_data in self.applied_promotions:
                applied_promotions_item = applied_promotions_item_data.to_dict()
                applied_promotions.append(applied_promotions_item)

        total_deduced_amount = self.total_deduced_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_promotions is not UNSET:
            field_dict["applied_promotions"] = applied_promotions
        if total_deduced_amount is not UNSET:
            field_dict["total_deduced_amount"] = total_deduced_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_promotions_applied_promotions import (
            OR11Response200OrdersPromotionsAppliedPromotions,
        )

        d = dict(src_dict)
        applied_promotions = []
        _applied_promotions = d.pop("applied_promotions", UNSET)
        for applied_promotions_item_data in _applied_promotions or []:
            applied_promotions_item = OR11Response200OrdersPromotionsAppliedPromotions.from_dict(
                applied_promotions_item_data
            )

            applied_promotions.append(applied_promotions_item)

        total_deduced_amount = d.pop("total_deduced_amount", UNSET)

        or11_response_200_orders_promotions = cls(
            applied_promotions=applied_promotions,
            total_deduced_amount=total_deduced_amount,
        )

        or11_response_200_orders_promotions.additional_properties = d
        return or11_response_200_orders_promotions

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
