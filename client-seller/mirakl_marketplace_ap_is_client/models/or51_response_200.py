import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or51_response_200_assessments import OR51Response200Assessments
    from ..models.or51_response_200_reply import OR51Response200Reply


T = TypeVar("T", bound="OR51Response200")


@_attrs_define
class OR51Response200:
    """
    Attributes:
        assessments (Union[Unset, list['OR51Response200Assessments']]): List of assessments
        comment (Union[Unset, str]): Evaluation comment
        customer_id (Union[Unset, str]): Identifier of the customer who posted the evaluation
        date (Union[Unset, datetime.datetime]): Evaluation creation date
        firstname (Union[Unset, str]): First name of the customer who posted the evaluation
        grade (Union[Unset, int]): Evaluation grade
        last_updated_date (Union[Unset, datetime.datetime]): Evaluation last updated date
        lastname (Union[Unset, str]): Last name of the customer who posted the evaluation
        reply (Union[Unset, OR51Response200Reply]):
        visible (Union[Unset, bool]): Whether the evaluation is visible or not
    """

    assessments: Union[Unset, list["OR51Response200Assessments"]] = UNSET
    comment: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    firstname: Union[Unset, str] = UNSET
    grade: Union[Unset, int] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    lastname: Union[Unset, str] = UNSET
    reply: Union[Unset, "OR51Response200Reply"] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assessments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assessments, Unset):
            assessments = []
            for assessments_item_data in self.assessments:
                assessments_item = assessments_item_data.to_dict()
                assessments.append(assessments_item)

        comment = self.comment

        customer_id = self.customer_id

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        firstname = self.firstname

        grade = self.grade

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        lastname = self.lastname

        reply: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reply, Unset):
            reply = self.reply.to_dict()

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assessments is not UNSET:
            field_dict["assessments"] = assessments
        if comment is not UNSET:
            field_dict["comment"] = comment
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if date is not UNSET:
            field_dict["date"] = date
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if grade is not UNSET:
            field_dict["grade"] = grade
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if reply is not UNSET:
            field_dict["reply"] = reply
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or51_response_200_assessments import OR51Response200Assessments
        from ..models.or51_response_200_reply import OR51Response200Reply

        d = dict(src_dict)
        assessments = []
        _assessments = d.pop("assessments", UNSET)
        for assessments_item_data in _assessments or []:
            assessments_item = OR51Response200Assessments.from_dict(assessments_item_data)

            assessments.append(assessments_item)

        comment = d.pop("comment", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        firstname = d.pop("firstname", UNSET)

        grade = d.pop("grade", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        lastname = d.pop("lastname", UNSET)

        _reply = d.pop("reply", UNSET)
        reply: Union[Unset, OR51Response200Reply]
        if isinstance(_reply, Unset):
            reply = UNSET
        else:
            reply = OR51Response200Reply.from_dict(_reply)

        visible = d.pop("visible", UNSET)

        or51_response_200 = cls(
            assessments=assessments,
            comment=comment,
            customer_id=customer_id,
            date=date,
            firstname=firstname,
            grade=grade,
            last_updated_date=last_updated_date,
            lastname=lastname,
            reply=reply,
            visible=visible,
        )

        or51_response_200.additional_properties = d
        return or51_response_200

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
