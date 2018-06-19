===
qng
===

**qng**, the Queb name generator.

Requirements
------------

To run **qng**, you will only need Python ≥ 3.6.

For installing, we recommend using the ``pip`` package manager.

Installing
----------

To install **qng** system-wide, run:

.. code-block:: sh

   sudo pip3 install qng

To install **qng** manually from source, the steps are as follows:

.. code-block:: sh

   git clone git@github.com:abusque/qng.git
   cd qng
   sudo ./setup.py install

Using
-----

Once installed, you can use **qng** by running the following command:

.. code-block:: sh

   qng


This will generate a single random Queb name.

You can also generate names for a specific gender:

.. code-block:: sh

   qng --gender male


Generate names according to their relative popularity:

.. code-block:: sh

   qng --weighted


Generate a name formatted as "snake_case" without any diacritics
(useful for naming your containers):

.. code-block:: sh

   qng --snake-case


All the above options may be combined if desired. Refer to the help
for more details:

.. code-block:: sh

   qng --help


Development
-----------

For local development of **qng**, you may use
`pipenv <https://docs.pipenv.org/>`_. Use ``pipenv install --dev`` to
generate a virtual environment into which the dependencies will be
installed. You may then use ``pipenv shell`` to activate that
environment.

For publishing releases to PyPI, we recommend using
`Twine <https://pypi.org/project/twine/>`_.

References
----------

The data for **qng** was sourced from `l'institut de la statistique`_
for surnames, and from `PrénomsQuébec.ca`_ for first names (who in
turn get their data from Retraite Québec's `banque de prénoms`_).

Scripts used for scraping the data from the web pages can be found
under the ``scripts/`` directory.

.. _l'institut de la statistique: http://www.stat.gouv.qc.ca/statistiques/population-demographie/caracteristiques/noms_famille_1000.htm
.. _PrénomsQuébec.ca: https://www.prenomsquebec.ca/
.. _banque de prénoms: https://www.rrq.gouv.qc.ca/fr/enfants/banque_prenoms/Pages/banque_prenoms.aspx