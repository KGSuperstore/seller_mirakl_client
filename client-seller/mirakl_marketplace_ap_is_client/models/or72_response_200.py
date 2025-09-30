from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or72_response_200_order_documents import OR72Response200OrderDocuments


T = TypeVar("T", bound="OR72Response200")


@_attrs_define
class OR72Response200:
    """
    Attributes:
        order_documents (Union[Unset, list['OR72Response200OrderDocuments']]): The document details
    """

    order_documents: Union[Unset, list["OR72Response200OrderDocuments"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.order_documents, Unset):
            order_documents = []
            for order_documents_item_data in self.order_documents:
                order_documents_item = order_documents_item_data.to_dict()
                order_documents.append(order_documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_documents is not UNSET:
            field_dict["order_documents"] = order_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or72_response_200_order_documents import OR72Response200OrderDocuments

        d = dict(src_dict)
        order_documents = []
        _order_documents = d.pop("order_documents", UNSET)
        for order_documents_item_data in _order_documents or []:
            order_documents_item = OR72Response200OrderDocuments.from_dict(order_documents_item_data)

            order_documents.append(order_documents_item)

        or72_response_200 = cls(
            order_documents=order_documents,
        )

        or72_response_200.additional_properties = d
        return or72_response_200

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
