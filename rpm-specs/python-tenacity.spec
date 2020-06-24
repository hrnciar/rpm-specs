%{?python_enable_dependency_generator}
%global pypi_name tenacity
%global common_desc  Tenacity is a general purpose retrying library

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{pypi_name}
Version:        6.0.0
Release:        2%{?dist}
Summary:        %{common_desc}
License:        ASL 2.0
URL:            https://github.com/jd/%{pypi_name}
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        %{common_desc}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:    python2-setuptools
BuildRequires:    python2-setuptools_scm
BuildRequires:    python2-devel
BuildRequires:    python2-pbr
BuildRequires:    python2-six >= 1.9.0
BuildRequires:    python2-futures >= 3.0
BuildRequires:    python2-monotonic >= 0.6
BuildRequires:    python2-tornado >= 4.5
BuildRequires:    python2-pytest
%if %{undefined __pythondist_requires}
Requires:         python2-six >= 1.9.0
Requires:         python2-futures >= 3.0
Requires:         python2-monotonic >= 0.6
%endif


%description -n python2-%{pypi_name}
%{common_desc}
%endif

%if %{with python3}
%package -n python3-%{pypi_name}

Summary:          %{common_desc}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:    python3-setuptools
BuildRequires:    python3-setuptools_scm
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-six >= 1.9.0
BuildRequires:    python3-tornado >= 4.5
BuildRequires:    python3-pytest
%if %{undefined __pythondist_requires}
Requires:         python3-six >= 1.9.0
%endif


%description -n python3-%{pypi_name}
Tenacity is a general-purpose retrying library, written in Python, to simplify
the task of adding retry behavior to just about anything. It originates from a
fork of Retrying.

%endif

%description
Tenacity is a general-purpose retrying library, written in Python, to simplify
the task of adding retry behavior to just about anything. It originates from a
fork of Retrying.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
# Remove python3-only code (asyncio)
for file in _asyncio.py tests/test_asyncio.py; do
  rm %{buildroot}/%{python2_sitelib}/%{pypi_name}/$file
done
%endif
%if %{with python3}
%py3_install
%endif

%check
%if %{with python3}
# XXX: fails under python3
pytest-%{python3_version}
%endif
%if %{with python2}
pytest-%{python2_version} --ignore='tenacity/tests/test_asyncio.py'
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Rebuilt for Python 3.9

* Tue Feb 4 2020 Christopher Brown <chris.brown@redhat.com> - 6.0.0-1
- Bump to 6.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Christopher Brown <chris.brown@redhat.com> - 5.1.1-1
- Bump to 5.1.1
- Add setuptools_scm BR

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Christopher Brown <chris.brown@redhat.com> - 5.0.4-1
- Bump to 5.0.4

* Wed Jan 30 2019 Christopher Brown <chris.brown@redhat.com> - 5.0.3-1
- Bump to 5.0.3

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2-2
- Enable python dependency generator

* Tue Dec 4 2018 Christopher Brown <chris.brown@redhat.com> - 5.0.2-1
- Bump to 5.0.2
  Add conditionals for F30 and CentOS
  Add description macro

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.12.0-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Jul 19 2018 Matthias Runge <mrunge@redhat.com> - 4.12.0-1
- rebase to 4.12.0 (rhbz#1551561)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Pradeep Kilambi <pkilambi@redhat.com> - 4.9.0-1
- rebase to 4.9.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.0-3
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.8.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 Pradeep Kilambi <pkilambi@redhat.com> - 4.8.0-1
- rebase to 4.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug  5 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 4.4.0-1
- Upstream 4.4.0
- Run unit tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuild for Python 3.6

* Thu Oct 06 2016 Pradeep Kilambi <pkilambi@redhat.com> - 3.2.1-1
- rebase to 3.2.1

* Wed Sep 07 2016 Pradeep Kilambi <pkilambi@redhat.com> - 3.0.0-1
- initial package release
