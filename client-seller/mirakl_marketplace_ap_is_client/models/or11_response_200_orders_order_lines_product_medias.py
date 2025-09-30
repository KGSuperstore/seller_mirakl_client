from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OR11Response200OrdersOrderLinesProductMedias")


@_attrs_define
class OR11Response200OrdersOrderLinesProductMedias:
    """
    Attributes:
        media_url (Union[Unset, str]): Media URL
        mime_type (Union[Unset, str]): Media MIME Type (.jpg, .png ...)
        type_ (Union[Unset, str]): Media TYPE (small, large...)
    """

    media_url: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_url = self.media_url

        mime_type = self.mime_type

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_url = d.pop("media_url", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        type_ = d.pop("type", UNSET)

        or11_response_200_orders_order_lines_product_medias = cls(
            media_url=media_url,
            mime_type=mime_type,
            type_=type_,
        )

        or11_response_200_orders_order_lines_product_medias.additional_properties = d
        return or11_response_200_orders_order_lines_product_medias

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
