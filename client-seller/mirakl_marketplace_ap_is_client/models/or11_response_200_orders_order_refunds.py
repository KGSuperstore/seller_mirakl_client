from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_order_refunds_taxes import OR11Response200OrdersOrderRefundsTaxes


T = TypeVar("T", bound="OR11Response200OrdersOrderRefunds")


@_attrs_define
class OR11Response200OrdersOrderRefunds:
    """
    Attributes:
        order_refund_id (Union[Unset, str]): The group identifier of the refunds created at the same time on the order
        taxes (Union[Unset, list['OR11Response200OrdersOrderRefundsTaxes']]): Total amount of refunded taxes aggregated
            per tax code and rate
    """

    order_refund_id: Union[Unset, str] = UNSET
    taxes: Union[Unset, list["OR11Response200OrdersOrderRefundsTaxes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_refund_id = self.order_refund_id

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_refund_id is not UNSET:
            field_dict["order_refund_id"] = order_refund_id
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_order_refunds_taxes import OR11Response200OrdersOrderRefundsTaxes

        d = dict(src_dict)
        order_refund_id = d.pop("order_refund_id", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = OR11Response200OrdersOrderRefundsTaxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        or11_response_200_orders_order_refunds = cls(
            order_refund_id=order_refund_id,
            taxes=taxes,
        )

        or11_response_200_orders_order_refunds.additional_properties = d
        return or11_response_200_orders_order_refunds

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
