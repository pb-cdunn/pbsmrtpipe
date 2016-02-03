import logging
import os
import unittest

import pbcommand.mock as M
from pbcommand.models import FileTypes
from pbsmrtpipe.dataset_io import dispatch_metadata_resolver, DatasetMetadata

from base import get_data_file, get_temp_file

log = logging.getLogger(__name__)


class DatasetFastaTest(unittest.TestCase):

    FILE_NAME = 'small.fasta'
    NRECORDS = 111
    FILE_TYPE = FileTypes.FASTA

    def _write_mock_file(self, p):
        M.write_random_fasta_records(p, nrecords=self.NRECORDS)

    def test_01(self):
        p = get_temp_file(self.FILE_NAME)
        self._write_mock_file(p)
        ds_metadata = dispatch_metadata_resolver(self.FILE_TYPE, p)
        self.assertIsInstance(ds_metadata, DatasetMetadata)
        self.assertEquals(ds_metadata.nrecords, self.NRECORDS)


class DatasetFastqTest(DatasetFastaTest):
    FILE_NAME = 'small.fastq'
    NRECORDS = 77
    FILE_TYPE = FileTypes.FASTQ

    def _write_mock_file(self, p):
        M.write_random_fastq_records(p, nrecords=self.NRECORDS)


class DatasetFofnTest(unittest.TestCase):

    FILE_TYPE = FileTypes.FOFN

    def test_01(self):
        nrecords = 15
        name = "example_fofn"
        f = get_temp_file(name)
        _ = M.write_random_fofn(f, nrecords)
        ds_metadata = dispatch_metadata_resolver(self.FILE_TYPE, f)
        self.assertEquals(ds_metadata.nrecords, nrecords)
        os.remove(f)


class DatasetRegionFofnTest(DatasetFofnTest):
    FILE_TYPE = FileTypes.RGN_FOFN


class DatasetRegionMovieFofnTest(DatasetFofnTest):
    FILE_TYPE = FileTypes.MOVIE_FOFN
