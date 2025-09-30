from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PR01Response200PromotionsTriggers")


@_attrs_define
class PR01Response200PromotionsTriggers:
    """
    Attributes:
        amount_purchased (Union[Unset, float]): Amount that triggers the promotion. Available for
            <code>minimum_amount</code> or <code>every_amount</code> type triggers.
        quantity_purchased (Union[Unset, int]): Quantity of items that triggers the promotion. Available for
            <code>minimum_quantity</code> or <code>every_quantity</code> type triggers.
        same_item_purchased (Union[Unset, bool]): Whether the promotion requires the same item to be triggered or not.
            Available for <code>minimum_quantity</code> or <code>every_quantity</code> type triggers.
        type_ (Union[Unset, str]): Type of promotion trigger
    """

    amount_purchased: Union[Unset, float] = UNSET
    quantity_purchased: Union[Unset, int] = UNSET
    same_item_purchased: Union[Unset, bool] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_purchased = self.amount_purchased

        quantity_purchased = self.quantity_purchased

        same_item_purchased = self.same_item_purchased

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_purchased is not UNSET:
            field_dict["amount_purchased"] = amount_purchased
        if quantity_purchased is not UNSET:
            field_dict["quantity_purchased"] = quantity_purchased
        if same_item_purchased is not UNSET:
            field_dict["same_item_purchased"] = same_item_purchased
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_purchased = d.pop("amount_purchased", UNSET)

        quantity_purchased = d.pop("quantity_purchased", UNSET)

        same_item_purchased = d.pop("same_item_purchased", UNSET)

        type_ = d.pop("type", UNSET)

        pr01_response_200_promotions_triggers = cls(
            amount_purchased=amount_purchased,
            quantity_purchased=quantity_purchased,
            same_item_purchased=same_item_purchased,
            type_=type_,
        )

        pr01_response_200_promotions_triggers.additional_properties = d
        return pr01_response_200_promotions_triggers

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
