from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_ import License


T = TypeVar("T", bound="ProcessorMetadata")


@attr.s(auto_attribs=True)
class ProcessorMetadata:
    """Detail about a Data Processor

    Attributes:
        name (str):
        description (str):
        dataset (str):
        author (str):
        license_ (License):
        origin_url (str):
        version (str):
        status (Union[Unset, str]):  Default: ''.
    """

    name: str
    description: str
    dataset: str
    author: str
    license_: "License"
    origin_url: str
    version: str
    status: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        dataset = self.dataset
        author = self.author
        license_ = self.license_.to_dict()

        origin_url = self.origin_url
        version = self.version
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "dataset": dataset,
                "author": author,
                "license": license_,
                "origin_url": origin_url,
                "version": version,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.license_ import License

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        dataset = d.pop("dataset")

        author = d.pop("author")

        license_ = License.from_dict(d.pop("license"))

        origin_url = d.pop("origin_url")

        version = d.pop("version")

        status = d.pop("status", UNSET)

        processor_metadata = cls(
            name=name,
            description=description,
            dataset=dataset,
            author=author,
            license_=license_,
            origin_url=origin_url,
            version=version,
            status=status,
        )

        processor_metadata.additional_properties = d
        return processor_metadata

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
