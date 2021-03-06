#!/usr/bin/env python
"""AFF4 objects for managing Rekall responses."""

from grr.lib import rdfvalue
from grr.lib.aff4_objects import collections


class RekallResponseCollection(collections.RDFValueCollection):
  """A collection of Rekall results."""
  _rdf_type = rdfvalue.RekallResponse

  renderer = "GRRRekallRenderer"

