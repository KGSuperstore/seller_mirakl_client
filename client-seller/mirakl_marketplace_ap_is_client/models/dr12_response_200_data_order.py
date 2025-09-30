import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dr12_response_200_data_order_transaction_info import DR12Response200DataOrderTransactionInfo


T = TypeVar("T", bound="DR12Response200DataOrder")


@_attrs_define
class DR12Response200DataOrder:
    """
    Attributes:
        commercial_id (Union[Unset, str]): Order commercial identifier
        date_created (Union[Unset, datetime.datetime]): Order date created
        id (Union[Unset, str]): Order identifier
        reference_for_customer (Union[Unset, str]): Order reference for customer
        reference_for_seller (Union[Unset, str]): Order reference for seller
        transaction_info (Union[Unset, DR12Response200DataOrderTransactionInfo]):
    """

    commercial_id: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    reference_for_customer: Union[Unset, str] = UNSET
    reference_for_seller: Union[Unset, str] = UNSET
    transaction_info: Union[Unset, "DR12Response200DataOrderTransactionInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commercial_id = self.commercial_id

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        id = self.id

        reference_for_customer = self.reference_for_customer

        reference_for_seller = self.reference_for_seller

        transaction_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transaction_info, Unset):
            transaction_info = self.transaction_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commercial_id is not UNSET:
            field_dict["commercial_id"] = commercial_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if id is not UNSET:
            field_dict["id"] = id
        if reference_for_customer is not UNSET:
            field_dict["reference_for_customer"] = reference_for_customer
        if reference_for_seller is not UNSET:
            field_dict["reference_for_seller"] = reference_for_seller
        if transaction_info is not UNSET:
            field_dict["transaction_info"] = transaction_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dr12_response_200_data_order_transaction_info import DR12Response200DataOrderTransactionInfo

        d = dict(src_dict)
        commercial_id = d.pop("commercial_id", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        id = d.pop("id", UNSET)

        reference_for_customer = d.pop("reference_for_customer", UNSET)

        reference_for_seller = d.pop("reference_for_seller", UNSET)

        _transaction_info = d.pop("transaction_info", UNSET)
        transaction_info: Union[Unset, DR12Response200DataOrderTransactionInfo]
        if isinstance(_transaction_info, Unset):
            transaction_info = UNSET
        else:
            transaction_info = DR12Response200DataOrderTransactionInfo.from_dict(_transaction_info)

        dr12_response_200_data_order = cls(
            commercial_id=commercial_id,
            date_created=date_created,
            id=id,
            reference_for_customer=reference_for_customer,
            reference_for_seller=reference_for_seller,
            transaction_info=transaction_info,
        )

        dr12_response_200_data_order.additional_properties = d
        return dr12_response_200_data_order

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
