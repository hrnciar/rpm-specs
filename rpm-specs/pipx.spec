Name:           pipx
Version:        0.15.3.1
Release:        2%{?dist}
Summary:        Install and run python applications in isolated environments

License:        MIT and BSD
URL:            https://pypi.python.org/pypi/pipx
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(argcomplete)
BuildRequires:  python3dist(userpath)

%{?python_provide:%python_provide python3-%{name}}

%description 
A python module and utility that create virtualenvs for python applications.

%prep
%autosetup
# Pacify rpmlint - eliminate bogus shebang line from non-executable files
sed -i -e 's|#!.*||' src/%{name}/main.py
sed -i -e 's|#!.*||' src/%{name}/venv_metadata_inspector.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.3.1-2
- Rebuilt for Python 3.9

* Mon May 18 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.3.1-1
- Update to upstream release 0.15.3.1

* Tue Jan 21 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.1.3-1
- Update to upstream release 0.15.1.3

* Sun Jan 12 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.1.2-1
- Update to upstream release 0.15.1.2

* Sat Jan 04 2020 Martin Jackson <mhjacks@swbell.net> - 0.14.0.0-1
- Convert to pipx name
