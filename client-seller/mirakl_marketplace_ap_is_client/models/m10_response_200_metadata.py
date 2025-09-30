import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.m10_response_200_metadata_last_sender import M10Response200MetadataLastSender


T = TypeVar("T", bound="M10Response200Metadata")


@_attrs_define
class M10Response200Metadata:
    """
    Attributes:
        last_message_date (Union[Unset, datetime.datetime]): Date of the last message
        last_sender (Union[Unset, M10Response200MetadataLastSender]):
        shop_reply_needed_since (Union[Unset, datetime.datetime]): Date since a shop response is needed in the thread
        total_count (Union[Unset, int]): Number of messages in the thread
    """

    last_message_date: Union[Unset, datetime.datetime] = UNSET
    last_sender: Union[Unset, "M10Response200MetadataLastSender"] = UNSET
    shop_reply_needed_since: Union[Unset, datetime.datetime] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_message_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_message_date, Unset):
            last_message_date = self.last_message_date.isoformat()

        last_sender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_sender, Unset):
            last_sender = self.last_sender.to_dict()

        shop_reply_needed_since: Union[Unset, str] = UNSET
        if not isinstance(self.shop_reply_needed_since, Unset):
            shop_reply_needed_since = self.shop_reply_needed_since.isoformat()

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_message_date is not UNSET:
            field_dict["last_message_date"] = last_message_date
        if last_sender is not UNSET:
            field_dict["last_sender"] = last_sender
        if shop_reply_needed_since is not UNSET:
            field_dict["shop_reply_needed_since"] = shop_reply_needed_since
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.m10_response_200_metadata_last_sender import M10Response200MetadataLastSender

        d = dict(src_dict)
        _last_message_date = d.pop("last_message_date", UNSET)
        last_message_date: Union[Unset, datetime.datetime]
        if isinstance(_last_message_date, Unset):
            last_message_date = UNSET
        else:
            last_message_date = isoparse(_last_message_date)

        _last_sender = d.pop("last_sender", UNSET)
        last_sender: Union[Unset, M10Response200MetadataLastSender]
        if isinstance(_last_sender, Unset):
            last_sender = UNSET
        else:
            last_sender = M10Response200MetadataLastSender.from_dict(_last_sender)

        _shop_reply_needed_since = d.pop("shop_reply_needed_since", UNSET)
        shop_reply_needed_since: Union[Unset, datetime.datetime]
        if isinstance(_shop_reply_needed_since, Unset):
            shop_reply_needed_since = UNSET
        else:
            shop_reply_needed_since = isoparse(_shop_reply_needed_since)

        total_count = d.pop("total_count", UNSET)

        m10_response_200_metadata = cls(
            last_message_date=last_message_date,
            last_sender=last_sender,
            shop_reply_needed_since=shop_reply_needed_since,
            total_count=total_count,
        )

        m10_response_200_metadata.additional_properties = d
        return m10_response_200_metadata

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
