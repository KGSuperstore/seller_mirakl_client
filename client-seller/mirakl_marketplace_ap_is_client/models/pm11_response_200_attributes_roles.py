from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pm11_response_200_attributes_roles_parameters import PM11Response200AttributesRolesParameters


T = TypeVar("T", bound="PM11Response200AttributesRoles")


@_attrs_define
class PM11Response200AttributesRoles:
    """
    Attributes:
        parameters (Union[Unset, list['PM11Response200AttributesRolesParameters']]): Attribute role parameters
        type_ (Union[Unset, str]): Role type of the attribute
    """

    parameters: Union[Unset, list["PM11Response200AttributesRolesParameters"]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pm11_response_200_attributes_roles_parameters import PM11Response200AttributesRolesParameters

        d = dict(src_dict)
        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = PM11Response200AttributesRolesParameters.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        type_ = d.pop("type", UNSET)

        pm11_response_200_attributes_roles = cls(
            parameters=parameters,
            type_=type_,
        )

        pm11_response_200_attributes_roles.additional_properties = d
        return pm11_response_200_attributes_roles

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
