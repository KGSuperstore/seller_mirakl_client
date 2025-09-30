from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or31_response_200_order_update_errors_errors import OR31Response200OrderUpdateErrorsErrors
    from ..models.or31_response_200_order_update_errors_input import OR31Response200OrderUpdateErrorsInput


T = TypeVar("T", bound="OR31Response200OrderUpdateErrors")


@_attrs_define
class OR31Response200OrderUpdateErrors:
    """
    Attributes:
        errors (Union[Unset, list['OR31Response200OrderUpdateErrorsErrors']]): Errors about the input object
        input_ (Union[Unset, OR31Response200OrderUpdateErrorsInput]):
    """

    errors: Union[Unset, list["OR31Response200OrderUpdateErrorsErrors"]] = UNSET
    input_: Union[Unset, "OR31Response200OrderUpdateErrorsInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        input_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or31_response_200_order_update_errors_errors import OR31Response200OrderUpdateErrorsErrors
        from ..models.or31_response_200_order_update_errors_input import OR31Response200OrderUpdateErrorsInput

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = OR31Response200OrderUpdateErrorsErrors.from_dict(errors_item_data)

            errors.append(errors_item)

        _input_ = d.pop("input", UNSET)
        input_: Union[Unset, OR31Response200OrderUpdateErrorsInput]
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = OR31Response200OrderUpdateErrorsInput.from_dict(_input_)

        or31_response_200_order_update_errors = cls(
            errors=errors,
            input_=input_,
        )

        or31_response_200_order_update_errors.additional_properties = d
        return or31_response_200_order_update_errors

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
