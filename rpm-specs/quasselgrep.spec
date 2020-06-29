%global commit0 502c88bdc7613abb68e868eb520e39ec8a5cf6dd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Created by pyp2rpm-3.2.2
%global pypi_name quasselgrep

# This package is not published to PyPI; it is purely a
# command line application that happens to be written in Python.

Name:           quasselgrep
Version:        0.1
Release:        0.10.20170411git%{shortcommit0}%{?dist}
Summary:        Tool for searching quassel logs from the commandline

License:        GPLv2 and BSD
URL:            https://github.com/fish-face/quasselgrep
Source0:        https://github.com/fish-face/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

# Port to python3 using modernize. I sent this patch upstream.
Patch0:         https://patch-diff.githubusercontent.com/raw/fish-face/quasselgrep/pull/12.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-future

Requires:       python3-dateutil
Requires:       python3-crypto
Requires:       python3-psycopg2
Requires:       python3-six

# Since this _is_ a python package, provide python3-quasselgrep.
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
quasselgrep is a tool for searching quassel logs from the commandline.
It can run against both SQLite and PostgreSQL databases, and also
supports running in a client/server mode.

%prep
%autosetup -n %{pypi_name}-%{commit0} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix chbang.
# Actually we should just delete the chbang.
sed "/env python/d" -i quasselgrep/quasselgrep.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/quasselgrep
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.10.20170411git502c88b
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20170411git502c88b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.8.20170411git502c88b
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.7.20170411git502c88b
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20170411git502c88b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.20170411git502c88b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20170411git502c88b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.3.20170411git502c88b
- Rebuilt for Python 3.7

* Thu Apr 12 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.1-0.2.20170411git502c88b
- Port to Python 3 using the 'modernize' tool.

* Thu Jun 29 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.1-0.1.20170411git502c88b
- Initial package.
