import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pr01_response_200_promotions_application_to_cart import PR01Response200PromotionsApplicationToCart
    from ..models.pr01_response_200_promotions_campaign import PR01Response200PromotionsCampaign
    from ..models.pr01_response_200_promotions_channels import PR01Response200PromotionsChannels
    from ..models.pr01_response_200_promotions_medias import PR01Response200PromotionsMedias
    from ..models.pr01_response_200_promotions_public_descriptions import PR01Response200PromotionsPublicDescriptions
    from ..models.pr01_response_200_promotions_triggers import PR01Response200PromotionsTriggers


T = TypeVar("T", bound="PR01Response200Promotions")


@_attrs_define
class PR01Response200Promotions:
    """
    Attributes:
        amount_off (Union[Unset, float]): The amount off of the promotion. <br/>Only applicable when promotion is of
            type <code>AMOUNT_OFF</code>, null otherwise
        application_to_cart (Union[Unset, list['PR01Response200PromotionsApplicationToCart']]): If applicable, returns
            promo code associated to the promotion
        campaign (Union[Unset, PR01Response200PromotionsCampaign]):
        channels (Union[Unset, list['PR01Response200PromotionsChannels']]): Channels on which the promotion is applied.
            If none, promotion applied on all channels
        customer_group_ids (Union[Unset, list[str]]): The customer groups on which the promotion is applied. If none,
            promotion applies to all customer groups.
        customer_organization_ids (Union[Unset, list[str]]): The customer organizations on which the promotion is
            applied. If none, promotion applies to all customer organizations.
        date_created (Union[Unset, datetime.datetime]): Creation date of the promotion
        end_date (Union[Unset, datetime.datetime]): End date of the promotion period of activity
        free_items_quantity (Union[Unset, int]): The free item target quantity of the promotion. <br/>Only applicable
            when promotion is of type <code>FREE_ITEMS</code>, null otherwise
        internal_description (Union[Unset, str]): Internal description of the promotion, set by the shop
        internal_id (Union[Unset, str]): Promotion identifier
        last_updated (Union[Unset, datetime.datetime]): Last update date of the promotion
        max_quantity_to_discount (Union[Unset, int]): Maximum quantity of items on which a percentage off discount
            applies. Only applicable when promotion is of type PERCENTAGE_OFF, null otherwise
        medias (Union[Unset, list['PR01Response200PromotionsMedias']]): The medias associated with this promotion, with
            the locales they apply to
        percentage_off (Union[Unset, float]): The percentage off of the promotion. <br/>Only applicable when promotion
            is of type <code>PERCENTAGE_OFF</code>, null otherwise
        public_descriptions (Union[Unset, list['PR01Response200PromotionsPublicDescriptions']]): The public descriptions
            of the promotion, with the locales they apply to
        reduced_unit_price (Union[Unset, float]): The new offer’s unit price triggered by the promotion. <br/>Only
            applicable when promotion is of type <code>REDUCED_UNIT_PRICE</code>, null otherwise.
        reward_offer_ids (Union[Unset, list[int]]): Offers used as reward in the promotion, according to the requested
            reward_offer_ids
        reward_on_purchased_items (Union[Unset, bool]): Specifies if the promotion's reward applies to purchased items
            or to a specific selection
        start_date (Union[Unset, datetime.datetime]): Start date of the promotion period of activity
        state (Union[Unset, str]): Promotion state
        trigger_offer_ids (Union[Unset, list[int]]): Offers which trigger the promotion, according to the requested
            trigger_offer_ids
        triggers (Union[Unset, list['PR01Response200PromotionsTriggers']]): Triggers of the promotion
        type_ (Union[Unset, str]): Promotion type
    """

    amount_off: Union[Unset, float] = UNSET
    application_to_cart: Union[Unset, list["PR01Response200PromotionsApplicationToCart"]] = UNSET
    campaign: Union[Unset, "PR01Response200PromotionsCampaign"] = UNSET
    channels: Union[Unset, list["PR01Response200PromotionsChannels"]] = UNSET
    customer_group_ids: Union[Unset, list[str]] = UNSET
    customer_organization_ids: Union[Unset, list[str]] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    free_items_quantity: Union[Unset, int] = UNSET
    internal_description: Union[Unset, str] = UNSET
    internal_id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    max_quantity_to_discount: Union[Unset, int] = UNSET
    medias: Union[Unset, list["PR01Response200PromotionsMedias"]] = UNSET
    percentage_off: Union[Unset, float] = UNSET
    public_descriptions: Union[Unset, list["PR01Response200PromotionsPublicDescriptions"]] = UNSET
    reduced_unit_price: Union[Unset, float] = UNSET
    reward_offer_ids: Union[Unset, list[int]] = UNSET
    reward_on_purchased_items: Union[Unset, bool] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, str] = UNSET
    trigger_offer_ids: Union[Unset, list[int]] = UNSET
    triggers: Union[Unset, list["PR01Response200PromotionsTriggers"]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_off = self.amount_off

        application_to_cart: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.application_to_cart, Unset):
            application_to_cart = []
            for application_to_cart_item_data in self.application_to_cart:
                application_to_cart_item = application_to_cart_item_data.to_dict()
                application_to_cart.append(application_to_cart_item)

        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        customer_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.customer_group_ids, Unset):
            customer_group_ids = self.customer_group_ids

        customer_organization_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.customer_organization_ids, Unset):
            customer_organization_ids = self.customer_organization_ids

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        free_items_quantity = self.free_items_quantity

        internal_description = self.internal_description

        internal_id = self.internal_id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        max_quantity_to_discount = self.max_quantity_to_discount

        medias: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.medias, Unset):
            medias = []
            for medias_item_data in self.medias:
                medias_item = medias_item_data.to_dict()
                medias.append(medias_item)

        percentage_off = self.percentage_off

        public_descriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.public_descriptions, Unset):
            public_descriptions = []
            for public_descriptions_item_data in self.public_descriptions:
                public_descriptions_item = public_descriptions_item_data.to_dict()
                public_descriptions.append(public_descriptions_item)

        reduced_unit_price = self.reduced_unit_price

        reward_offer_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.reward_offer_ids, Unset):
            reward_offer_ids = self.reward_offer_ids

        reward_on_purchased_items = self.reward_on_purchased_items

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        state = self.state

        trigger_offer_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.trigger_offer_ids, Unset):
            trigger_offer_ids = self.trigger_offer_ids

        triggers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item = triggers_item_data.to_dict()
                triggers.append(triggers_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_off is not UNSET:
            field_dict["amount_off"] = amount_off
        if application_to_cart is not UNSET:
            field_dict["application_to_cart"] = application_to_cart
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if channels is not UNSET:
            field_dict["channels"] = channels
        if customer_group_ids is not UNSET:
            field_dict["customer_group_ids"] = customer_group_ids
        if customer_organization_ids is not UNSET:
            field_dict["customer_organization_ids"] = customer_organization_ids
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if free_items_quantity is not UNSET:
            field_dict["free_items_quantity"] = free_items_quantity
        if internal_description is not UNSET:
            field_dict["internal_description"] = internal_description
        if internal_id is not UNSET:
            field_dict["internal_id"] = internal_id
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if max_quantity_to_discount is not UNSET:
            field_dict["max_quantity_to_discount"] = max_quantity_to_discount
        if medias is not UNSET:
            field_dict["medias"] = medias
        if percentage_off is not UNSET:
            field_dict["percentage_off"] = percentage_off
        if public_descriptions is not UNSET:
            field_dict["public_descriptions"] = public_descriptions
        if reduced_unit_price is not UNSET:
            field_dict["reduced_unit_price"] = reduced_unit_price
        if reward_offer_ids is not UNSET:
            field_dict["reward_offer_ids"] = reward_offer_ids
        if reward_on_purchased_items is not UNSET:
            field_dict["reward_on_purchased_items"] = reward_on_purchased_items
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if state is not UNSET:
            field_dict["state"] = state
        if trigger_offer_ids is not UNSET:
            field_dict["trigger_offer_ids"] = trigger_offer_ids
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pr01_response_200_promotions_application_to_cart import PR01Response200PromotionsApplicationToCart
        from ..models.pr01_response_200_promotions_campaign import PR01Response200PromotionsCampaign
        from ..models.pr01_response_200_promotions_channels import PR01Response200PromotionsChannels
        from ..models.pr01_response_200_promotions_medias import PR01Response200PromotionsMedias
        from ..models.pr01_response_200_promotions_public_descriptions import (
            PR01Response200PromotionsPublicDescriptions,
        )
        from ..models.pr01_response_200_promotions_triggers import PR01Response200PromotionsTriggers

        d = dict(src_dict)
        amount_off = d.pop("amount_off", UNSET)

        application_to_cart = []
        _application_to_cart = d.pop("application_to_cart", UNSET)
        for application_to_cart_item_data in _application_to_cart or []:
            application_to_cart_item = PR01Response200PromotionsApplicationToCart.from_dict(
                application_to_cart_item_data
            )

            application_to_cart.append(application_to_cart_item)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, PR01Response200PromotionsCampaign]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = PR01Response200PromotionsCampaign.from_dict(_campaign)

        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = PR01Response200PromotionsChannels.from_dict(channels_item_data)

            channels.append(channels_item)

        customer_group_ids = cast(list[str], d.pop("customer_group_ids", UNSET))

        customer_organization_ids = cast(list[str], d.pop("customer_organization_ids", UNSET))

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        free_items_quantity = d.pop("free_items_quantity", UNSET)

        internal_description = d.pop("internal_description", UNSET)

        internal_id = d.pop("internal_id", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        max_quantity_to_discount = d.pop("max_quantity_to_discount", UNSET)

        medias = []
        _medias = d.pop("medias", UNSET)
        for medias_item_data in _medias or []:
            medias_item = PR01Response200PromotionsMedias.from_dict(medias_item_data)

            medias.append(medias_item)

        percentage_off = d.pop("percentage_off", UNSET)

        public_descriptions = []
        _public_descriptions = d.pop("public_descriptions", UNSET)
        for public_descriptions_item_data in _public_descriptions or []:
            public_descriptions_item = PR01Response200PromotionsPublicDescriptions.from_dict(
                public_descriptions_item_data
            )

            public_descriptions.append(public_descriptions_item)

        reduced_unit_price = d.pop("reduced_unit_price", UNSET)

        reward_offer_ids = cast(list[int], d.pop("reward_offer_ids", UNSET))

        reward_on_purchased_items = d.pop("reward_on_purchased_items", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        state = d.pop("state", UNSET)

        trigger_offer_ids = cast(list[int], d.pop("trigger_offer_ids", UNSET))

        triggers = []
        _triggers = d.pop("triggers", UNSET)
        for triggers_item_data in _triggers or []:
            triggers_item = PR01Response200PromotionsTriggers.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        type_ = d.pop("type", UNSET)

        pr01_response_200_promotions = cls(
            amount_off=amount_off,
            application_to_cart=application_to_cart,
            campaign=campaign,
            channels=channels,
            customer_group_ids=customer_group_ids,
            customer_organization_ids=customer_organization_ids,
            date_created=date_created,
            end_date=end_date,
            free_items_quantity=free_items_quantity,
            internal_description=internal_description,
            internal_id=internal_id,
            last_updated=last_updated,
            max_quantity_to_discount=max_quantity_to_discount,
            medias=medias,
            percentage_off=percentage_off,
            public_descriptions=public_descriptions,
            reduced_unit_price=reduced_unit_price,
            reward_offer_ids=reward_offer_ids,
            reward_on_purchased_items=reward_on_purchased_items,
            start_date=start_date,
            state=state,
            trigger_offer_ids=trigger_offer_ids,
            triggers=triggers,
            type_=type_,
        )

        pr01_response_200_promotions.additional_properties = d
        return pr01_response_200_promotions

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
