import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.m11_response_200_data_messages_attachments import M11Response200DataMessagesAttachments
    from ..models.m11_response_200_data_messages_from import M11Response200DataMessagesFrom
    from ..models.m11_response_200_data_messages_to import M11Response200DataMessagesTo


T = TypeVar("T", bound="M11Response200DataMessages")


@_attrs_define
class M11Response200DataMessages:
    """
    Attributes:
        attachments (Union[Unset, list['M11Response200DataMessagesAttachments']]): Message attachments
        body (Union[Unset, str]): Message body
        date_created (Union[Unset, datetime.datetime]): Message creation date
        from_ (Union[Unset, M11Response200DataMessagesFrom]):
        id (Union[Unset, str]): Message id
        to (Union[Unset, list['M11Response200DataMessagesTo']]): Message recipients
    """

    attachments: Union[Unset, list["M11Response200DataMessagesAttachments"]] = UNSET
    body: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    from_: Union[Unset, "M11Response200DataMessagesFrom"] = UNSET
    id: Union[Unset, str] = UNSET
    to: Union[Unset, list["M11Response200DataMessagesTo"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        body = self.body

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        id = self.id

        to: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.to, Unset):
            to = []
            for to_item_data in self.to:
                to_item = to_item_data.to_dict()
                to.append(to_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if body is not UNSET:
            field_dict["body"] = body
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.m11_response_200_data_messages_attachments import M11Response200DataMessagesAttachments
        from ..models.m11_response_200_data_messages_from import M11Response200DataMessagesFrom
        from ..models.m11_response_200_data_messages_to import M11Response200DataMessagesTo

        d = dict(src_dict)
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = M11Response200DataMessagesAttachments.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        body = d.pop("body", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, M11Response200DataMessagesFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = M11Response200DataMessagesFrom.from_dict(_from_)

        id = d.pop("id", UNSET)

        to = []
        _to = d.pop("to", UNSET)
        for to_item_data in _to or []:
            to_item = M11Response200DataMessagesTo.from_dict(to_item_data)

            to.append(to_item)

        m11_response_200_data_messages = cls(
            attachments=attachments,
            body=body,
            date_created=date_created,
            from_=from_,
            id=id,
            to=to,
        )

        m11_response_200_data_messages.additional_properties = d
        return m11_response_200_data_messages

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
