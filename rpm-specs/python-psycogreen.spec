%global pypi_name psycogreen

%global common_desc \
The psycogreen package enables psycopg2 to work with co-routine libraries,	\
using asynchronous calls internally but offering a blocking interface so	\
that regular code can run unmodified.  Psycopg offers co-routines support	\
since release 2.2.  Because the main module is a C extension it cannot be	\
monkey-patched to become co-routine-friendly.  Instead it exposes a hook	\
that co-routine libraries can use to install a function integrating with	\
their event scheduler.  Psycopg will call the function whenever it		\
executes a libpq call that may block.  Psycogreen is a collection of “wait	\
callbacks” useful to integrate Psycopg with different co-routine libraries.


Name:		python-%{pypi_name}
Version:	1.0.2
Release:	2%{?dist}
Summary:	Psycopg2 integration with co-routine libraries

License:	BSD
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

Requires:	python3-eventlet
Requires:	python3-gevent
Requires:	python3-psycopg2

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license COPYING
%doc PKG-INFO README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.9

* Sun Feb 23 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.2-1
- New upstream release (#1806198)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuild for Python 3.6

* Tue Sep 27 2016 Björn Esser <fedora@besser82.io> - 1.0-1
- Initial import (rhbz 1379421)

* Tue Sep 27 2016 Björn Esser <fedora@besser82.io> - 1.0-0.2
- Updated with suggestions from:
  https://bugzilla.redhat.com/show_bug.cgi?id=1379421#c1
- Enabled Python 3

* Sun Sep 25 2016 Björn Esser <fedora@besser82.io> - 1.0-0.1
- Initial package (rhbz 1379421)
