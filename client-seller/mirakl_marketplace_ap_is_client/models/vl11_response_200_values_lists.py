from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vl11_response_200_values_lists_label_translations import VL11Response200ValuesListsLabelTranslations
    from ..models.vl11_response_200_values_lists_values import VL11Response200ValuesListsValues


T = TypeVar("T", bound="VL11Response200ValuesLists")


@_attrs_define
class VL11Response200ValuesLists:
    """
    Attributes:
        code (Union[Unset, str]): Value list code
        label (Union[Unset, str]): Value list label
        label_translations (Union[Unset, list['VL11Response200ValuesListsLabelTranslations']]): Value list translations
        values (Union[Unset, list['VL11Response200ValuesListsValues']]): Value list's of value list
    """

    code: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    label_translations: Union[Unset, list["VL11Response200ValuesListsLabelTranslations"]] = UNSET
    values: Union[Unset, list["VL11Response200ValuesListsValues"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        label = self.label

        label_translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.label_translations, Unset):
            label_translations = []
            for label_translations_item_data in self.label_translations:
                label_translations_item = label_translations_item_data.to_dict()
                label_translations.append(label_translations_item)

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if label is not UNSET:
            field_dict["label"] = label
        if label_translations is not UNSET:
            field_dict["label_translations"] = label_translations
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vl11_response_200_values_lists_label_translations import (
            VL11Response200ValuesListsLabelTranslations,
        )
        from ..models.vl11_response_200_values_lists_values import VL11Response200ValuesListsValues

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        label = d.pop("label", UNSET)

        label_translations = []
        _label_translations = d.pop("label_translations", UNSET)
        for label_translations_item_data in _label_translations or []:
            label_translations_item = VL11Response200ValuesListsLabelTranslations.from_dict(
                label_translations_item_data
            )

            label_translations.append(label_translations_item)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = VL11Response200ValuesListsValues.from_dict(values_item_data)

            values.append(values_item)

        vl11_response_200_values_lists = cls(
            code=code,
            label=label,
            label_translations=label_translations,
            values=values,
        )

        vl11_response_200_values_lists.additional_properties = d
        return vl11_response_200_values_lists

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
