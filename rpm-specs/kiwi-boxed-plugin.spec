# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global desc \
The KIWI boxed plugin provides support for self contained building \
of images based on fast booting VM images.

%global srcname kiwi_boxed_plugin

Name:           kiwi-boxed-plugin
Version:        0.1.4
Release:        1%{?dist}
URL:            https://github.com/OSInside/kiwi-boxed-plugin
Summary:        KIWI - Boxed Build Plugin
License:        GPLv3+
# We must use the version uploaded to pypi, as it contains all the required files.
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# doc build requirements
BuildRequires:  python3dist(cerberus)
BuildRequires:  python3dist(docopt)
BuildRequires:  python3dist(kiwi)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)

Requires:       python3-%{name} = %{version}-%{release}
Supplements:    (kiwi-cli and qemu-kvm)
Provides:       %{srcname} = %{version}-%{release}

BuildArch:      noarch

%description %{desc}

%package -n python3-%{name}
Summary:        KIWI - Boxed Build Plugin - Python 3 implementation
Supplements:    (python%{python3_version}dist(kiwi) and qemu-kvm)
Requires:       qemu-kvm
Provides:       python3-%{srcname} = %{version}-%{release}

%description -n python3-%{name} %{desc}

This package provides the Python 3 library plugin.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

# Install documentation
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install

# Delete this now, we'll docify later
rm -f %{buildroot}%{_defaultdocdir}/python-%{srcname}/LICENSE
rm -f %{buildroot}%{_defaultdocdir}/python-%{srcname}/README

%files
%doc README.rst
%{_mandir}/man8/*.8*

%files -n python3-%{name}
%license LICENSE
%{python3_sitelib}/%{srcname}*

%changelog
* Sat Aug 15 2020 Neal Gompa <ngompa13@gmail.com> - 0.1.4-1
- Update to 0.1.4 (RH#1837026)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Neal Gompa <ngompa13@gmail.com> - 0.1.0-1
- Initial packaging
