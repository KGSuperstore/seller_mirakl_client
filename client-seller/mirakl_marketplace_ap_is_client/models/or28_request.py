from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or28_request_refunds import OR28RequestRefunds


T = TypeVar("T", bound="OR28Request")


@_attrs_define
class OR28Request:
    """
    Attributes:
        order_tax_mode (Union[Unset, str]): Please note: If the taxes are not specified, the prices with mode
            TAX_EXCLUDED and with mode TAX_INCLUDED will return the same amounts.<br>Possible
            values:<ul><li><code>TAX_EXCLUDED</code>: the price fields (price, unit price, shipping price and order total
            prices) do not include taxes.</li><li><code>TAX_INCLUDED</code>: the price fields include the tax amounts.
            </li><li>If not specified, the default order tax mode of the platform is used.</li></ul>
        refunds (Union[Unset, list['OR28RequestRefunds']]): List of representations of refunds to be created
    """

    order_tax_mode: Union[Unset, str] = UNSET
    refunds: Union[Unset, list["OR28RequestRefunds"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_tax_mode = self.order_tax_mode

        refunds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = []
            for refunds_item_data in self.refunds:
                refunds_item = refunds_item_data.to_dict()
                refunds.append(refunds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_tax_mode is not UNSET:
            field_dict["order_tax_mode"] = order_tax_mode
        if refunds is not UNSET:
            field_dict["refunds"] = refunds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or28_request_refunds import OR28RequestRefunds

        d = dict(src_dict)
        order_tax_mode = d.pop("order_tax_mode", UNSET)

        refunds = []
        _refunds = d.pop("refunds", UNSET)
        for refunds_item_data in _refunds or []:
            refunds_item = OR28RequestRefunds.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        or28_request = cls(
            order_tax_mode=order_tax_mode,
            refunds=refunds,
        )

        or28_request.additional_properties = d
        return or28_request

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
