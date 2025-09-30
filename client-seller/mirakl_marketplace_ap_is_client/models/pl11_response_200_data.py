import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pl11_response_200_data_order_lines import PL11Response200DataOrderLines
    from ..models.pl11_response_200_data_picklist_lines import PL11Response200DataPicklistLines


T = TypeVar("T", bound="PL11Response200Data")


@_attrs_define
class PL11Response200Data:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]): Picklist creation date
        id (Union[Unset, str]): Picklist identifier
        last_updated (Union[Unset, datetime.datetime]): Picklist last update date
        order_lines (Union[Unset, list['PL11Response200DataOrderLines']]): Picklist order line identifiers
        picklist_lines (Union[Unset, list['PL11Response200DataPicklistLines']]): Picklist lines
        pickrun_code (Union[Unset, str]): Pickrun code
        pickup_date (Union[Unset, datetime.datetime]): Pickup date
        shop_id (Union[Unset, int]): Picklist shop identifier
        state (Union[Unset, str]): Picklist state
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    order_lines: Union[Unset, list["PL11Response200DataOrderLines"]] = UNSET
    picklist_lines: Union[Unset, list["PL11Response200DataPicklistLines"]] = UNSET
    pickrun_code: Union[Unset, str] = UNSET
    pickup_date: Union[Unset, datetime.datetime] = UNSET
    shop_id: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        order_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            order_lines = []
            for order_lines_item_data in self.order_lines:
                order_lines_item = order_lines_item_data.to_dict()
                order_lines.append(order_lines_item)

        picklist_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.picklist_lines, Unset):
            picklist_lines = []
            for picklist_lines_item_data in self.picklist_lines:
                picklist_lines_item = picklist_lines_item_data.to_dict()
                picklist_lines.append(picklist_lines_item)

        pickrun_code = self.pickrun_code

        pickup_date: Union[Unset, str] = UNSET
        if not isinstance(self.pickup_date, Unset):
            pickup_date = self.pickup_date.isoformat()

        shop_id = self.shop_id

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if order_lines is not UNSET:
            field_dict["order_lines"] = order_lines
        if picklist_lines is not UNSET:
            field_dict["picklist_lines"] = picklist_lines
        if pickrun_code is not UNSET:
            field_dict["pickrun_code"] = pickrun_code
        if pickup_date is not UNSET:
            field_dict["pickup_date"] = pickup_date
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pl11_response_200_data_order_lines import PL11Response200DataOrderLines
        from ..models.pl11_response_200_data_picklist_lines import PL11Response200DataPicklistLines

        d = dict(src_dict)
        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        order_lines = []
        _order_lines = d.pop("order_lines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = PL11Response200DataOrderLines.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        picklist_lines = []
        _picklist_lines = d.pop("picklist_lines", UNSET)
        for picklist_lines_item_data in _picklist_lines or []:
            picklist_lines_item = PL11Response200DataPicklistLines.from_dict(picklist_lines_item_data)

            picklist_lines.append(picklist_lines_item)

        pickrun_code = d.pop("pickrun_code", UNSET)

        _pickup_date = d.pop("pickup_date", UNSET)
        pickup_date: Union[Unset, datetime.datetime]
        if isinstance(_pickup_date, Unset):
            pickup_date = UNSET
        else:
            pickup_date = isoparse(_pickup_date)

        shop_id = d.pop("shop_id", UNSET)

        state = d.pop("state", UNSET)

        pl11_response_200_data = cls(
            date_created=date_created,
            id=id,
            last_updated=last_updated,
            order_lines=order_lines,
            picklist_lines=picklist_lines,
            pickrun_code=pickrun_code,
            pickup_date=pickup_date,
            shop_id=shop_id,
            state=state,
        )

        pl11_response_200_data.additional_properties = d
        return pl11_response_200_data

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
