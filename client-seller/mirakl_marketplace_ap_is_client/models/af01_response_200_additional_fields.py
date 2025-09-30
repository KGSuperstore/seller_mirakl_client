from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AF01Response200AdditionalFields")


@_attrs_define
class AF01Response200AdditionalFields:
    """
    Attributes:
        accepted_values (Union[Unset, list[str]]): The list of accepted values for this additional field. This field is
            only present for additional fields of type 'LIST'
        code (Union[Unset, str]): Additional field code
        description (Union[Unset, str]): The description of the additional field.
        editable (Union[Unset, bool]): Whether or not the additional field will be editable
        entity (Union[Unset, str]): The object on which the additional field applies
        label (Union[Unset, str]): Additional field label
        regex (Union[Unset, str]): The regular expression that is used to validate the value value of this
            field.<br/>This field is only present for additional fields of type 'REGEX'.
        required (Union[Unset, bool]): Whether or not this additionnal field will be required
        type_ (Union[Unset, str]): Additional field type:<ul><li><strong>STRING</strong> chain of characters (up to 2000
            characters)</li><li><strong>DATE</strong> date in yyyy-mm-dd format</li><li><strong>NUMERIC</strong> decimal
            value (eg 52.63)</li><li><strong>BOOLEAN</strong> true or false</li><li><strong>LINK</strong> valid
            URL</li><li><strong>LIST</strong> list of values. Valid values are specified in accepted_values
            field</li><li><strong>REGEX</strong> regular expression. The regex that is used to validate the value of this
            field is specified in the regex field</li><li><strong>TEXTAREA</strong> long chain of characters (up to 5000
            characters). May have multiple lines</li></ul>
    """

    accepted_values: Union[Unset, list[str]] = UNSET
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    editable: Union[Unset, bool] = UNSET
    entity: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    regex: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.accepted_values, Unset):
            accepted_values = self.accepted_values

        code = self.code

        description = self.description

        editable = self.editable

        entity = self.entity

        label = self.label

        regex = self.regex

        required = self.required

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_values is not UNSET:
            field_dict["accepted_values"] = accepted_values
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if editable is not UNSET:
            field_dict["editable"] = editable
        if entity is not UNSET:
            field_dict["entity"] = entity
        if label is not UNSET:
            field_dict["label"] = label
        if regex is not UNSET:
            field_dict["regex"] = regex
        if required is not UNSET:
            field_dict["required"] = required
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted_values = cast(list[str], d.pop("accepted_values", UNSET))

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        editable = d.pop("editable", UNSET)

        entity = d.pop("entity", UNSET)

        label = d.pop("label", UNSET)

        regex = d.pop("regex", UNSET)

        required = d.pop("required", UNSET)

        type_ = d.pop("type", UNSET)

        af01_response_200_additional_fields = cls(
            accepted_values=accepted_values,
            code=code,
            description=description,
            editable=editable,
            entity=entity,
            label=label,
            regex=regex,
            required=required,
            type_=type_,
        )

        af01_response_200_additional_fields.additional_properties = d
        return af01_response_200_additional_fields

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
