Name:           micropipenv
Version:        1.0.0
Release:        1%{?dist}
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPLv3+
URL:            https://github.com/thoth-station/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)
# For testing
BuildRequires:  python3dist(flexmock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-venv)

%{?python_provide:%python_provide python3-%{name}}

Requires:       python3dist(pip)
Requires:       python3dist(setuptools)
Requires:       python3dist(toml)

%description
A lightweight wrapper for pip to support Pipenv and Poetry lock files or
converting them to pip-tools compatible output.

%prep
%autosetup -n %{name}-%{version}
# Remove shebang line from the module
sed -i '1{\@^#!/usr/bin/env python@d}' %{name}.py

%build
%py3_build

%install
%py3_install

%check
# skipped tests requires internet
%pytest -m "not online"

%files
%doc README.rst
%license LICENSE*
%{_bindir}/micropipenv
%pycached %{python3_sitelib}/%{name}.py
%{python3_sitelib}/%{name}-%{version}-py*.egg-info/

%changelog
* Fri Oct 02 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1884346)

* Thu Sep 03 2020 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Update to 0.6.0 (#1875250)

* Thu Jul 30 2020 Lumír Balhar <lbalhar@redhat.com> - 0.5.1-1
- Update to 0.5.1 (#1859995)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Lumír Balhar <lbalhar@redhat.com> - 0.4.0-1
- Update to 0.4.0 (#1854424)

* Mon Jun 15 2020 Lumír Balhar <lbalhar@redhat.com> - 0.3.0-1
- Update to 0.3.0 (#1846944)

* Fri Jun 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Correct the license tag (GPLv3+ to LGPLv3+)
- Include the actual LICENSE files in the package

* Thu Jun 04 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.0-1
- Update to 0.2.0 (#1838278, #1841641)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.6-1
- Update to 0.1.6 (#1831328)

* Tue Apr 07 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.5-1
- Update to 0.1.5 (#1821807)

* Thu Mar 12 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.4-1
- Initial package.
