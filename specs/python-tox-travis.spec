%global pypiname tox-travis
%global module tox_travis

%define version 0.11

Name:       python-%{pypiname}
Version:    0.11
Release:    1
Summary:    Seamless integration of Tox into Travis CI
License:    MIT
URL:        https://github.com/tox-dev/tox-travis
Source0:    https://github.com/tox-dev/%{pypiname}/archive/%{version}/%{pypiname}-%{version}.tar.gz
Group:      Development/Libraries
BuildArch:  noarch
Vendor:     Ryan Hiebert <ryan@ryanhiebert.com>

%description
====================================
tox-travis: Integrate tox and Travis
====================================

.. image:: https://img.shields.io/pypi/v/tox-travis.svg
   :target: https://pypi.org/project/tox-travis/
   :alt: Latest Version

.. image:: https://readthedocs.org/projects/tox-travis/badge/?version=stable
   :target: https://tox-travis.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://travis-ci.org/tox-dev/tox-travis.svg?branch=master
   :target: https://travis-ci.org/tox-dev/tox-travis

.. image:: https://codecov.io/gh/tox-dev/tox-travis/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/tox-dev/tox-travis

.. image:: https://badges.gitter.im/tox-dev/tox-travis.svg
   :alt: Join the chat at https://gitter.im/tox-dev/tox-travis
   :target: https://gitter.im/tox-dev/tox-travis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

tox-travis is a plugin for `tox <https://pypi.org/project/tox/>`_ that simplifies the setup
between tox and Travis.

Usage
=====

Configure the Python versions to test with in ``.travis.yml``,
and install ``tox-travis`` with pip:

.. code-block:: yaml

    sudo: false
    language: python
    python:
      - "2.7"
      - "3.4"
    install: pip install tox-travis
    script: tox

tox will only run the ``py27`` or ``py34`` env
(or envs that have a factor that matches)
as appropriate for the version of Python
that is being run by each Travis job.

%package -n python3-%{pypiname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypiname}}
Provides:       %{pypiname} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_enable_dependency_generator}

%description -n python3-%{pypiname}
====================================
tox-travis: Integrate tox and Travis
====================================

.. image:: https://img.shields.io/pypi/v/tox-travis.svg
   :target: https://pypi.org/project/tox-travis/
   :alt: Latest Version

.. image:: https://readthedocs.org/projects/tox-travis/badge/?version=stable
   :target: https://tox-travis.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://travis-ci.org/tox-dev/tox-travis.svg?branch=master
   :target: https://travis-ci.org/tox-dev/tox-travis

.. image:: https://codecov.io/gh/tox-dev/tox-travis/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/tox-dev/tox-travis

.. image:: https://badges.gitter.im/tox-dev/tox-travis.svg
   :alt: Join the chat at https://gitter.im/tox-dev/tox-travis
   :target: https://gitter.im/tox-dev/tox-travis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

tox-travis is a plugin for `tox <https://pypi.org/project/tox/>`_ that simplifies the setup
between tox and Travis.

Usage
=====

Configure the Python versions to test with in ``.travis.yml``,
and install ``tox-travis`` with pip:

.. code-block:: yaml

    sudo: false
    language: python
    python:
      - "2.7"
      - "3.4"
    install: pip install tox-travis
    script: tox

tox will only run the ``py27`` or ``py34`` env
(or envs that have a factor that matches)
as appropriate for the version of Python
that is being run by each Travis job.

%prep
%autosetup -n %{pypiname}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{pypiname}
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
