import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.m11_response_200_data_authorized_participants import M11Response200DataAuthorizedParticipants
    from ..models.m11_response_200_data_current_participants import M11Response200DataCurrentParticipants
    from ..models.m11_response_200_data_customer_organization import M11Response200DataCustomerOrganization
    from ..models.m11_response_200_data_entities import M11Response200DataEntities
    from ..models.m11_response_200_data_messages import M11Response200DataMessages
    from ..models.m11_response_200_data_metadata import M11Response200DataMetadata
    from ..models.m11_response_200_data_no_store_reply_needed import M11Response200DataNoStoreReplyNeeded
    from ..models.m11_response_200_data_topic import M11Response200DataTopic


T = TypeVar("T", bound="M11Response200Data")


@_attrs_define
class M11Response200Data:
    """
    Attributes:
        authorized_participants (Union[Unset, list['M11Response200DataAuthorizedParticipants']]): Thread authorized
            participants<br/>
            Those are the participants who are authorized to join the thread.
        current_participants (Union[Unset, list['M11Response200DataCurrentParticipants']]): Thread current
            participants<br/>
            Those are the participants who have actually participated in the thread, meaning that they are either sender or
            receivers of at least one message of the thread.<br/>
            These participants must be on the list of the <code>authorized_participants</code>
        customer_organization (Union[Unset, M11Response200DataCustomerOrganization]):
        date_created (Union[Unset, datetime.datetime]): Thread created date
        date_updated (Union[Unset, datetime.datetime]): Thread updated date
        entities (Union[Unset, list['M11Response200DataEntities']]): Thread entities
        id (Union[Unset, str]): Thread id
        messages (Union[Unset, list['M11Response200DataMessages']]): Thread messages. Limited to the last 100 messages
            of the thread. Present if with_messages query parameter has been set to true
        metadata (Union[Unset, M11Response200DataMetadata]):
        no_store_reply_needed (Union[Unset, list['M11Response200DataNoStoreReplyNeeded']]):     Thread "no store reply
            needed" actions. Present if "with_messages" query parameter has been set to true.
        topic (Union[Unset, M11Response200DataTopic]):
    """

    authorized_participants: Union[Unset, list["M11Response200DataAuthorizedParticipants"]] = UNSET
    current_participants: Union[Unset, list["M11Response200DataCurrentParticipants"]] = UNSET
    customer_organization: Union[Unset, "M11Response200DataCustomerOrganization"] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_updated: Union[Unset, datetime.datetime] = UNSET
    entities: Union[Unset, list["M11Response200DataEntities"]] = UNSET
    id: Union[Unset, str] = UNSET
    messages: Union[Unset, list["M11Response200DataMessages"]] = UNSET
    metadata: Union[Unset, "M11Response200DataMetadata"] = UNSET
    no_store_reply_needed: Union[Unset, list["M11Response200DataNoStoreReplyNeeded"]] = UNSET
    topic: Union[Unset, "M11Response200DataTopic"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorized_participants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.authorized_participants, Unset):
            authorized_participants = []
            for authorized_participants_item_data in self.authorized_participants:
                authorized_participants_item = authorized_participants_item_data.to_dict()
                authorized_participants.append(authorized_participants_item)

        current_participants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.current_participants, Unset):
            current_participants = []
            for current_participants_item_data in self.current_participants:
                current_participants_item = current_participants_item_data.to_dict()
                current_participants.append(current_participants_item)

        customer_organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer_organization, Unset):
            customer_organization = self.customer_organization.to_dict()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_updated: Union[Unset, str] = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        id = self.id

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        no_store_reply_needed: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.no_store_reply_needed, Unset):
            no_store_reply_needed = []
            for no_store_reply_needed_item_data in self.no_store_reply_needed:
                no_store_reply_needed_item = no_store_reply_needed_item_data.to_dict()
                no_store_reply_needed.append(no_store_reply_needed_item)

        topic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topic, Unset):
            topic = self.topic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorized_participants is not UNSET:
            field_dict["authorized_participants"] = authorized_participants
        if current_participants is not UNSET:
            field_dict["current_participants"] = current_participants
        if customer_organization is not UNSET:
            field_dict["customer_organization"] = customer_organization
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if entities is not UNSET:
            field_dict["entities"] = entities
        if id is not UNSET:
            field_dict["id"] = id
        if messages is not UNSET:
            field_dict["messages"] = messages
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if no_store_reply_needed is not UNSET:
            field_dict["no_store_reply_needed"] = no_store_reply_needed
        if topic is not UNSET:
            field_dict["topic"] = topic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.m11_response_200_data_authorized_participants import M11Response200DataAuthorizedParticipants
        from ..models.m11_response_200_data_current_participants import M11Response200DataCurrentParticipants
        from ..models.m11_response_200_data_customer_organization import M11Response200DataCustomerOrganization
        from ..models.m11_response_200_data_entities import M11Response200DataEntities
        from ..models.m11_response_200_data_messages import M11Response200DataMessages
        from ..models.m11_response_200_data_metadata import M11Response200DataMetadata
        from ..models.m11_response_200_data_no_store_reply_needed import M11Response200DataNoStoreReplyNeeded
        from ..models.m11_response_200_data_topic import M11Response200DataTopic

        d = dict(src_dict)
        authorized_participants = []
        _authorized_participants = d.pop("authorized_participants", UNSET)
        for authorized_participants_item_data in _authorized_participants or []:
            authorized_participants_item = M11Response200DataAuthorizedParticipants.from_dict(
                authorized_participants_item_data
            )

            authorized_participants.append(authorized_participants_item)

        current_participants = []
        _current_participants = d.pop("current_participants", UNSET)
        for current_participants_item_data in _current_participants or []:
            current_participants_item = M11Response200DataCurrentParticipants.from_dict(current_participants_item_data)

            current_participants.append(current_participants_item)

        _customer_organization = d.pop("customer_organization", UNSET)
        customer_organization: Union[Unset, M11Response200DataCustomerOrganization]
        if isinstance(_customer_organization, Unset):
            customer_organization = UNSET
        else:
            customer_organization = M11Response200DataCustomerOrganization.from_dict(_customer_organization)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_updated = d.pop("date_updated", UNSET)
        date_updated: Union[Unset, datetime.datetime]
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = isoparse(_date_updated)

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = M11Response200DataEntities.from_dict(entities_item_data)

            entities.append(entities_item)

        id = d.pop("id", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = M11Response200DataMessages.from_dict(messages_item_data)

            messages.append(messages_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, M11Response200DataMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = M11Response200DataMetadata.from_dict(_metadata)

        no_store_reply_needed = []
        _no_store_reply_needed = d.pop("no_store_reply_needed", UNSET)
        for no_store_reply_needed_item_data in _no_store_reply_needed or []:
            no_store_reply_needed_item = M11Response200DataNoStoreReplyNeeded.from_dict(no_store_reply_needed_item_data)

            no_store_reply_needed.append(no_store_reply_needed_item)

        _topic = d.pop("topic", UNSET)
        topic: Union[Unset, M11Response200DataTopic]
        if isinstance(_topic, Unset):
            topic = UNSET
        else:
            topic = M11Response200DataTopic.from_dict(_topic)

        m11_response_200_data = cls(
            authorized_participants=authorized_participants,
            current_participants=current_participants,
            customer_organization=customer_organization,
            date_created=date_created,
            date_updated=date_updated,
            entities=entities,
            id=id,
            messages=messages,
            metadata=metadata,
            no_store_reply_needed=no_store_reply_needed,
            topic=topic,
        )

        m11_response_200_data.additional_properties = d
        return m11_response_200_data

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
