from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.h11_response_200_hierarchies_label_translations import H11Response200HierarchiesLabelTranslations


T = TypeVar("T", bound="H11Response200Hierarchies")


@_attrs_define
class H11Response200Hierarchies:
    """
    Attributes:
        code (Union[Unset, str]): Hierarchy code
        label (Union[Unset, str]): Hierarchy label
        label_translations (Union[Unset, list['H11Response200HierarchiesLabelTranslations']]): Hierarchy label
            translation
        level (Union[Unset, int]): Hierarchy level
        parent_code (Union[Unset, str]): Parent Hierarchy code
    """

    code: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    label_translations: Union[Unset, list["H11Response200HierarchiesLabelTranslations"]] = UNSET
    level: Union[Unset, int] = UNSET
    parent_code: Union[Unset, str] = UNSET
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

        level = self.level

        parent_code = self.parent_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if label is not UNSET:
            field_dict["label"] = label
        if label_translations is not UNSET:
            field_dict["label_translations"] = label_translations
        if level is not UNSET:
            field_dict["level"] = level
        if parent_code is not UNSET:
            field_dict["parent_code"] = parent_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.h11_response_200_hierarchies_label_translations import H11Response200HierarchiesLabelTranslations

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        label = d.pop("label", UNSET)

        label_translations = []
        _label_translations = d.pop("label_translations", UNSET)
        for label_translations_item_data in _label_translations or []:
            label_translations_item = H11Response200HierarchiesLabelTranslations.from_dict(label_translations_item_data)

            label_translations.append(label_translations_item)

        level = d.pop("level", UNSET)

        parent_code = d.pop("parent_code", UNSET)

        h11_response_200_hierarchies = cls(
            code=code,
            label=label,
            label_translations=label_translations,
            level=level,
            parent_code=parent_code,
        )

        h11_response_200_hierarchies.additional_properties = d
        return h11_response_200_hierarchies

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
