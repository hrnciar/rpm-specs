%global srcname rustcfg
%{?python_enable_dependency_generator}

Name:           python-rustcfg
Version:        0.0.2
Release:        7%{?dist}
Summary:        Rust cfg expression parser in python

License:        MIT
URL:            https://pagure.io/fedora-rust/python-rustcfg
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %_description

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pyparsing)
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{_description}

%package     -n python3-%{srcname}-tests
Summary:        Tests for python3-%{srcname}
%{?python_provide:%python_provide python3-%{srcname}-tests}
Requires:       python3-%{srcname} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-pytest

%description -n python3-rustcfg-tests
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/rustcfg-*.egg-info/
%{python3_sitelib}/rustcfg/
%exclude %{python3_sitelib}/rustcfg/test

%files -n python3-%{srcname}-tests
%{python3_sitelib}/%{srcname}/test/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.2-1
- Update to 0.0.2

* Thu Aug 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.1-3
- Rebase with PyPI tarball

* Thu Aug 16 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.1-2
- Split out tests subpackage to avoid dependency on pytest

* Mon Aug 13 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.1-1
- Initial packaging (#1615629)
