from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rt11_response_200_data_return_lines_compliance import RT11Response200DataReturnLinesCompliance


T = TypeVar("T", bound="RT11Response200DataReturnLines")


@_attrs_define
class RT11Response200DataReturnLines:
    """
    Attributes:
        compliance (Union[Unset, list['RT11Response200DataReturnLinesCompliance']]): Compliance
        order_line_id (Union[Unset, str]): Order line id
        quantity (Union[Unset, int]): Quantity
    """

    compliance: Union[Unset, list["RT11Response200DataReturnLinesCompliance"]] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compliance: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.compliance, Unset):
            compliance = []
            for compliance_item_data in self.compliance:
                compliance_item = compliance_item_data.to_dict()
                compliance.append(compliance_item)

        order_line_id = self.order_line_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance is not UNSET:
            field_dict["compliance"] = compliance
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rt11_response_200_data_return_lines_compliance import RT11Response200DataReturnLinesCompliance

        d = dict(src_dict)
        compliance = []
        _compliance = d.pop("compliance", UNSET)
        for compliance_item_data in _compliance or []:
            compliance_item = RT11Response200DataReturnLinesCompliance.from_dict(compliance_item_data)

            compliance.append(compliance_item)

        order_line_id = d.pop("order_line_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        rt11_response_200_data_return_lines = cls(
            compliance=compliance,
            order_line_id=order_line_id,
            quantity=quantity,
        )

        rt11_response_200_data_return_lines.additional_properties = d
        return rt11_response_200_data_return_lines

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
