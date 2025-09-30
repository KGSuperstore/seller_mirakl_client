from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.or11_response_200_orders_promotions_applied_promotions_campaign import (
        OR11Response200OrdersPromotionsAppliedPromotionsCampaign,
    )
    from ..models.or11_response_200_orders_promotions_applied_promotions_configuration import (
        OR11Response200OrdersPromotionsAppliedPromotionsConfiguration,
    )


T = TypeVar("T", bound="OR11Response200OrdersPromotionsAppliedPromotions")


@_attrs_define
class OR11Response200OrdersPromotionsAppliedPromotions:
    """
    Attributes:
        apportioned (Union[Unset, bool]): <code>true</code> when the promotion's reward amount is divided and allocated
            proportionally to multiple order lines.<br><code>false</code> when the entire reward amount is allocated to one
            order line, or when the same discount percentage is applied to several order lines (one-step percentage off
            promotions).
        campaign (Union[Unset, OR11Response200OrdersPromotionsAppliedPromotionsCampaign]):
        configuration (Union[Unset, OR11Response200OrdersPromotionsAppliedPromotionsConfiguration]):
        deduced_amount (Union[Unset, float]): Promotion's amount for this line.
        id (Union[Unset, str]): Promotion's id, defined by the shop
        offered_quantity (Union[Unset, int]): The quantity of free items offered by the promotion for this line.
            <br/>Only applicable when promotion is of type <code>FREE_ITEMS</code>, null otherwise.
        promo_code (Union[Unset, str]): Promo code associated to the promotion
    """

    apportioned: Union[Unset, bool] = UNSET
    campaign: Union[Unset, "OR11Response200OrdersPromotionsAppliedPromotionsCampaign"] = UNSET
    configuration: Union[Unset, "OR11Response200OrdersPromotionsAppliedPromotionsConfiguration"] = UNSET
    deduced_amount: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    offered_quantity: Union[Unset, int] = UNSET
    promo_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apportioned = self.apportioned

        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        deduced_amount = self.deduced_amount

        id = self.id

        offered_quantity = self.offered_quantity

        promo_code = self.promo_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apportioned is not UNSET:
            field_dict["apportioned"] = apportioned
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if deduced_amount is not UNSET:
            field_dict["deduced_amount"] = deduced_amount
        if id is not UNSET:
            field_dict["id"] = id
        if offered_quantity is not UNSET:
            field_dict["offered_quantity"] = offered_quantity
        if promo_code is not UNSET:
            field_dict["promo_code"] = promo_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.or11_response_200_orders_promotions_applied_promotions_campaign import (
            OR11Response200OrdersPromotionsAppliedPromotionsCampaign,
        )
        from ..models.or11_response_200_orders_promotions_applied_promotions_configuration import (
            OR11Response200OrdersPromotionsAppliedPromotionsConfiguration,
        )

        d = dict(src_dict)
        apportioned = d.pop("apportioned", UNSET)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, OR11Response200OrdersPromotionsAppliedPromotionsCampaign]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = OR11Response200OrdersPromotionsAppliedPromotionsCampaign.from_dict(_campaign)

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, OR11Response200OrdersPromotionsAppliedPromotionsConfiguration]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = OR11Response200OrdersPromotionsAppliedPromotionsConfiguration.from_dict(_configuration)

        deduced_amount = d.pop("deduced_amount", UNSET)

        id = d.pop("id", UNSET)

        offered_quantity = d.pop("offered_quantity", UNSET)

        promo_code = d.pop("promo_code", UNSET)

        or11_response_200_orders_promotions_applied_promotions = cls(
            apportioned=apportioned,
            campaign=campaign,
            configuration=configuration,
            deduced_amount=deduced_amount,
            id=id,
            offered_quantity=offered_quantity,
            promo_code=promo_code,
        )

        or11_response_200_orders_promotions_applied_promotions.additional_properties = d
        return or11_response_200_orders_promotions_applied_promotions

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
