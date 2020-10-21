%global pypi_name rows

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        9%{?dist}
Summary:        A common, beautiful interface to tabular data, no matter the format

License:        GPLv3+
URL:            https://github.com/turicas/rows
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# Required for tests: https://github.com/turicas/rows/issues/193
BuildRequires:  glibc-langpack-pt

%description
No matter in which format your tabular data is: rows will import it,
automatically detect types and give you high-level Python objects so
you can start working with the data instead of trying to parse it. It
is also locale-and-unicode aware.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-six
BuildRequires:  python3-psycopg2
BuildRequires:  python3-tqdm
BuildRequires:  python3-cached-property
BuildRequires:  python3-PyMuPDF
BuildRequires:  python3-pdfminer
BuildRequires:  python3-requests
BuildRequires:  python3-click
BuildRequires:  python3-unicodecsv
BuildRequires:  python3-openpyxl
BuildRequires:  python3-lxml
BuildRequires:  python3-xlrd
BuildRequires:  python3-xlwt
Recommends:     python3-xlrd
Recommends:     python3-xlwt
Recommends:     python3-magic
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
No matter in which format your tabular data is: rows will import it,
automatically detect types and give you high-level Python objects so
you can start working with the data instead of trying to parse it. It
is also locale-and-unicode aware.

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tool for tabular formatter.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i 's/\"pathlib\"//g' setup.py

%build
%py3_build

%install
%py3_install
install -Dpm 0644 %{pypi_name}.1.txt %{buildroot}%{_mandir}/man1/%{pypi_name}.1

%check
EXCLUDE_ARG=""
# We don't package xlsx and parquet things yet
EXCLUDE_ARG="$EXCLUDE_ARG -e tests_plugin_parquet -e tests_plugin_xlsx"
# AssertionError: 'ISO-8859-8' != u'iso-8859-1'
# https://github.com/turicas/rows/issues/194
EXCLUDE_ARG="$EXCLUDE_ARG -e test_local_file_sample_size"
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 293: ordinal not in range(128)
# https://github.com/turicas/rows/issues/195
EXCLUDE_ARG="$EXCLUDE_ARG -e tests_plugin_json"
# Don't test postgreSQL
EXCLUDE_ARG="$EXCLUDE_ARG -e tests_plugin_postgresql"
# FAIL: rows.Table.add should be constant time
# https://github.com/turicas/rows/issues/283
EXCLUDE_ARG="$EXCLUDE_ARG -e test_table_add_time"

%files -n python3-%{pypi_name}
%doc AUTHORS.md README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%files -n %{pypi_name}
%doc AUTHORS.md README.md
%license LICENSE
%{_mandir}/man1/%{pypi_name}.1*
%{_bindir}/%{pypi_name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-6
- Fix install issue (rhbz#1770853)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-2
- Rework check section and enable tests
- Move CLI tool to sub-package

* Sun Feb 24 2019 William Moreno Reyes <williamjmorenor@gmail.com> - 0.4.1-1
- Update to v0.4.1 (rhbz#1674171)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.3.1-8
- Remove python2 subpackage (rhbz#1630832)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.3.1-6
- Disable failing test

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 William Moreno <williamjmorenor@gmail.com> - 0.3.1-1
- Update to 0.3.1 upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuild for Python 3.6

* Mon Sep 05 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-2
- Run locale-specific tests

* Sat Sep 03 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Update to 0.3.0
- Add python3 subpackage
- Other fixes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 28 2015 Fedora <williamjmorenor@gmail.com> - 0.1.1-1
- Initial Packaging
