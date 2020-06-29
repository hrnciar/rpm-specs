# Created by pyp2rpm-3.3.2
%global pypi_name userpath

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        2%{?dist}
Summary:        Cross-platform tool for adding locations to the user PATH

License:        MIT OR ASL 2.0
URL:            https://github.com/ofek/userpath
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  dos2unix

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
Ever wanted to release a cool new app but found it difficult to add its
location to PATH for users? Me too! This tool does that for you on all major
operating systems and does not require elevated privileges! Fear not, this
only modifies the user PATH; the system PATH is never touched nor even looked
at!

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(click)
Requires:       python3dist(distro)
Requires:       python3dist(setuptools)

# Old package name
Provides:       python3-adduserpath = %{version}-%{release}
Provides:       python3dist(adduserpath) = %{version}-%{release}
Provides:       python%{python_version}dist(adduserpath) = %{version}-%{release}
Obsoletes:      python3-adduserpath < 0.4.0.10

%description -n python3-%{pypi_name}
Ever wanted to release a cool new app but found it difficult to add its
location to PATH for users? Me too! This tool does that for you on all major
operating systems and does not require elevated privileges! Fear not, this
only modifies the user PATH; the system PATH is never touched nor even looked
at!

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Convert EOL encoding to Unix one
# https://github.com/ofek/userpath/issues/2
dos2unix -v README.rst

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Lumír Balhar <lbalhar@redhat.com> - 1.4.0-1
- Update to 1.4.0 (#1833676)

* Sat Feb 08 2020 Lumír Balhar <lbalhar@redhat.com> - 1.3.0-3
- Provide more variants of the old package name

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Lumír Balhar <lbalhar@redhat.com> - 1.3.0-1
- Initial package.
- Replacement for python-adduserpath
