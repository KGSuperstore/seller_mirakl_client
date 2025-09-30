import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF21Response200OffersAllPricesContext")


@_attrs_define
class OF21Response200OffersAllPricesContext:
    """
    Attributes:
        channel_codes (Union[Unset, list[str]]): The channel codes on which a specific price applies.
        customer_group_ids (Union[Unset, list[str]]): The customer group ids on which a specific price applies.
        customer_organization_ids (Union[Unset, list[str]]): The customer organization ids on which a specific price
            applies.
        end_date (Union[Unset, datetime.datetime]): The end date of a specific price.
        start_date (Union[Unset, datetime.datetime]): The start date of a specific price.
    """

    channel_codes: Union[Unset, list[str]] = UNSET
    customer_group_ids: Union[Unset, list[str]] = UNSET
    customer_organization_ids: Union[Unset, list[str]] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_codes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channel_codes, Unset):
            channel_codes = self.channel_codes

        customer_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.customer_group_ids, Unset):
            customer_group_ids = self.customer_group_ids

        customer_organization_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.customer_organization_ids, Unset):
            customer_organization_ids = self.customer_organization_ids

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_codes is not UNSET:
            field_dict["channel_codes"] = channel_codes
        if customer_group_ids is not UNSET:
            field_dict["customer_group_ids"] = customer_group_ids
        if customer_organization_ids is not UNSET:
            field_dict["customer_organization_ids"] = customer_organization_ids
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_codes = cast(list[str], d.pop("channel_codes", UNSET))

        customer_group_ids = cast(list[str], d.pop("customer_group_ids", UNSET))

        customer_organization_ids = cast(list[str], d.pop("customer_organization_ids", UNSET))

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        of21_response_200_offers_all_prices_context = cls(
            channel_codes=channel_codes,
            customer_group_ids=customer_group_ids,
            customer_organization_ids=customer_organization_ids,
            end_date=end_date,
            start_date=start_date,
        )

        of21_response_200_offers_all_prices_context.additional_properties = d
        return of21_response_200_offers_all_prices_context

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
