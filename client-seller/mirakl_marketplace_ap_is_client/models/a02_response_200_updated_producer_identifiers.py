from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="A02Response200UpdatedProducerIdentifiers")


@_attrs_define
class A02Response200UpdatedProducerIdentifiers:
    """
    Attributes:
        epr_category_code (Union[Unset, str]): Extended Producer Responsibility (EPR) category code.
        producer_id (Union[Unset, str]): Shop producer identifier.
    """

    epr_category_code: Union[Unset, str] = UNSET
    producer_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        epr_category_code = self.epr_category_code

        producer_id = self.producer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epr_category_code is not UNSET:
            field_dict["epr_category_code"] = epr_category_code
        if producer_id is not UNSET:
            field_dict["producer_id"] = producer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        epr_category_code = d.pop("epr_category_code", UNSET)

        producer_id = d.pop("producer_id", UNSET)

        a02_response_200_updated_producer_identifiers = cls(
            epr_category_code=epr_category_code,
            producer_id=producer_id,
        )

        a02_response_200_updated_producer_identifiers.additional_properties = d
        return a02_response_200_updated_producer_identifiers

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
