from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or28_response_200_refunds import OR28Response200Refunds


T = TypeVar("T", bound="OR28Response200")


@_attrs_define
class OR28Response200:
    """
    Attributes:
        order_tax_mode (Union[Unset, str]): Please note: In case there is no tax, the prices will show the same amount
            in TAX_EXCLUDED and TAX_INCLUDED mode. The tax mode is only useful if taxes are specified in the
            refund.<br>Possible values: <ul><li><code>TAX_EXCLUDED</code>: the price fields (amount, shipping amount) are
            expressed without tax (taxes should be added to these prices in order to get the full amount including
            taxes).</li><li><code>TAX_INCLUDED</code>: the price fields include the tax amount. </li></ul>
        refunds (Union[Unset, list['OR28Response200Refunds']]): List of representations of created refunds
    """

    order_tax_mode: Union[Unset, str] = UNSET
    refunds: Union[Unset, list["OR28Response200Refunds"]] = UNSET
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
        from ..models.or28_response_200_refunds import OR28Response200Refunds

        d = dict(src_dict)
        order_tax_mode = d.pop("order_tax_mode", UNSET)

        refunds = []
        _refunds = d.pop("refunds", UNSET)
        for refunds_item_data in _refunds or []:
            refunds_item = OR28Response200Refunds.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        or28_response_200 = cls(
            order_tax_mode=order_tax_mode,
            refunds=refunds,
        )

        or28_response_200.additional_properties = d
        return or28_response_200

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
