from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rt27_response_200_return_errors import RT27Response200ReturnErrors
    from ..models.rt27_response_200_return_success import RT27Response200ReturnSuccess


T = TypeVar("T", bound="RT27Response200")


@_attrs_define
class RT27Response200:
    """
    Attributes:
        return_errors (Union[Unset, list['RT27Response200ReturnErrors']]): Returns update success
        return_success (Union[Unset, list['RT27Response200ReturnSuccess']]): Returns update success
    """

    return_errors: Union[Unset, list["RT27Response200ReturnErrors"]] = UNSET
    return_success: Union[Unset, list["RT27Response200ReturnSuccess"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.return_errors, Unset):
            return_errors = []
            for return_errors_item_data in self.return_errors:
                return_errors_item = return_errors_item_data.to_dict()
                return_errors.append(return_errors_item)

        return_success: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.return_success, Unset):
            return_success = []
            for return_success_item_data in self.return_success:
                return_success_item = return_success_item_data.to_dict()
                return_success.append(return_success_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_errors is not UNSET:
            field_dict["return_errors"] = return_errors
        if return_success is not UNSET:
            field_dict["return_success"] = return_success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rt27_response_200_return_errors import RT27Response200ReturnErrors
        from ..models.rt27_response_200_return_success import RT27Response200ReturnSuccess

        d = dict(src_dict)
        return_errors = []
        _return_errors = d.pop("return_errors", UNSET)
        for return_errors_item_data in _return_errors or []:
            return_errors_item = RT27Response200ReturnErrors.from_dict(return_errors_item_data)

            return_errors.append(return_errors_item)

        return_success = []
        _return_success = d.pop("return_success", UNSET)
        for return_success_item_data in _return_success or []:
            return_success_item = RT27Response200ReturnSuccess.from_dict(return_success_item_data)

            return_success.append(return_success_item)

        rt27_response_200 = cls(
            return_errors=return_errors,
            return_success=return_success,
        )

        rt27_response_200.additional_properties = d
        return rt27_response_200

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
