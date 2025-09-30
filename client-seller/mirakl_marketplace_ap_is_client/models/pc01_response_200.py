from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pc01_response_200_features import PC01Response200Features
    from ..models.pc01_response_200_modules import PC01Response200Modules
    from ..models.pc01_response_200_platform_configuration import PC01Response200PlatformConfiguration


T = TypeVar("T", bound="PC01Response200")


@_attrs_define
class PC01Response200:
    """
    Attributes:
        features (Union[Unset, PC01Response200Features]):
        modules (Union[Unset, PC01Response200Modules]):
        platform_configuration (Union[Unset, PC01Response200PlatformConfiguration]):
        platform_name (Union[Unset, str]): Operator platform name
        tenant_name (Union[Unset, str]): Tenant platform name
        timezone (Union[Unset, str]): Platform timezone
    """

    features: Union[Unset, "PC01Response200Features"] = UNSET
    modules: Union[Unset, "PC01Response200Modules"] = UNSET
    platform_configuration: Union[Unset, "PC01Response200PlatformConfiguration"] = UNSET
    platform_name: Union[Unset, str] = UNSET
    tenant_name: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        modules: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules.to_dict()

        platform_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.platform_configuration, Unset):
            platform_configuration = self.platform_configuration.to_dict()

        platform_name = self.platform_name

        tenant_name = self.tenant_name

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if features is not UNSET:
            field_dict["features"] = features
        if modules is not UNSET:
            field_dict["modules"] = modules
        if platform_configuration is not UNSET:
            field_dict["platform_configuration"] = platform_configuration
        if platform_name is not UNSET:
            field_dict["platform_name"] = platform_name
        if tenant_name is not UNSET:
            field_dict["tenant_name"] = tenant_name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pc01_response_200_features import PC01Response200Features
        from ..models.pc01_response_200_modules import PC01Response200Modules
        from ..models.pc01_response_200_platform_configuration import PC01Response200PlatformConfiguration

        d = dict(src_dict)
        _features = d.pop("features", UNSET)
        features: Union[Unset, PC01Response200Features]
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = PC01Response200Features.from_dict(_features)

        _modules = d.pop("modules", UNSET)
        modules: Union[Unset, PC01Response200Modules]
        if isinstance(_modules, Unset):
            modules = UNSET
        else:
            modules = PC01Response200Modules.from_dict(_modules)

        _platform_configuration = d.pop("platform_configuration", UNSET)
        platform_configuration: Union[Unset, PC01Response200PlatformConfiguration]
        if isinstance(_platform_configuration, Unset):
            platform_configuration = UNSET
        else:
            platform_configuration = PC01Response200PlatformConfiguration.from_dict(_platform_configuration)

        platform_name = d.pop("platform_name", UNSET)

        tenant_name = d.pop("tenant_name", UNSET)

        timezone = d.pop("timezone", UNSET)

        pc01_response_200 = cls(
            features=features,
            modules=modules,
            platform_configuration=platform_configuration,
            platform_name=platform_name,
            tenant_name=tenant_name,
            timezone=timezone,
        )

        pc01_response_200.additional_properties = d
        return pc01_response_200

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
