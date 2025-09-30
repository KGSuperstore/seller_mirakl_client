from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or04_response_200_updated_orders_errors import OR04Response200UpdatedOrdersErrors
    from ..models.or04_response_200_updated_orders_updated import OR04Response200UpdatedOrdersUpdated


T = TypeVar("T", bound="OR04Response200UpdatedOrders")


@_attrs_define
class OR04Response200UpdatedOrders:
    """
    Attributes:
        errors (Union[Unset, list['OR04Response200UpdatedOrdersErrors']]): List of errors encountered when updating
            order
        order_id (Union[Unset, str]): Order identifier
        updated (Union[Unset, OR04Response200UpdatedOrdersUpdated]):
    """

    errors: Union[Unset, list["OR04Response200UpdatedOrdersErrors"]] = UNSET
    order_id: Union[Unset, str] = UNSET
    updated: Union[Unset, "OR04Response200UpdatedOrdersUpdated"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        order_id = self.order_id

        updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or04_response_200_updated_orders_errors import OR04Response200UpdatedOrdersErrors
        from ..models.or04_response_200_updated_orders_updated import OR04Response200UpdatedOrdersUpdated

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = OR04Response200UpdatedOrdersErrors.from_dict(errors_item_data)

            errors.append(errors_item)

        order_id = d.pop("order_id", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, OR04Response200UpdatedOrdersUpdated]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = OR04Response200UpdatedOrdersUpdated.from_dict(_updated)

        or04_response_200_updated_orders = cls(
            errors=errors,
            order_id=order_id,
            updated=updated,
        )

        or04_response_200_updated_orders.additional_properties = d
        return or04_response_200_updated_orders

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
