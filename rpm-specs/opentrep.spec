#
%global mydocs __tmp_docdir

# Build -pythonN subpackage
%bcond_without python3

#
Name:           opentrep
Version:        0.07.7
Release:        4%{?dist}

Summary:        C++ library providing a clean API for parsing travel-focused requests

# The entire source code is LGPLv2+ except opentrep/basic/float_utils_google.hpp,
# which is BSD
License:        LGPLv2+ and BSD
URL:            https://github.com/trep/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  cmake
%else
BuildRequires:  cmake3
%endif
BuildRequires:  boost-devel
BuildRequires:  readline-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  xapian-core-devel
BuildRequires:  sqlite-devel
BuildRequires:  mysql-devel
BuildRequires:  libicu-devel
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-compiler

%description
%{name} aims at providing a clean API, and the corresponding C++
implementation, for parsing travel-focused requests.
It powers the https://transport-search.org Web site.

%{name} uses Xapian (https://www.xapian.org) for the Information Retrieval
part, on freely available travel-related data (e.g., country names and codes,
city names and codes, airline names and codes, etc.), mainly to be found in
the OpenTravelData project (https://github.com/opentraveldata/opentraveldata).

The data files are available from https://transport-search.org/data/optd/por/

%{name} exposes a simple, clean and object-oriented, API. For instance,
the OPENTREP::interpretTravelRequest() method takes, as input, a string
containing the travel request, and yields, as output, the list of the
recognized terms as well as their corresponding types.
As an example, the travel request
'Washington DC Beijing Monday a/r +AA -UA 1 week 2 adults 1 dog' would give
the following list:
 * Origin airport: Washington, DC, USA
 * Destination airport: Beijing, China
 * Date of travel: next Monday
 * Date of return: 1 week after next Monday
 * Preferred airline: American Airlines; non-preferred airline: United Airlines
 * Number of travelers: 2 adults and a dog

The output can then be used by other systems, for instance to book the
corresponding travel or to visualize it on a map and calendar and to
share it with others.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) and
SOCI (https://github.com/SOCI) libraries are used.

Note that %{name} currently only recognizes points of reference (POR),
as to be found in the following file: http://bit.ly/1DXIjWE
A good complementary tool is GeoBase
(https://opentraveldata.github.io/geobases), a Python-based software
able to access to any travel-related data source.

%package        devel
Summary:        Header files, libraries and development helper tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared libraries and
development helper tools for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%if %{with python3}

%package    -n python3-%{name}
Summary:    Python bindings for %{name}
Group:      System Environment/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  boost-python3-devel

%description -n python3-%{name}
This package contains Python libraries for %{name}

%endif

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
BuildRequires:  tex(latex), tex(sectsty.sty), tex(tocloft.sty), tex(xtab.sty)
#BuildRequires:  texlive-collection-langcyrillic, texlive-cyrillic
BuildRequires:  texlive-epstopdf
BuildRequires:  doxygen
BuildRequires:  ghostscript

%description    doc
This package contains HTML pages for %{name}. All that documentation
is generated thanks to Doxygen (https://doxygen.org). The content is
the same as what can be browsed online (https://opentrep.sourceforge.net).
Note that the PDF form of the reference manual is mainly available online
(https://opentrep.sourceforge.net/refman.pdf), as the one present in that
package is usually corrupted: it depends on the building conditions,
and it is therefore not reliable.

%prep
%setup -q -n %{name}-%{name}-%{version}


%build
mkdir tmpbuild
pushd tmpbuild
%if 0%{?fedora} || 0%{?rhel} > 7
%cmake ..
%else
%cmake3 ..
%endif

%make_build
popd

%install
pushd tmpbuild
%make_install
popd

# From rpm version > 4.9.1, it may no longer be necessary to move the
# documentation out of the docdir path, as the %%doc macro no longer
# deletes the full directory before installing files into it.
mkdir -p %{mydocs}
mv %{buildroot}%{_docdir}/%{name}/html %{mydocs}
rm -f %{mydocs}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%if %{with python3}
# (Pure) Python OpenTREP executable
chmod a-x %{buildroot}%{python3_sitearch}/py%{name}/Travel_pb2.py
%endif


#check
#ctest

%if 0%{?rhel} <= 7
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif

%if %{with python3}
%post -n python3-%{name}
ln -s -f %{python3_sitearch}/py%{name}/py%{name} %{_bindir}/py%{name}

%postun -n python3-%{name}
rm -f %{_bindir}/py%{name}
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/%{name}-indexer
%{_bindir}/%{name}-searcher
%{_bindir}/%{name}-dbmgr
%{_libdir}/lib%{name}.so.0.*
%{_mandir}/man1/%{name}-indexer.1.*
%{_mandir}/man1/%{name}-searcher.1.*
%{_mandir}/man1/%{name}-dbmgr.1.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%dir %{_datadir}/%{name}/data/por
%{_datadir}/%{name}/data/por/README.md
%{_datadir}/%{name}/data/por/create_trep_user_and_db.sql
%{_datadir}/%{name}/data/por/create_trep_tables_sqlite3.sql
%{_datadir}/%{name}/data/por/create_trep_tables_mysql.sql
%{_datadir}/%{name}/data/por/test_optd_por_public.csv
%{_datadir}/%{name}/data/por/test_optd_por_public_schema.sql
%{_datadir}/%{name}/data/por/test_world_schedule.csv

%files devel
%{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/%{name}/CMake
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{mydocs}/html
%license COPYING

%if %{with python3}
%files -n python3-%{name}
%{python3_sitearch}/py%{name}/
%{_mandir}/man1/py%{name}.1.*
%endif

%changelog
* Sun Jun 21 2020 Adrian Reber <adrian@lisas.de> - 0.07.7-4
- Rebuilt for protobuf 3.12

* Tue Jun 16 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.07.7-3
- Rebuilt for library dependency inconsistency

* Sun Jun 07 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.07.7-2
- Rebuilt for SOCI 4.0.1-alpha2

* Mon Jun 01 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.07.7-1
- Upstream update

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.07.4-7
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.07.4-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 0.07.4-4
- Rebuild for protobuf 3.11

* Sun Nov 24 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.07.4-3
- Fixed a few typos in Pythn dependencies

* Fri Nov 15 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.07.4-2
- Fixed the too long description line

* Mon Nov 11 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.07.4-1
- Upstream update to 0.07.4

