%global pypi_name pyjokes
%global with_tests 0
%global global_desc One line jokes for programmers (jokes as a service)

Name:           %{pypi_name}
Version:        0.5.0
Release:        17%{?dist}
Summary:        %{global_desc}

License:        BSD
URL:            http://pyjok.es/
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif


%description
%{global_desc}.

%package     -n python3-%{pypi_name}
Summary: %{global_desc}. This package includes a commandline interface.

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{global_desc}.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENCE.txt
%doc docs/*
# For noarch packages: sitelib
%{_bindir}/pyjoke*
%{python3_sitelib}/pyjokes-*
%{python3_sitelib}/pyjokes/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Paul Whalen <pwhalen@fedoraproject.org> - 0.5.0-10
- Python 2 Package Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-7
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Lumír Balhar <lbalhar@redhat.com> - 0.5.0-5
- Fix directory ownership

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Paul Whalen <pwhalen@redhat.com> - 0.5.0-3
- Fix python2-pyjokes requires both Python 2 and Python 3(BZ#1448514)

* Fri Mar 03 2017 Paul Whalen <pwhalen@redhat.com> - 0.5.0-2
- Add %%python_provide macro.
- Consistently use %%pypi_name macro.
- Add global decription macro.

* Fri Feb 24 2017 Paul Whalen <pwhalen@redhat.com> 0.5.0-1
- Initial packaging.
