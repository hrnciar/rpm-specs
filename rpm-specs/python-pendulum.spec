%global pypi_name pendulum

Name:           python-%{pypi_name}
Version:        2.1.2
Release:        2%{?dist}
Summary:        Python datetimes made easy

License:        MIT
URL:            https://pendulum.eustace.io
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(toml)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-2
- Update build workflow

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to new upstream release 2.1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-2
- Fix description (rhbz#1790074)

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-1
- Initial package for Fedora
