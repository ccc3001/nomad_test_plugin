from typing import TYPE_CHECKING

from nomad.config import config
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.parser import MatchingParser

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

configuration = config.get_plugin_entry_point(
    'nomad_plugin_test.parsers:parser_entry_point'
)


class NewParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info("MyParser is working!")
        # archive.data = EntryData()
        # archive.data.comment = "test"
        logger.info('NewParser.parse', parameter=configuration.parameter)
        logger.warn("some warning")
        archive.workflow2 = Workflow(name='test')
