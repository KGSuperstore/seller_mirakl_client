from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.of61_response_200_offer_states import OF61Response200OfferStates


T = TypeVar("T", bound="OF61Response200")


@_attrs_define
class OF61Response200:
    """
    Attributes:
        offer_states (Union[Unset, list['OF61Response200OfferStates']]): Offer conditions
    """

    offer_states: Union[Unset, list["OF61Response200OfferStates"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_states: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.offer_states, Unset):
            offer_states = []
            for offer_states_item_data in self.offer_states:
                offer_states_item = offer_states_item_data.to_dict()
                offer_states.append(offer_states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer_states is not UNSET:
            field_dict["offer_states"] = offer_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.of61_response_200_offer_states import OF61Response200OfferStates

        d = dict(src_dict)
        offer_states = []
        _offer_states = d.pop("offer_states", UNSET)
        for offer_states_item_data in _offer_states or []:
            offer_states_item = OF61Response200OfferStates.from_dict(offer_states_item_data)

            offer_states.append(offer_states_item)

        of61_response_200 = cls(
            offer_states=offer_states,
        )

        of61_response_200.additional_properties = d
        return of61_response_200

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
