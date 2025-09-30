from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PC01Response200ModulesTaxManagerTaxProvider")


@_attrs_define
class PC01Response200ModulesTaxManagerTaxProvider:
    """
    Attributes:
        avalara (Union[Unset, bool]): Avalara configured as tax provider
        vertex (Union[Unset, bool]): Vertex configured as tax provider
    """

    avalara: Union[Unset, bool] = UNSET
    vertex: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avalara = self.avalara

        vertex = self.vertex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avalara is not UNSET:
            field_dict["avalara"] = avalara
        if vertex is not UNSET:
            field_dict["vertex"] = vertex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avalara = d.pop("avalara", UNSET)

        vertex = d.pop("vertex", UNSET)

        pc01_response_200_modules_tax_manager_tax_provider = cls(
            avalara=avalara,
            vertex=vertex,
        )

        pc01_response_200_modules_tax_manager_tax_provider.additional_properties = d
        return pc01_response_200_modules_tax_manager_tax_provider

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
