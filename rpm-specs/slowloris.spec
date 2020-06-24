Name:           slowloris
Version:        0.2.1
Release:        2%{?dist}
Summary:        Low bandwidth DoS tool

License:        MIT
URL:            https://github.com/gkbrk/slowloris
Source0:        %{pypi_source Slowloris}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%package -n     python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%prep
%autosetup -n Slowloris-%{version}
# Use setuptools
sed -i -e "s/distutils.core/setuptools/g" setup.py
# Remove shebang
sed -i -e '/^#!\//, 1d' %{name}.py

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{name}

%files -n python3-%{name}
%doc README.md
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/Slowloris-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Add README and LICENSE file
- Update to latest upstream release 0.2.1

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora

