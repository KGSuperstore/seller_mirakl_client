from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p42_response_200_conversion_options_ai_enrichment import P42Response200ConversionOptionsAiEnrichment
    from ..models.p42_response_200_conversion_options_ai_rewrite import P42Response200ConversionOptionsAiRewrite


T = TypeVar("T", bound="P42Response200ConversionOptions")


@_attrs_define
class P42Response200ConversionOptions:
    """
    Attributes:
        ai_enrichment (Union[Unset, P42Response200ConversionOptionsAiEnrichment]):
        ai_rewrite (Union[Unset, P42Response200ConversionOptionsAiRewrite]):
    """

    ai_enrichment: Union[Unset, "P42Response200ConversionOptionsAiEnrichment"] = UNSET
    ai_rewrite: Union[Unset, "P42Response200ConversionOptionsAiRewrite"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ai_enrichment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ai_enrichment, Unset):
            ai_enrichment = self.ai_enrichment.to_dict()

        ai_rewrite: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ai_rewrite, Unset):
            ai_rewrite = self.ai_rewrite.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ai_enrichment is not UNSET:
            field_dict["ai_enrichment"] = ai_enrichment
        if ai_rewrite is not UNSET:
            field_dict["ai_rewrite"] = ai_rewrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p42_response_200_conversion_options_ai_enrichment import (
            P42Response200ConversionOptionsAiEnrichment,
        )
        from ..models.p42_response_200_conversion_options_ai_rewrite import P42Response200ConversionOptionsAiRewrite

        d = dict(src_dict)
        _ai_enrichment = d.pop("ai_enrichment", UNSET)
        ai_enrichment: Union[Unset, P42Response200ConversionOptionsAiEnrichment]
        if isinstance(_ai_enrichment, Unset):
            ai_enrichment = UNSET
        else:
            ai_enrichment = P42Response200ConversionOptionsAiEnrichment.from_dict(_ai_enrichment)

        _ai_rewrite = d.pop("ai_rewrite", UNSET)
        ai_rewrite: Union[Unset, P42Response200ConversionOptionsAiRewrite]
        if isinstance(_ai_rewrite, Unset):
            ai_rewrite = UNSET
        else:
            ai_rewrite = P42Response200ConversionOptionsAiRewrite.from_dict(_ai_rewrite)

        p42_response_200_conversion_options = cls(
            ai_enrichment=ai_enrichment,
            ai_rewrite=ai_rewrite,
        )

        p42_response_200_conversion_options.additional_properties = d
        return p42_response_200_conversion_options

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
