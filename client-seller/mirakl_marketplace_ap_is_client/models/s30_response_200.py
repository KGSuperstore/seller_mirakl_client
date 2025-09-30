from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s30_response_200_shop_documents import S30Response200ShopDocuments


T = TypeVar("T", bound="S30Response200")


@_attrs_define
class S30Response200:
    """
    Attributes:
        shop_documents (Union[Unset, list['S30Response200ShopDocuments']]): Document details
    """

    shop_documents: Union[Unset, list["S30Response200ShopDocuments"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shop_documents, Unset):
            shop_documents = []
            for shop_documents_item_data in self.shop_documents:
                shop_documents_item = shop_documents_item_data.to_dict()
                shop_documents.append(shop_documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_documents is not UNSET:
            field_dict["shop_documents"] = shop_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s30_response_200_shop_documents import S30Response200ShopDocuments

        d = dict(src_dict)
        shop_documents = []
        _shop_documents = d.pop("shop_documents", UNSET)
        for shop_documents_item_data in _shop_documents or []:
            shop_documents_item = S30Response200ShopDocuments.from_dict(shop_documents_item_data)

            shop_documents.append(shop_documents_item)

        s30_response_200 = cls(
            shop_documents=shop_documents,
        )

        s30_response_200.additional_properties = d
        return s30_response_200

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
