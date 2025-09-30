from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or30_response_200_cancelations import OR30Response200Cancelations


T = TypeVar("T", bound="OR30Response200")


@_attrs_define
class OR30Response200:
    """
    Attributes:
        cancelations (Union[Unset, list['OR30Response200Cancelations']]): List of representations of created
            cancellations
        order_tax_mode (Union[Unset, str]): Please note: In case there is no tax, the prices will show the same amount
            in TAX_EXCLUDED and TAX_INCLUDED mode. The tax mode is only useful if taxes are specified in the
            cancelation.<br>Possible values: <ul><li><code>TAX_EXCLUDED</code>: the price fields (amount, shipping amount)
            are expressed without tax (taxes should be added to these prices in order to get the full amount including
            taxes).</li><li><code>TAX_INCLUDED</code>: the price fields include the tax amount. </li></ul>
    """

    cancelations: Union[Unset, list["OR30Response200Cancelations"]] = UNSET
    order_tax_mode: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cancelations, Unset):
            cancelations = []
            for cancelations_item_data in self.cancelations:
                cancelations_item = cancelations_item_data.to_dict()
                cancelations.append(cancelations_item)

        order_tax_mode = self.order_tax_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancelations is not UNSET:
            field_dict["cancelations"] = cancelations
        if order_tax_mode is not UNSET:
            field_dict["order_tax_mode"] = order_tax_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or30_response_200_cancelations import OR30Response200Cancelations

        d = dict(src_dict)
        cancelations = []
        _cancelations = d.pop("cancelations", UNSET)
        for cancelations_item_data in _cancelations or []:
            cancelations_item = OR30Response200Cancelations.from_dict(cancelations_item_data)

            cancelations.append(cancelations_item)

        order_tax_mode = d.pop("order_tax_mode", UNSET)

        or30_response_200 = cls(
            cancelations=cancelations,
            order_tax_mode=order_tax_mode,
        )

        or30_response_200.additional_properties = d
        return or30_response_200

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
