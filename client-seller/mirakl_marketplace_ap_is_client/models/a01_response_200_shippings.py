from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a01_response_200_shippings_additional_fields import A01Response200ShippingsAdditionalFields


T = TypeVar("T", bound="A01Response200Shippings")


@_attrs_define
class A01Response200Shippings:
    """
    Attributes:
        additional_fields (Union[Unset, list['A01Response200ShippingsAdditionalFields']]): List of custom shipping
            fields for this shipping zone and shipping method
        shipping_free_amount (Union[Unset, float]): Minimal amount for free shipping
        shipping_type_code (Union[Unset, str]): The code of the shipping type
        shipping_type_label (Union[Unset, str]): The label of the shipping type
        shipping_type_standard_code (Union[Unset, str]): The code of the standard shipping type
        shipping_zone_code (Union[Unset, str]): The code of the shipping zone
        shipping_zone_label (Union[Unset, str]): The label of the shipping zone
    """

    additional_fields: Union[Unset, list["A01Response200ShippingsAdditionalFields"]] = UNSET
    shipping_free_amount: Union[Unset, float] = UNSET
    shipping_type_code: Union[Unset, str] = UNSET
    shipping_type_label: Union[Unset, str] = UNSET
    shipping_type_standard_code: Union[Unset, str] = UNSET
    shipping_zone_code: Union[Unset, str] = UNSET
    shipping_zone_label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_fields, Unset):
            additional_fields = []
            for additional_fields_item_data in self.additional_fields:
                additional_fields_item = additional_fields_item_data.to_dict()
                additional_fields.append(additional_fields_item)

        shipping_free_amount = self.shipping_free_amount

        shipping_type_code = self.shipping_type_code

        shipping_type_label = self.shipping_type_label

        shipping_type_standard_code = self.shipping_type_standard_code

        shipping_zone_code = self.shipping_zone_code

        shipping_zone_label = self.shipping_zone_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_fields is not UNSET:
            field_dict["additional_fields"] = additional_fields
        if shipping_free_amount is not UNSET:
            field_dict["shipping_free_amount"] = shipping_free_amount
        if shipping_type_code is not UNSET:
            field_dict["shipping_type_code"] = shipping_type_code
        if shipping_type_label is not UNSET:
            field_dict["shipping_type_label"] = shipping_type_label
        if shipping_type_standard_code is not UNSET:
            field_dict["shipping_type_standard_code"] = shipping_type_standard_code
        if shipping_zone_code is not UNSET:
            field_dict["shipping_zone_code"] = shipping_zone_code
        if shipping_zone_label is not UNSET:
            field_dict["shipping_zone_label"] = shipping_zone_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a01_response_200_shippings_additional_fields import A01Response200ShippingsAdditionalFields

        d = dict(src_dict)
        additional_fields = []
        _additional_fields = d.pop("additional_fields", UNSET)
        for additional_fields_item_data in _additional_fields or []:
            additional_fields_item = A01Response200ShippingsAdditionalFields.from_dict(additional_fields_item_data)

            additional_fields.append(additional_fields_item)

        shipping_free_amount = d.pop("shipping_free_amount", UNSET)

        shipping_type_code = d.pop("shipping_type_code", UNSET)

        shipping_type_label = d.pop("shipping_type_label", UNSET)

        shipping_type_standard_code = d.pop("shipping_type_standard_code", UNSET)

        shipping_zone_code = d.pop("shipping_zone_code", UNSET)

        shipping_zone_label = d.pop("shipping_zone_label", UNSET)

        a01_response_200_shippings = cls(
            additional_fields=additional_fields,
            shipping_free_amount=shipping_free_amount,
            shipping_type_code=shipping_type_code,
            shipping_type_label=shipping_type_label,
            shipping_type_standard_code=shipping_type_standard_code,
            shipping_zone_code=shipping_zone_code,
            shipping_zone_label=shipping_zone_label,
        )

        a01_response_200_shippings.additional_properties = d
        return a01_response_200_shippings

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
