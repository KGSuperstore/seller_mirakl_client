from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.st12_response_200_data import ST12Response200Data


T = TypeVar("T", bound="ST12Response200")


@_attrs_define
class ST12Response200:
    """
    Attributes:
        data (Union[Unset, list['ST12Response200Data']]): Page of data
        next_page_token (Union[Unset, str]): Token to access the next page. Absent if the current page is the last one.
        previous_page_token (Union[Unset, str]): Token to access the previous page. Absent if the current page is the
            first one.
    """

    data: Union[Unset, list["ST12Response200Data"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    previous_page_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        next_page_token = self.next_page_token

        previous_page_token = self.previous_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if previous_page_token is not UNSET:
            field_dict["previous_page_token"] = previous_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.st12_response_200_data import ST12Response200Data

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ST12Response200Data.from_dict(data_item_data)

            data.append(data_item)

        next_page_token = d.pop("next_page_token", UNSET)

        previous_page_token = d.pop("previous_page_token", UNSET)

        st12_response_200 = cls(
            data=data,
            next_page_token=next_page_token,
            previous_page_token=previous_page_token,
        )

        st12_response_200.additional_properties = d
        return st12_response_200

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
