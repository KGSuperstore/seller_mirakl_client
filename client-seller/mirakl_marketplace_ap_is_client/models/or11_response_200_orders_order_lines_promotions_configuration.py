from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersOrderLinesPromotionsConfiguration")


@_attrs_define
class OR11Response200OrdersOrderLinesPromotionsConfiguration:
    """
    Attributes:
        amount_off (Union[Unset, float]): The amount off of the promotion. <br/>Only applicable when promotion is of
            type <code>AMOUNT_OFF</code>, null otherwise.
        free_items_quantity (Union[Unset, int]): The free item target quantity of the promotion. <br/>Only applicable
            when promotion is of type <code>FREE_ITEMS</code>, null otherwise.
        internal_description (Union[Unset, str]): Promotion's Internal description, set by the shop at creation
        percentage_off (Union[Unset, float]): The percentage off of the promotion. <br/>Only applicable when promotion
            is of type <code>PERCENTAGE_OFF</code>, null otherwise.
        reduced_unit_price (Union[Unset, float]): The new offer’s unit price triggered by the promotion. <br/>Only
            applicable when promotion is of type <code>REDUCED_UNIT_PRICE</code>, null otherwise.
        type_ (Union[Unset, str]): Promotion's type, whether it is applied to this item (<code>ITEM</code>), or every
            items in the basket for this shop (<code>BASKET</code>)
    """

    amount_off: Union[Unset, float] = UNSET
    free_items_quantity: Union[Unset, int] = UNSET
    internal_description: Union[Unset, str] = UNSET
    percentage_off: Union[Unset, float] = UNSET
    reduced_unit_price: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_off = self.amount_off

        free_items_quantity = self.free_items_quantity

        internal_description = self.internal_description

        percentage_off = self.percentage_off

        reduced_unit_price = self.reduced_unit_price

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_off is not UNSET:
            field_dict["amount_off"] = amount_off
        if free_items_quantity is not UNSET:
            field_dict["free_items_quantity"] = free_items_quantity
        if internal_description is not UNSET:
            field_dict["internal_description"] = internal_description
        if percentage_off is not UNSET:
            field_dict["percentage_off"] = percentage_off
        if reduced_unit_price is not UNSET:
            field_dict["reduced_unit_price"] = reduced_unit_price
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_off = d.pop("amount_off", UNSET)

        free_items_quantity = d.pop("free_items_quantity", UNSET)

        internal_description = d.pop("internal_description", UNSET)

        percentage_off = d.pop("percentage_off", UNSET)

        reduced_unit_price = d.pop("reduced_unit_price", UNSET)

        type_ = d.pop("type", UNSET)

        or11_response_200_orders_order_lines_promotions_configuration = cls(
            amount_off=amount_off,
            free_items_quantity=free_items_quantity,
            internal_description=internal_description,
            percentage_off=percentage_off,
            reduced_unit_price=reduced_unit_price,
            type_=type_,
        )

        or11_response_200_orders_order_lines_promotions_configuration.additional_properties = d
        return or11_response_200_orders_order_lines_promotions_configuration

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
