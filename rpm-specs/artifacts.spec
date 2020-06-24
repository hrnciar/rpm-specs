%global pypi_name artifacts
%global date 20200118

Name:           %{pypi_name}
Version:        0.0.%{date}
Release:        2%{?dist}
Summary:        A collection of digital forensic artifacts

License:        ASL 2.0
URL:            https://github.com/ForensicArtifacts/artifacts
Source0:        https://github.com/ForensicArtifacts/artifacts/releases/download/%{date}/%{pypi_name}-%{date}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml

%description
A free, community-sourced, machine-readable knowledge base of digital
forensic artifacts that the world can use both as an information source
and within other tools.

If you'd like to use the artifacts in your own tools, all you need to be
able to do is read YAML. That is it, no other dependencies. The Python
code in this project is just used to validate all the artifacts to make
sure they follow the specification.

%prep
%autosetup -n %{pypi_name}-%{date}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_defaultdocdir}/%{pypi_name}/LICENSE

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib}/ pytest-%{python3_version} -v tests

%files
%doc ACKNOWLEDGEMENTS AUTHORS README
%license LICENSE
%{_bindir}/*.py
%{_datadir}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{date}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20200118-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200118-1
- Update to latest upstream release 20200118

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190320-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190320-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190320-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190320-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20190320-1
- Update version (rhbz#1720865)

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20190320-1
- Initial package for Fedora
