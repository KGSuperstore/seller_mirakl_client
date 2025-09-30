from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pm11_response_200_attributes_channels import PM11Response200AttributesChannels
    from ..models.pm11_response_200_attributes_description_translations import (
        PM11Response200AttributesDescriptionTranslations,
    )
    from ..models.pm11_response_200_attributes_label_translations import PM11Response200AttributesLabelTranslations
    from ..models.pm11_response_200_attributes_roles import PM11Response200AttributesRoles
    from ..models.pm11_response_200_attributes_type_parameters import PM11Response200AttributesTypeParameters
    from ..models.pm11_response_200_attributes_values import PM11Response200AttributesValues


T = TypeVar("T", bound="PM11Response200Attributes")


@_attrs_define
class PM11Response200Attributes:
    """
    Attributes:
        channels (Union[Unset, list['PM11Response200AttributesChannels']]): Channels
        code (Union[Unset, str]): Attribute code
        default_value (Union[Unset, str]): Default value for value list type attributes
        description (Union[Unset, str]): Attribute description
        description_translations (Union[Unset, list['PM11Response200AttributesDescriptionTranslations']]): Translations
            of the attribute description
        example (Union[Unset, str]): Attribute example to help sellers when they fill the product creation form
        hierarchy_code (Union[Unset, str]): The code of the hierarchy (category) this attribute belongs to. If this
            field is empty, the attribute is shared among all hierarchies.
        label (Union[Unset, str]): Attribute label
        label_translations (Union[Unset, list['PM11Response200AttributesLabelTranslations']]): Translations of the
            attribute label
        locale (Union[Unset, str]): Attribute localization.<br/>
            The language format can either be:<br/>
            <ul>
               <li>ISO-639 (E.g. "en")</li>
               <li>ISO-639_ISO-3166 (E.g. "en_US")</li>
            </ul>
        required (Union[Unset, bool]): Whether or not the attribute is required
        requirement_level (Union[Unset, str]): Requirement level of the attribute
        roles (Union[Unset, list['PM11Response200AttributesRoles']]): Attribute roles
        transformations (Union[Unset, str]): Transformations applied to the attribute (a list of transformations
            separated by commas)
        type_ (Union[Unset, str]): Attribute type
        type_parameter (Union[Unset, str]): Type parameter
        type_parameters (Union[Unset, list['PM11Response200AttributesTypeParameters']]): Specificities of the attribute
            type, for example the date format, or the maximum size of a media
        unique_code (Union[Unset, str]): Unique code of the attribute
        validations (Union[Unset, str]): Validations applied to the attribute (a list of validations separated by
            commas)
        values (Union[Unset, list['PM11Response200AttributesValues']]): A list of authorized values for this attribute
        values_list (Union[Unset, str]): This code points to the list defining the authorized values for this attribute.
        variant (Union[Unset, bool]): Whether or not the attribute is a variation axis. Possible values:
            <code>true</code> or <code>false</code>
    """

    channels: Union[Unset, list["PM11Response200AttributesChannels"]] = UNSET
    code: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    description_translations: Union[Unset, list["PM11Response200AttributesDescriptionTranslations"]] = UNSET
    example: Union[Unset, str] = UNSET
    hierarchy_code: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    label_translations: Union[Unset, list["PM11Response200AttributesLabelTranslations"]] = UNSET
    locale: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    requirement_level: Union[Unset, str] = UNSET
    roles: Union[Unset, list["PM11Response200AttributesRoles"]] = UNSET
    transformations: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    type_parameter: Union[Unset, str] = UNSET
    type_parameters: Union[Unset, list["PM11Response200AttributesTypeParameters"]] = UNSET
    unique_code: Union[Unset, str] = UNSET
    validations: Union[Unset, str] = UNSET
    values: Union[Unset, list["PM11Response200AttributesValues"]] = UNSET
    values_list: Union[Unset, str] = UNSET
    variant: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        code = self.code

        default_value = self.default_value

        description = self.description

        description_translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.description_translations, Unset):
            description_translations = []
            for description_translations_item_data in self.description_translations:
                description_translations_item = description_translations_item_data.to_dict()
                description_translations.append(description_translations_item)

        example = self.example

        hierarchy_code = self.hierarchy_code

        label = self.label

        label_translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.label_translations, Unset):
            label_translations = []
            for label_translations_item_data in self.label_translations:
                label_translations_item = label_translations_item_data.to_dict()
                label_translations.append(label_translations_item)

        locale = self.locale

        required = self.required

        requirement_level = self.requirement_level

        roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        transformations = self.transformations

        type_ = self.type_

        type_parameter = self.type_parameter

        type_parameters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.type_parameters, Unset):
            type_parameters = []
            for type_parameters_item_data in self.type_parameters:
                type_parameters_item = type_parameters_item_data.to_dict()
                type_parameters.append(type_parameters_item)

        unique_code = self.unique_code

        validations = self.validations

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        values_list = self.values_list

        variant = self.variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if code is not UNSET:
            field_dict["code"] = code
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if description_translations is not UNSET:
            field_dict["description_translations"] = description_translations
        if example is not UNSET:
            field_dict["example"] = example
        if hierarchy_code is not UNSET:
            field_dict["hierarchy_code"] = hierarchy_code
        if label is not UNSET:
            field_dict["label"] = label
        if label_translations is not UNSET:
            field_dict["label_translations"] = label_translations
        if locale is not UNSET:
            field_dict["locale"] = locale
        if required is not UNSET:
            field_dict["required"] = required
        if requirement_level is not UNSET:
            field_dict["requirement_level"] = requirement_level
        if roles is not UNSET:
            field_dict["roles"] = roles
        if transformations is not UNSET:
            field_dict["transformations"] = transformations
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_parameter is not UNSET:
            field_dict["type_parameter"] = type_parameter
        if type_parameters is not UNSET:
            field_dict["type_parameters"] = type_parameters
        if unique_code is not UNSET:
            field_dict["unique_code"] = unique_code
        if validations is not UNSET:
            field_dict["validations"] = validations
        if values is not UNSET:
            field_dict["values"] = values
        if values_list is not UNSET:
            field_dict["values_list"] = values_list
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pm11_response_200_attributes_channels import PM11Response200AttributesChannels
        from ..models.pm11_response_200_attributes_description_translations import (
            PM11Response200AttributesDescriptionTranslations,
        )
        from ..models.pm11_response_200_attributes_label_translations import PM11Response200AttributesLabelTranslations
        from ..models.pm11_response_200_attributes_roles import PM11Response200AttributesRoles
        from ..models.pm11_response_200_attributes_type_parameters import PM11Response200AttributesTypeParameters
        from ..models.pm11_response_200_attributes_values import PM11Response200AttributesValues

        d = dict(src_dict)
        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = PM11Response200AttributesChannels.from_dict(channels_item_data)

            channels.append(channels_item)

        code = d.pop("code", UNSET)

        default_value = d.pop("default_value", UNSET)

        description = d.pop("description", UNSET)

        description_translations = []
        _description_translations = d.pop("description_translations", UNSET)
        for description_translations_item_data in _description_translations or []:
            description_translations_item = PM11Response200AttributesDescriptionTranslations.from_dict(
                description_translations_item_data
            )

            description_translations.append(description_translations_item)

        example = d.pop("example", UNSET)

        hierarchy_code = d.pop("hierarchy_code", UNSET)

        label = d.pop("label", UNSET)

        label_translations = []
        _label_translations = d.pop("label_translations", UNSET)
        for label_translations_item_data in _label_translations or []:
            label_translations_item = PM11Response200AttributesLabelTranslations.from_dict(label_translations_item_data)

            label_translations.append(label_translations_item)

        locale = d.pop("locale", UNSET)

        required = d.pop("required", UNSET)

        requirement_level = d.pop("requirement_level", UNSET)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = PM11Response200AttributesRoles.from_dict(roles_item_data)

            roles.append(roles_item)

        transformations = d.pop("transformations", UNSET)

        type_ = d.pop("type", UNSET)

        type_parameter = d.pop("type_parameter", UNSET)

        type_parameters = []
        _type_parameters = d.pop("type_parameters", UNSET)
        for type_parameters_item_data in _type_parameters or []:
            type_parameters_item = PM11Response200AttributesTypeParameters.from_dict(type_parameters_item_data)

            type_parameters.append(type_parameters_item)

        unique_code = d.pop("unique_code", UNSET)

        validations = d.pop("validations", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = PM11Response200AttributesValues.from_dict(values_item_data)

            values.append(values_item)

        values_list = d.pop("values_list", UNSET)

        variant = d.pop("variant", UNSET)

        pm11_response_200_attributes = cls(
            channels=channels,
            code=code,
            default_value=default_value,
            description=description,
            description_translations=description_translations,
            example=example,
            hierarchy_code=hierarchy_code,
            label=label,
            label_translations=label_translations,
            locale=locale,
            required=required,
            requirement_level=requirement_level,
            roles=roles,
            transformations=transformations,
            type_=type_,
            type_parameter=type_parameter,
            type_parameters=type_parameters,
            unique_code=unique_code,
            validations=validations,
            values=values,
            values_list=values_list,
            variant=variant,
        )

        pm11_response_200_attributes.additional_properties = d
        return pm11_response_200_attributes

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
