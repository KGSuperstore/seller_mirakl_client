import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tl02_response_200_data_entities_order_payment_info import TL02Response200DataEntitiesOrderPaymentInfo
    from ..models.tl02_response_200_data_entities_order_references import TL02Response200DataEntitiesOrderReferences


T = TypeVar("T", bound="TL02Response200DataEntitiesOrder")


@_attrs_define
class TL02Response200DataEntitiesOrder:
    """
    Attributes:
        commercial_id (Union[Unset, str]): The order commercial id
        creation_date (Union[Unset, datetime.datetime]): The order creation date
        id (Union[Unset, str]): The order id
        payment_info (Union[Unset, TL02Response200DataEntitiesOrderPaymentInfo]):
        references (Union[Unset, TL02Response200DataEntitiesOrderReferences]):
    """

    commercial_id: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    payment_info: Union[Unset, "TL02Response200DataEntitiesOrderPaymentInfo"] = UNSET
    references: Union[Unset, "TL02Response200DataEntitiesOrderReferences"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commercial_id = self.commercial_id

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        id = self.id

        payment_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_info, Unset):
            payment_info = self.payment_info.to_dict()

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commercial_id is not UNSET:
            field_dict["commercial_id"] = commercial_id
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if id is not UNSET:
            field_dict["id"] = id
        if payment_info is not UNSET:
            field_dict["payment_info"] = payment_info
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tl02_response_200_data_entities_order_payment_info import (
            TL02Response200DataEntitiesOrderPaymentInfo,
        )
        from ..models.tl02_response_200_data_entities_order_references import TL02Response200DataEntitiesOrderReferences

        d = dict(src_dict)
        commercial_id = d.pop("commercial_id", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        id = d.pop("id", UNSET)

        _payment_info = d.pop("payment_info", UNSET)
        payment_info: Union[Unset, TL02Response200DataEntitiesOrderPaymentInfo]
        if isinstance(_payment_info, Unset):
            payment_info = UNSET
        else:
            payment_info = TL02Response200DataEntitiesOrderPaymentInfo.from_dict(_payment_info)

        _references = d.pop("references", UNSET)
        references: Union[Unset, TL02Response200DataEntitiesOrderReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = TL02Response200DataEntitiesOrderReferences.from_dict(_references)

        tl02_response_200_data_entities_order = cls(
            commercial_id=commercial_id,
            creation_date=creation_date,
            id=id,
            payment_info=payment_info,
            references=references,
        )

        tl02_response_200_data_entities_order.additional_properties = d
        return tl02_response_200_data_entities_order

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
