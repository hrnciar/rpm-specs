%bcond_without tests

%global srcname progressbar2

%global desc %{expand: \
A text progress bar is typically used to display the progress of a long running
operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.}

Name:           python-%{srcname}
Version:        3.51.4
Release:        2%{?dist}
Summary:        A Progressbar library to provide visual progress to long running operations


License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:  %{py3_dist python-utils}
Requires:  %{py3_dist six}
BuildRequires:  %{py3_dist python-utils}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
%if %{with tests}
BuildRequires:  %{py3_dist freezegun} >= 0.3.10
%endif

# obsolete python-progressbar
Obsoletes:      python3-progressbar < 2.3-14
Provides:       python3-progressbar == %{version}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}
rm -rfv %{srcname}.egg-info

find . -name '*.pyc' -print -delete
find . -name '*.swp' -print -delete
rm -rfv tests/__pycache__/

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=. %pytest tests
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst CONTRIBUTING.rst
%{python3_sitelib}/%{srcname}-%{version}-py3.*.egg-info/
%{python3_sitelib}/progressbar

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.51.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Petr Viktorin <pviktori@redhat.com> - 3.51.4-1
- Update to 3.51.4
- Run pytest directly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.47.0-2
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Petr Viktorin <pviktori@redhat.com> - 3.47.0-1
- Update to latest upstream version
  https://github.com/WoLpH/python-progressbar/compare/v3.39.3...vv3.47.0
  Highlights:
  - Rate limiting
  - Added proper support for non-terminal output
  - Add MultiProgressBar

* Wed Feb 12 2020 Petr Viktorin <pviktori@redhat.com> - 3.39.3-7
- Remove linting BuildRequires
  https://bugzilla.redhat.com/show_bug.cgi?id=1795451
- Fix egg-info glob to work for Python 3.10+

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.39.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.39.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.39.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.39.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Orion Poplawski <orion@nwra.com> - 3.39.3-2
- Drop unneeded BR on pytest-cache

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.39.3-1
- Update to 3.39.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.39.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Petr Viktorin <pviktori@redhat.com> - 3.39.2-2
- Provide python3-progressbar

* Wed Dec 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.39.2-1
- Update to latest upstream commit
- Should fix failing tests

* Thu Dec 13 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.38.0-1
- Check tests and file issue upstream
- Initial build
- Drop py2 subpackage
- Obsolete python-progressbar
