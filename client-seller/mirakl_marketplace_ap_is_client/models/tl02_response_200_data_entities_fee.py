from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tl02_response_200_data_entities_fee_cancelations import TL02Response200DataEntitiesFeeCancelations
    from ..models.tl02_response_200_data_entities_fee_refunds import TL02Response200DataEntitiesFeeRefunds


T = TypeVar("T", bound="TL02Response200DataEntitiesFee")


@_attrs_define
class TL02Response200DataEntitiesFee:
    """
    Attributes:
        cancelations (Union[Unset, list['TL02Response200DataEntitiesFeeCancelations']]): The list of cancelations
            information if any
        code (Union[Unset, str]): The code of the seller additional fee
        refunds (Union[Unset, list['TL02Response200DataEntitiesFeeRefunds']]): The list of refunds information if any
    """

    cancelations: Union[Unset, list["TL02Response200DataEntitiesFeeCancelations"]] = UNSET
    code: Union[Unset, str] = UNSET
    refunds: Union[Unset, list["TL02Response200DataEntitiesFeeRefunds"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cancelations, Unset):
            cancelations = []
            for cancelations_item_data in self.cancelations:
                cancelations_item = cancelations_item_data.to_dict()
                cancelations.append(cancelations_item)

        code = self.code

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
        if code is not UNSET:
            field_dict["code"] = code
        if refunds is not UNSET:
            field_dict["refunds"] = refunds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tl02_response_200_data_entities_fee_cancelations import TL02Response200DataEntitiesFeeCancelations
        from ..models.tl02_response_200_data_entities_fee_refunds import TL02Response200DataEntitiesFeeRefunds

        d = dict(src_dict)
        cancelations = []
        _cancelations = d.pop("cancelations", UNSET)
        for cancelations_item_data in _cancelations or []:
            cancelations_item = TL02Response200DataEntitiesFeeCancelations.from_dict(cancelations_item_data)

            cancelations.append(cancelations_item)

        code = d.pop("code", UNSET)

        refunds = []
        _refunds = d.pop("refunds", UNSET)
        for refunds_item_data in _refunds or []:
            refunds_item = TL02Response200DataEntitiesFeeRefunds.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        tl02_response_200_data_entities_fee = cls(
            cancelations=cancelations,
            code=code,
            refunds=refunds,
        )

        tl02_response_200_data_entities_fee.additional_properties = d
        return tl02_response_200_data_entities_fee

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
