from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a01_response_200_payment_details_sub_balances import A01Response200PaymentDetailsSubBalances


T = TypeVar("T", bound="A01Response200PaymentDetails")


@_attrs_define
class A01Response200PaymentDetails:
    """
    Attributes:
        paid_balance (Union[Unset, float]): Paid balance
        payable_balance (Union[Unset, float]): Payable balance
        pending_balance (Union[Unset, float]): Pending balance
        reserve_balance (Union[Unset, float]): Current reserve balance
        reserve_target (Union[Unset, float]): Configured reserve target
        sub_balances (Union[Unset, list['A01Response200PaymentDetailsSubBalances']]): Store sub-balances by pay-out PSP.
            Requires the feature Hybrid pay-out PSP to be enabled on the platform
    """

    paid_balance: Union[Unset, float] = UNSET
    payable_balance: Union[Unset, float] = UNSET
    pending_balance: Union[Unset, float] = UNSET
    reserve_balance: Union[Unset, float] = UNSET
    reserve_target: Union[Unset, float] = UNSET
    sub_balances: Union[Unset, list["A01Response200PaymentDetailsSubBalances"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid_balance = self.paid_balance

        payable_balance = self.payable_balance

        pending_balance = self.pending_balance

        reserve_balance = self.reserve_balance

        reserve_target = self.reserve_target

        sub_balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sub_balances, Unset):
            sub_balances = []
            for sub_balances_item_data in self.sub_balances:
                sub_balances_item = sub_balances_item_data.to_dict()
                sub_balances.append(sub_balances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paid_balance is not UNSET:
            field_dict["paid_balance"] = paid_balance
        if payable_balance is not UNSET:
            field_dict["payable_balance"] = payable_balance
        if pending_balance is not UNSET:
            field_dict["pending_balance"] = pending_balance
        if reserve_balance is not UNSET:
            field_dict["reserve_balance"] = reserve_balance
        if reserve_target is not UNSET:
            field_dict["reserve_target"] = reserve_target
        if sub_balances is not UNSET:
            field_dict["sub_balances"] = sub_balances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a01_response_200_payment_details_sub_balances import A01Response200PaymentDetailsSubBalances

        d = dict(src_dict)
        paid_balance = d.pop("paid_balance", UNSET)

        payable_balance = d.pop("payable_balance", UNSET)

        pending_balance = d.pop("pending_balance", UNSET)

        reserve_balance = d.pop("reserve_balance", UNSET)

        reserve_target = d.pop("reserve_target", UNSET)

        sub_balances = []
        _sub_balances = d.pop("sub_balances", UNSET)
        for sub_balances_item_data in _sub_balances or []:
            sub_balances_item = A01Response200PaymentDetailsSubBalances.from_dict(sub_balances_item_data)

            sub_balances.append(sub_balances_item)

        a01_response_200_payment_details = cls(
            paid_balance=paid_balance,
            payable_balance=payable_balance,
            pending_balance=pending_balance,
            reserve_balance=reserve_balance,
            reserve_target=reserve_target,
            sub_balances=sub_balances,
        )

        a01_response_200_payment_details.additional_properties = d
        return a01_response_200_payment_details

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
