from typing import TYPE_CHECKING

from nomad.config import config
from nomad.parsing.parser import MatchingParser

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

configuration = config.get_plugin_entry_point(
    'nomad_plugin_test.parsers:parser_entry_point'
)

from nomad.datamodel.datamodel import EntryArchive

class NewParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger: "BoundLogger",
    ) -> None:
        logger.info("MyParser is working!")

        
