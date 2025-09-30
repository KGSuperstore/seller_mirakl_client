from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pc01_response_200_modules_tax_manager import PC01Response200ModulesTaxManager


T = TypeVar("T", bound="PC01Response200Modules")


@_attrs_define
class PC01Response200Modules:
    """
    Attributes:
        mirakl_catalog_integrator (Union[Unset, bool]): Mirakl Catalog integrator activated. Allows operator to manage
            catalog structure into Mirakl.
        mirakl_catalog_manager (Union[Unset, bool]): Mirakl Catalog Manager activated. Allows operator to remove the
            complexity of integrating catalogs from multiple sources.
        mirakl_catalog_transformer (Union[Unset, bool]): Mirakl Catalog Transformer activated.
        mirakl_platform_services (Union[Unset, bool]): Mirakl Platform for Services activated. Specific module for
            services management: separated from the product management module.
        offer_management (Union[Unset, bool]): Offer management available on the platform
        offer_management_mode (Union[Unset, str]): Offer management mode on the platform: SIMPLE: All shops can push
            offers. HYBRID: The operator decides whether a shop can push offers on the platform.
        order_management (Union[Unset, bool]): Order management available on the platform
        order_management_mode (Union[Unset, str]): Order management mode on the platform: SIMPLE: All shops can process
            orders. HYBRID: The operator decides whether a shop can process orders on the platform.
        promotions (Union[Unset, bool]): Promotion module activated
        quotes (Union[Unset, bool]): Quote module activated
        tax_manager (Union[Unset, PC01Response200ModulesTaxManager]):
    """

    mirakl_catalog_integrator: Union[Unset, bool] = UNSET
    mirakl_catalog_manager: Union[Unset, bool] = UNSET
    mirakl_catalog_transformer: Union[Unset, bool] = UNSET
    mirakl_platform_services: Union[Unset, bool] = UNSET
    offer_management: Union[Unset, bool] = UNSET
    offer_management_mode: Union[Unset, str] = UNSET
    order_management: Union[Unset, bool] = UNSET
    order_management_mode: Union[Unset, str] = UNSET
    promotions: Union[Unset, bool] = UNSET
    quotes: Union[Unset, bool] = UNSET
    tax_manager: Union[Unset, "PC01Response200ModulesTaxManager"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mirakl_catalog_integrator = self.mirakl_catalog_integrator

        mirakl_catalog_manager = self.mirakl_catalog_manager

        mirakl_catalog_transformer = self.mirakl_catalog_transformer

        mirakl_platform_services = self.mirakl_platform_services

        offer_management = self.offer_management

        offer_management_mode = self.offer_management_mode

        order_management = self.order_management

        order_management_mode = self.order_management_mode

        promotions = self.promotions

        quotes = self.quotes

        tax_manager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_manager, Unset):
            tax_manager = self.tax_manager.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mirakl_catalog_integrator is not UNSET:
            field_dict["mirakl_catalog_integrator"] = mirakl_catalog_integrator
        if mirakl_catalog_manager is not UNSET:
            field_dict["mirakl_catalog_manager"] = mirakl_catalog_manager
        if mirakl_catalog_transformer is not UNSET:
            field_dict["mirakl_catalog_transformer"] = mirakl_catalog_transformer
        if mirakl_platform_services is not UNSET:
            field_dict["mirakl_platform_services"] = mirakl_platform_services
        if offer_management is not UNSET:
            field_dict["offer_management"] = offer_management
        if offer_management_mode is not UNSET:
            field_dict["offer_management_mode"] = offer_management_mode
        if order_management is not UNSET:
            field_dict["order_management"] = order_management
        if order_management_mode is not UNSET:
            field_dict["order_management_mode"] = order_management_mode
        if promotions is not UNSET:
            field_dict["promotions"] = promotions
        if quotes is not UNSET:
            field_dict["quotes"] = quotes
        if tax_manager is not UNSET:
            field_dict["tax_manager"] = tax_manager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pc01_response_200_modules_tax_manager import PC01Response200ModulesTaxManager

        d = dict(src_dict)
        mirakl_catalog_integrator = d.pop("mirakl_catalog_integrator", UNSET)

        mirakl_catalog_manager = d.pop("mirakl_catalog_manager", UNSET)

        mirakl_catalog_transformer = d.pop("mirakl_catalog_transformer", UNSET)

        mirakl_platform_services = d.pop("mirakl_platform_services", UNSET)

        offer_management = d.pop("offer_management", UNSET)

        offer_management_mode = d.pop("offer_management_mode", UNSET)

        order_management = d.pop("order_management", UNSET)

        order_management_mode = d.pop("order_management_mode", UNSET)

        promotions = d.pop("promotions", UNSET)

        quotes = d.pop("quotes", UNSET)

        _tax_manager = d.pop("tax_manager", UNSET)
        tax_manager: Union[Unset, PC01Response200ModulesTaxManager]
        if isinstance(_tax_manager, Unset):
            tax_manager = UNSET
        else:
            tax_manager = PC01Response200ModulesTaxManager.from_dict(_tax_manager)

        pc01_response_200_modules = cls(
            mirakl_catalog_integrator=mirakl_catalog_integrator,
            mirakl_catalog_manager=mirakl_catalog_manager,
            mirakl_catalog_transformer=mirakl_catalog_transformer,
            mirakl_platform_services=mirakl_platform_services,
            offer_management=offer_management,
            offer_management_mode=offer_management_mode,
            order_management=order_management,
            order_management_mode=order_management_mode,
            promotions=promotions,
            quotes=quotes,
            tax_manager=tax_manager,
        )

        pc01_response_200_modules.additional_properties = d
        return pc01_response_200_modules

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
