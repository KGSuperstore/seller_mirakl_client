from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="P11Response200ProductsProductMedia")


@_attrs_define
class P11Response200ProductsProductMedia:
    """
    Attributes:
        dam_url (Union[Unset, str]): DAM URL for the media provided when available, otherwise use <code>media_url</code>
        media_url (Union[Unset, str]): Media URL
        type_ (Union[Unset, str]): Media TYPE (small, large...)
    """

    dam_url: Union[Unset, str] = UNSET
    media_url: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dam_url = self.dam_url

        media_url = self.media_url

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dam_url is not UNSET:
            field_dict["dam_url"] = dam_url
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dam_url = d.pop("dam_url", UNSET)

        media_url = d.pop("media_url", UNSET)

        type_ = d.pop("type", UNSET)

        p11_response_200_products_product_media = cls(
            dam_url=dam_url,
            media_url=media_url,
            type_=type_,
        )

        p11_response_200_products_product_media.additional_properties = d
        return p11_response_200_products_product_media

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
