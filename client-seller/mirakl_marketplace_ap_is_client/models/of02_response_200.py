import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OF02Response200")


@_attrs_define
class OF02Response200:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]): Import creation date
        has_error_report (Union[Unset, bool]): Indicate if an error report exists
        import_id (Union[Unset, int]): Import ID
        lines_in_error (Union[Unset, int]): Total count of lines in error
        lines_in_pending (Union[Unset, int]): Total count of lines in pending
        lines_in_success (Union[Unset, int]): Total count of lines in success
        lines_read (Union[Unset, int]): Total count of lines read
        mode (Union[Unset, str]): Import mode
        offer_deleted (Union[Unset, int]): Total count of deleted offers
        offer_inserted (Union[Unset, int]): Total count of inserted offers
        offer_updated (Union[Unset, int]): Total count of updated offers
        reason_status (Union[Unset, str]): Import status reason
        status (Union[Unset, str]): Import status
        type_ (Union[Unset, str]): Will be remove in a future version
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    has_error_report: Union[Unset, bool] = UNSET
    import_id: Union[Unset, int] = UNSET
    lines_in_error: Union[Unset, int] = UNSET
    lines_in_pending: Union[Unset, int] = UNSET
    lines_in_success: Union[Unset, int] = UNSET
    lines_read: Union[Unset, int] = UNSET
    mode: Union[Unset, str] = UNSET
    offer_deleted: Union[Unset, int] = UNSET
    offer_inserted: Union[Unset, int] = UNSET
    offer_updated: Union[Unset, int] = UNSET
    reason_status: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        has_error_report = self.has_error_report

        import_id = self.import_id

        lines_in_error = self.lines_in_error

        lines_in_pending = self.lines_in_pending

        lines_in_success = self.lines_in_success

        lines_read = self.lines_read

        mode = self.mode

        offer_deleted = self.offer_deleted

        offer_inserted = self.offer_inserted

        offer_updated = self.offer_updated

        reason_status = self.reason_status

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if has_error_report is not UNSET:
            field_dict["has_error_report"] = has_error_report
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if lines_in_error is not UNSET:
            field_dict["lines_in_error"] = lines_in_error
        if lines_in_pending is not UNSET:
            field_dict["lines_in_pending"] = lines_in_pending
        if lines_in_success is not UNSET:
            field_dict["lines_in_success"] = lines_in_success
        if lines_read is not UNSET:
            field_dict["lines_read"] = lines_read
        if mode is not UNSET:
            field_dict["mode"] = mode
        if offer_deleted is not UNSET:
            field_dict["offer_deleted"] = offer_deleted
        if offer_inserted is not UNSET:
            field_dict["offer_inserted"] = offer_inserted
        if offer_updated is not UNSET:
            field_dict["offer_updated"] = offer_updated
        if reason_status is not UNSET:
            field_dict["reason_status"] = reason_status
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        has_error_report = d.pop("has_error_report", UNSET)

        import_id = d.pop("import_id", UNSET)

        lines_in_error = d.pop("lines_in_error", UNSET)

        lines_in_pending = d.pop("lines_in_pending", UNSET)

        lines_in_success = d.pop("lines_in_success", UNSET)

        lines_read = d.pop("lines_read", UNSET)

        mode = d.pop("mode", UNSET)

        offer_deleted = d.pop("offer_deleted", UNSET)

        offer_inserted = d.pop("offer_inserted", UNSET)

        offer_updated = d.pop("offer_updated", UNSET)

        reason_status = d.pop("reason_status", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        of02_response_200 = cls(
            date_created=date_created,
            has_error_report=has_error_report,
            import_id=import_id,
            lines_in_error=lines_in_error,
            lines_in_pending=lines_in_pending,
            lines_in_success=lines_in_success,
            lines_read=lines_read,
            mode=mode,
            offer_deleted=offer_deleted,
            offer_inserted=offer_inserted,
            offer_updated=offer_updated,
            reason_status=reason_status,
            status=status,
            type_=type_,
        )

        of02_response_200.additional_properties = d
        return of02_response_200

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
