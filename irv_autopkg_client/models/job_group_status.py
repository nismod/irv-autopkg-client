from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_status import JobStatus


T = TypeVar("T", bound="JobGroupStatus")


@attr.s(auto_attribs=True)
class JobGroupStatus:
    """Status of the Processor Group in a submited DAG

    Attributes:
        job_group_status (str):
        job_group_processors (List['JobStatus']):
        job_group_percent_complete (Union[Unset, int]):
    """

    job_group_status: str
    job_group_processors: List["JobStatus"]
    job_group_percent_complete: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_group_status = self.job_group_status
        job_group_processors = []
        for job_group_processors_item_data in self.job_group_processors:
            job_group_processors_item = job_group_processors_item_data.to_dict()

            job_group_processors.append(job_group_processors_item)

        job_group_percent_complete = self.job_group_percent_complete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_group_status": job_group_status,
                "job_group_processors": job_group_processors,
            }
        )
        if job_group_percent_complete is not UNSET:
            field_dict["job_group_percent_complete"] = job_group_percent_complete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_status import JobStatus

        d = src_dict.copy()
        job_group_status = d.pop("job_group_status")

        job_group_processors = []
        _job_group_processors = d.pop("job_group_processors")
        for job_group_processors_item_data in _job_group_processors:
            job_group_processors_item = JobStatus.from_dict(job_group_processors_item_data)

            job_group_processors.append(job_group_processors_item)

        job_group_percent_complete = d.pop("job_group_percent_complete", UNSET)

        job_group_status = cls(
            job_group_status=job_group_status,
            job_group_processors=job_group_processors,
            job_group_percent_complete=job_group_percent_complete,
        )

        job_group_status.additional_properties = d
        return job_group_status

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
