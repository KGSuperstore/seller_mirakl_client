from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or31_response_200_order_update_errors import OR31Response200OrderUpdateErrors
    from ..models.or31_response_200_order_update_result import OR31Response200OrderUpdateResult


T = TypeVar("T", bound="OR31Response200")


@_attrs_define
class OR31Response200:
    """
    Attributes:
        order_update_errors (Union[Unset, OR31Response200OrderUpdateErrors]):
        order_update_result (Union[Unset, OR31Response200OrderUpdateResult]):
    """

    order_update_errors: Union[Unset, "OR31Response200OrderUpdateErrors"] = UNSET
    order_update_result: Union[Unset, "OR31Response200OrderUpdateResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_update_errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_update_errors, Unset):
            order_update_errors = self.order_update_errors.to_dict()

        order_update_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_update_result, Unset):
            order_update_result = self.order_update_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_update_errors is not UNSET:
            field_dict["order_update_errors"] = order_update_errors
        if order_update_result is not UNSET:
            field_dict["order_update_result"] = order_update_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or31_response_200_order_update_errors import OR31Response200OrderUpdateErrors
        from ..models.or31_response_200_order_update_result import OR31Response200OrderUpdateResult

        d = dict(src_dict)
        _order_update_errors = d.pop("order_update_errors", UNSET)
        order_update_errors: Union[Unset, OR31Response200OrderUpdateErrors]
        if isinstance(_order_update_errors, Unset):
            order_update_errors = UNSET
        else:
            order_update_errors = OR31Response200OrderUpdateErrors.from_dict(_order_update_errors)

        _order_update_result = d.pop("order_update_result", UNSET)
        order_update_result: Union[Unset, OR31Response200OrderUpdateResult]
        if isinstance(_order_update_result, Unset):
            order_update_result = UNSET
        else:
            order_update_result = OR31Response200OrderUpdateResult.from_dict(_order_update_result)

        or31_response_200 = cls(
            order_update_errors=order_update_errors,
            order_update_result=order_update_result,
        )

        or31_response_200.additional_properties = d
        return or31_response_200

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
