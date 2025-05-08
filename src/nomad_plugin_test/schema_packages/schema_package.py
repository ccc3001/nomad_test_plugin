from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, Package

# Load plugin configuration from pyproject.toml entry point
configuration = config.get_plugin_entry_point(
    'nomad_plugin_test.schema_packages:schema_package_entry_point'
)

# Define the metainfo package
m_package = Package(name='new_schema_package')


# Define your schema class
class NewSchemaPackage(Schema):
    m_def = m_package.m_schema()  # Register class with the package

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        logger.info('NewSchemaPackage.normalize', parameter=configuration.parameter)

        if self.name:
            self.message = f'Hello {self.name}!'
        else:
            self.message = "Hello, unnamed package!"
