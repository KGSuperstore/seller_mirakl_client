import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rt04_response_200_return_success_documents import RT04Response200ReturnSuccessDocuments
    from ..models.rt04_response_200_return_success_return_address import RT04Response200ReturnSuccessReturnAddress
    from ..models.rt04_response_200_return_success_return_lines import RT04Response200ReturnSuccessReturnLines
    from ..models.rt04_response_200_return_success_tracking import RT04Response200ReturnSuccessTracking


T = TypeVar("T", bound="RT04Response200ReturnSuccess")


@_attrs_define
class RT04Response200ReturnSuccess:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]): Return creation date
        description (Union[Unset, str]): Description
        documents (Union[Unset, list['RT04Response200ReturnSuccessDocuments']]): Return documents
        id (Union[Unset, str]): Return id
        label_url (Union[Unset, str]): Label URL
        last_updated (Union[Unset, datetime.datetime]): Return last updated date
        method_code (Union[Unset, str]): Return method code
        order_commercial_id (Union[Unset, str]): Order commercial id
        order_id (Union[Unset, str]): Order id
        reason_code (Union[Unset, str]): Return reason code
        rejection_reason_code (Union[Unset, str]): Return rejection reason code
        return_address (Union[Unset, RT04Response200ReturnSuccessReturnAddress]):
        return_lines (Union[Unset, list['RT04Response200ReturnSuccessReturnLines']]): Return lines
        rma (Union[Unset, str]): Return RMA
        state (Union[Unset, str]): Return state
        tracking (Union[Unset, RT04Response200ReturnSuccessTracking]):
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    documents: Union[Unset, list["RT04Response200ReturnSuccessDocuments"]] = UNSET
    id: Union[Unset, str] = UNSET
    label_url: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    method_code: Union[Unset, str] = UNSET
    order_commercial_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    reason_code: Union[Unset, str] = UNSET
    rejection_reason_code: Union[Unset, str] = UNSET
    return_address: Union[Unset, "RT04Response200ReturnSuccessReturnAddress"] = UNSET
    return_lines: Union[Unset, list["RT04Response200ReturnSuccessReturnLines"]] = UNSET
    rma: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    tracking: Union[Unset, "RT04Response200ReturnSuccessTracking"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        description = self.description

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        id = self.id

        label_url = self.label_url

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        method_code = self.method_code

        order_commercial_id = self.order_commercial_id

        order_id = self.order_id

        reason_code = self.reason_code

        rejection_reason_code = self.rejection_reason_code

        return_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.return_address, Unset):
            return_address = self.return_address.to_dict()

        return_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.return_lines, Unset):
            return_lines = []
            for return_lines_item_data in self.return_lines:
                return_lines_item = return_lines_item_data.to_dict()
                return_lines.append(return_lines_item)

        rma = self.rma

        state = self.state

        tracking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if description is not UNSET:
            field_dict["description"] = description
        if documents is not UNSET:
            field_dict["documents"] = documents
        if id is not UNSET:
            field_dict["id"] = id
        if label_url is not UNSET:
            field_dict["label_url"] = label_url
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if method_code is not UNSET:
            field_dict["method_code"] = method_code
        if order_commercial_id is not UNSET:
            field_dict["order_commercial_id"] = order_commercial_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if rejection_reason_code is not UNSET:
            field_dict["rejection_reason_code"] = rejection_reason_code
        if return_address is not UNSET:
            field_dict["return_address"] = return_address
        if return_lines is not UNSET:
            field_dict["return_lines"] = return_lines
        if rma is not UNSET:
            field_dict["rma"] = rma
        if state is not UNSET:
            field_dict["state"] = state
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rt04_response_200_return_success_documents import RT04Response200ReturnSuccessDocuments
        from ..models.rt04_response_200_return_success_return_address import RT04Response200ReturnSuccessReturnAddress
        from ..models.rt04_response_200_return_success_return_lines import RT04Response200ReturnSuccessReturnLines
        from ..models.rt04_response_200_return_success_tracking import RT04Response200ReturnSuccessTracking

        d = dict(src_dict)
        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        description = d.pop("description", UNSET)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = RT04Response200ReturnSuccessDocuments.from_dict(documents_item_data)

            documents.append(documents_item)

        id = d.pop("id", UNSET)

        label_url = d.pop("label_url", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        method_code = d.pop("method_code", UNSET)

        order_commercial_id = d.pop("order_commercial_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        reason_code = d.pop("reason_code", UNSET)

        rejection_reason_code = d.pop("rejection_reason_code", UNSET)

        _return_address = d.pop("return_address", UNSET)
        return_address: Union[Unset, RT04Response200ReturnSuccessReturnAddress]
        if isinstance(_return_address, Unset):
            return_address = UNSET
        else:
            return_address = RT04Response200ReturnSuccessReturnAddress.from_dict(_return_address)

        return_lines = []
        _return_lines = d.pop("return_lines", UNSET)
        for return_lines_item_data in _return_lines or []:
            return_lines_item = RT04Response200ReturnSuccessReturnLines.from_dict(return_lines_item_data)

            return_lines.append(return_lines_item)

        rma = d.pop("rma", UNSET)

        state = d.pop("state", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, RT04Response200ReturnSuccessTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = RT04Response200ReturnSuccessTracking.from_dict(_tracking)

        rt04_response_200_return_success = cls(
            date_created=date_created,
            description=description,
            documents=documents,
            id=id,
            label_url=label_url,
            last_updated=last_updated,
            method_code=method_code,
            order_commercial_id=order_commercial_id,
            order_id=order_id,
            reason_code=reason_code,
            rejection_reason_code=rejection_reason_code,
            return_address=return_address,
            return_lines=return_lines,
            rma=rma,
            state=state,
            tracking=tracking,
        )

        rt04_response_200_return_success.additional_properties = d
        return rt04_response_200_return_success

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
