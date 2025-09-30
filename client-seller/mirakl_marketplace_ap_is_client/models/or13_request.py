import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR13Request")


@_attrs_define
class OR13Request:
    """
    Attributes:
        channel_codes (Union[Unset, list[str]]): A list of channel codes
        end_date (Union[Unset, datetime.datetime]): End order creation date for filtering. Must be used with
            <code>start_date</code>.
        end_update_date (Union[Unset, datetime.datetime]): End order update date for filtering. Must be used with
            <code>start_update_date</code>.
        fulfillment_center_codes (Union[Unset, str]): Code of the fulfillment center
        items_per_chunk (Union[Unset, int]): Maximum number of items included in the generated files Default: 1000000.
        megabytes_per_chunk (Union[Unset, int]): Maximum mega bytes weight for generated files Default: 512.
        only_null_channel (Union[Unset, bool]): Return only orders without channel. If <code>true</code>, ignore the
            <code>channel_codes</code> Default: False.
        order_state_codes (Union[Unset, list[str]]): A list of order state's codes
        order_tax_mode (Union[Unset, str]): Please note: If the taxes are not specified, the prices with mode
            TAX_EXCLUDED and with mode TAX_INCLUDED will return the same amounts.<br>Possible
            values:<ul><li><code>TAX_EXCLUDED</code>: the price fields (price, unit price, shipping price, cancellation
            amount, refund amount and order total prices) do not include taxes.</li><li><code>TAX_INCLUDED</code>: the price
            fields include the tax amount. </li></ul><li>If this query parameter is not specified, the default order tax
            mode of the platform is used.</li>
        start_date (Union[Unset, datetime.datetime]): Start order creation date for filtering. Must be used with
            <code>end_date</code>.
        start_update_date (Union[Unset, datetime.datetime]): Start order update date for filtering. Mirakl will subtract
            a time delta to ensure no orders are missed due to network and/or software latency. Must be used with
            <code>end_update_date</code>.
    """

    channel_codes: Union[Unset, list[str]] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    end_update_date: Union[Unset, datetime.datetime] = UNSET
    fulfillment_center_codes: Union[Unset, str] = UNSET
    items_per_chunk: Union[Unset, int] = 1000000
    megabytes_per_chunk: Union[Unset, int] = 512
    only_null_channel: Union[Unset, bool] = False
    order_state_codes: Union[Unset, list[str]] = UNSET
    order_tax_mode: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    start_update_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_codes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channel_codes, Unset):
            channel_codes = self.channel_codes

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        end_update_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_update_date, Unset):
            end_update_date = self.end_update_date.isoformat()

        fulfillment_center_codes = self.fulfillment_center_codes

        items_per_chunk = self.items_per_chunk

        megabytes_per_chunk = self.megabytes_per_chunk

        only_null_channel = self.only_null_channel

        order_state_codes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.order_state_codes, Unset):
            order_state_codes = self.order_state_codes

        order_tax_mode = self.order_tax_mode

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_update_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_update_date, Unset):
            start_update_date = self.start_update_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_codes is not UNSET:
            field_dict["channel_codes"] = channel_codes
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if end_update_date is not UNSET:
            field_dict["end_update_date"] = end_update_date
        if fulfillment_center_codes is not UNSET:
            field_dict["fulfillment_center_codes"] = fulfillment_center_codes
        if items_per_chunk is not UNSET:
            field_dict["items_per_chunk"] = items_per_chunk
        if megabytes_per_chunk is not UNSET:
            field_dict["megabytes_per_chunk"] = megabytes_per_chunk
        if only_null_channel is not UNSET:
            field_dict["only_null_channel"] = only_null_channel
        if order_state_codes is not UNSET:
            field_dict["order_state_codes"] = order_state_codes
        if order_tax_mode is not UNSET:
            field_dict["order_tax_mode"] = order_tax_mode
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_update_date is not UNSET:
            field_dict["start_update_date"] = start_update_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_codes = cast(list[str], d.pop("channel_codes", UNSET))

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _end_update_date = d.pop("end_update_date", UNSET)
        end_update_date: Union[Unset, datetime.datetime]
        if isinstance(_end_update_date, Unset):
            end_update_date = UNSET
        else:
            end_update_date = isoparse(_end_update_date)

        fulfillment_center_codes = d.pop("fulfillment_center_codes", UNSET)

        items_per_chunk = d.pop("items_per_chunk", UNSET)

        megabytes_per_chunk = d.pop("megabytes_per_chunk", UNSET)

        only_null_channel = d.pop("only_null_channel", UNSET)

        order_state_codes = cast(list[str], d.pop("order_state_codes", UNSET))

        order_tax_mode = d.pop("order_tax_mode", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _start_update_date = d.pop("start_update_date", UNSET)
        start_update_date: Union[Unset, datetime.datetime]
        if isinstance(_start_update_date, Unset):
            start_update_date = UNSET
        else:
            start_update_date = isoparse(_start_update_date)

        or13_request = cls(
            channel_codes=channel_codes,
            end_date=end_date,
            end_update_date=end_update_date,
            fulfillment_center_codes=fulfillment_center_codes,
            items_per_chunk=items_per_chunk,
            megabytes_per_chunk=megabytes_per_chunk,
            only_null_channel=only_null_channel,
            order_state_codes=order_state_codes,
            order_tax_mode=order_tax_mode,
            start_date=start_date,
            start_update_date=start_update_date,
        )

        or13_request.additional_properties = d
        return or13_request

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
