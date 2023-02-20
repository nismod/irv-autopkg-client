from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processor_metadata import ProcessorMetadata


T = TypeVar("T", bound="ProcessorVersion")


@attr.s(auto_attribs=True)
class ProcessorVersion:
    """A Version of a Processor

    Attributes:
        version (str):
        processor (ProcessorMetadata): Detail about a Data Processor
        uri (Union[Unset, str]):  Default: ''.
    """

    version: str
    processor: "ProcessorMetadata"
    uri: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        processor = self.processor.to_dict()

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "processor": processor,
            }
        )
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.processor_metadata import ProcessorMetadata

        d = src_dict.copy()
        version = d.pop("version")

        processor = ProcessorMetadata.from_dict(d.pop("processor"))

        uri = d.pop("uri", UNSET)

        processor_version = cls(
            version=version,
            processor=processor,
            uri=uri,
        )

        processor_version.additional_properties = d
        return processor_version

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
