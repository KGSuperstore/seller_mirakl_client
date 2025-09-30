from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sh31_response_200_logistic_classes import SH31Response200LogisticClasses


T = TypeVar("T", bound="SH31Response200")


@_attrs_define
class SH31Response200:
    """
    Attributes:
        logistic_classes (Union[Unset, list['SH31Response200LogisticClasses']]): List of logistic classes
    """

    logistic_classes: Union[Unset, list["SH31Response200LogisticClasses"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logistic_classes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logistic_classes, Unset):
            logistic_classes = []
            for logistic_classes_item_data in self.logistic_classes:
                logistic_classes_item = logistic_classes_item_data.to_dict()
                logistic_classes.append(logistic_classes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logistic_classes is not UNSET:
            field_dict["logistic_classes"] = logistic_classes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sh31_response_200_logistic_classes import SH31Response200LogisticClasses

        d = dict(src_dict)
        logistic_classes = []
        _logistic_classes = d.pop("logistic_classes", UNSET)
        for logistic_classes_item_data in _logistic_classes or []:
            logistic_classes_item = SH31Response200LogisticClasses.from_dict(logistic_classes_item_data)

            logistic_classes.append(logistic_classes_item)

        sh31_response_200 = cls(
            logistic_classes=logistic_classes,
        )

        sh31_response_200.additional_properties = d
        return sh31_response_200

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
