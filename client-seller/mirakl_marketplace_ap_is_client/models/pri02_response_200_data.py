import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PRI02Response200Data")


@_attrs_define
class PRI02Response200Data:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]): Import creation date
        has_error_report (Union[Unset, bool]): Indicate if an error report exists
        import_id (Union[Unset, str]): Import ID
        lines_in_error (Union[Unset, int]): Total count of lines in error
        lines_in_success (Union[Unset, int]): Total count of lines in success
        offers_in_error (Union[Unset, int]): Total count of offers in error
        offers_updated (Union[Unset, int]): Total count of updated offers
        origin (Union[Unset, str]): Import origin
        reason_status (Union[Unset, str]): Import status reason
        shop_id (Union[Unset, int]): Shop identifier
        status (Union[Unset, str]): Import status
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    has_error_report: Union[Unset, bool] = UNSET
    import_id: Union[Unset, str] = UNSET
    lines_in_error: Union[Unset, int] = UNSET
    lines_in_success: Union[Unset, int] = UNSET
    offers_in_error: Union[Unset, int] = UNSET
    offers_updated: Union[Unset, int] = UNSET
    origin: Union[Unset, str] = UNSET
    reason_status: Union[Unset, str] = UNSET
    shop_id: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        has_error_report = self.has_error_report

        import_id = self.import_id

        lines_in_error = self.lines_in_error

        lines_in_success = self.lines_in_success

        offers_in_error = self.offers_in_error

        offers_updated = self.offers_updated

        origin = self.origin

        reason_status = self.reason_status

        shop_id = self.shop_id

        status = self.status

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
        if lines_in_success is not UNSET:
            field_dict["lines_in_success"] = lines_in_success
        if offers_in_error is not UNSET:
            field_dict["offers_in_error"] = offers_in_error
        if offers_updated is not UNSET:
            field_dict["offers_updated"] = offers_updated
        if origin is not UNSET:
            field_dict["origin"] = origin
        if reason_status is not UNSET:
            field_dict["reason_status"] = reason_status
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if status is not UNSET:
            field_dict["status"] = status

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

        lines_in_success = d.pop("lines_in_success", UNSET)

        offers_in_error = d.pop("offers_in_error", UNSET)

        offers_updated = d.pop("offers_updated", UNSET)

        origin = d.pop("origin", UNSET)

        reason_status = d.pop("reason_status", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        status = d.pop("status", UNSET)

        pri02_response_200_data = cls(
            date_created=date_created,
            has_error_report=has_error_report,
            import_id=import_id,
            lines_in_error=lines_in_error,
            lines_in_success=lines_in_success,
            offers_in_error=offers_in_error,
            offers_updated=offers_updated,
            origin=origin,
            reason_status=reason_status,
            shop_id=shop_id,
            status=status,
        )

        pri02_response_200_data.additional_properties = d
        return pri02_response_200_data

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
