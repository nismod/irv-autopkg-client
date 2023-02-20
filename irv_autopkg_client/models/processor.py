from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.processor_version import ProcessorVersion


T = TypeVar("T", bound="Processor")


@attr.s(auto_attribs=True)
class Processor:
    """Summary information about a Processor

    Attributes:
        name (str):
        versions (List['ProcessorVersion']):
    """

    name: str
    versions: List["ProcessorVersion"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()

            versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.processor_version import ProcessorVersion

        d = src_dict.copy()
        name = d.pop("name")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = ProcessorVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        processor = cls(
            name=name,
            versions=versions,
        )

        processor.additional_properties = d
        return processor

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
