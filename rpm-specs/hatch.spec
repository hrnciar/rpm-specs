Name:           hatch
Version:        0.23.0
Release:        3%{?dist}
Summary:        A modern project, package, and virtual env manager

License:        MIT or ASL 2.0
URL:            https://github.com/ofek/hatch
Source0:        https://files.pythonhosted.org/packages/source/h/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-userpath
BuildRequires:  python3-appdirs
BuildRequires:  python3-atomicwrites
BuildRequires:  python3-click
BuildRequires:  python3-coverage
BuildRequires:  python3-pip
BuildRequires:  python3-parse
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-semver
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sortedcontainers
BuildRequires:  python3-toml
BuildRequires:  python3-tqdm
BuildRequires:  python3-virtualenv
BuildRequires:  python3-wheel
BuildRequires:  twine

Requires:  git-core
Requires:  python3-userpath
Requires:  python3-appdirs
Requires:  python3-atomicwrites
Requires:  python3-click
Requires:  python3-coverage
Requires:  python3-colorama
Requires:  python3-pip
Requires:  python3-parse
Requires:  python3-pexpect
Requires:  python3-pytest
Requires:  python3-requests
Requires:  python3-semver
Requires:  python3-setuptools
Requires:  python3-six
Requires:  python3-sortedcontainers
Requires:  python3-toml
Requires:  python3-tqdm
Requires:  python3-virtualenv
Requires:  python3-wheel
Requires:  twine

%{?python_provide:%python_provide python3-%{name}}

%description
Hatch is a productivity tool designed to make your workflow easier and more
efficient, while also reducing the number of other tools you need to know.
It aims to make the 90% use cases as pleasant as possible.


%prep
%autosetup -p1 -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -k "not test_download_file"

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Lumír Balhar <lbalhar@redhat.com> - 0.23.0-1
- New upstream version 0.23.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Lumír Balhar <lbalhar@redhat.com> - 0.20.0-9
- Fix dependency name python3-twine → twine

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Lumír Balhar <lbalhar@redhat.com> - 0.20.0-6
- Bump release to rebuild in side tag f29-python with Python 3.7

* Wed Jun 27 2018 Lumír Balhar <lbalhar@redhat.com> - 0.20.0-5
- Fix FTBFS due to failing tests which newly requires internet connection

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Lumir Balhar <lbalhar@redhat.com> - 0.20.0-2
- Backslashes removed from description

* Wed Nov 15 2017 Lumir Balhar <lbalhar@redhat.com> - 0.20.0-1
- New upstream version
- New dependencies python-adduserpath (module userpath) and python-toml
- One test skipped due to internet connection requirement

* Wed Sep 13 2017 Lumir Balhar <lbalhar@redhat.com> - 0.11.0-1
- Initial package.
