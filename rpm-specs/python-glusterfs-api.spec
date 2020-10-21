# What's in a name ? :‑O
#
# * The source repo is named libgfapi-python
# * The python package is named gfapi
# * The RPM package is named python-glusterfs-api to be analogous to
#   glusterfs-api RPM which provides the libgfapi C library

%global src_repo_name libgfapi-python
%global python_pkg_name gfapi
%global pkg_name glusterfs-api

%if ( 0%{?fedora} && 0%{?fedora} > 26 ) || ( 0%{?rhel} && 0%{?rhel} > 7 )
%global with_python3 1
%endif

%global _description \
libgfapi is a library that allows applications to natively access \
GlusterFS volumes. This package contains python bindings to libgfapi. \
See https://libgfapi-python.rtfd.io/ for more details.

Name:             python-%{pkg_name}
Summary:          Python bindings for GlusterFS libgfapi
Version:          1.2
Release:          8%{?dist}
License:          GPLv2 or LGPLv3+
URL:              https://github.com/gluster/%{src_repo_name}
Source0:          %pypi_source %{python_pkg_name} %{version}

%description %{_description}

%package -n python3-%{pkg_name}
Summary:          Python bindings for GlusterFS libgfapi
BuildArch:        noarch
BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
# Requires libgfapi.so
Requires:         glusterfs-api >= 4.1.0
# Requires gluster/__init__.py
Requires:         python3-gluster >= 4.1.0
Obsoletes:        python2-glusterfs-api < %{version}
Obsoletes:        python-glusterfs-api < %{version}

%description -n python3-%{pkg_name} %{_description}

%global debug_package %{nil}

%prep
%autosetup -n %{python_pkg_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.rst
%license COPYING-GPLV2 COPYING-LGPLV3
%{python3_sitelib}/*
# As weird as it may seem, excluding __init__.py[co] is intentional as
# it is provided by python-gluster package which is a dependency.
%exclude %{python3_sitelib}/gluster/__init__*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 1.2-1
- python-glusterfs-api 1.2 GA

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Kaleb S. KEITHLEY <kkeithle[at]redhat.com>
- %__python2, %python2_sitelib, and %license globals for EL6

* Thu Jan 19 2017 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 1.1-2
- Initial import plus RHEL feature test for python-devel

* Tue Aug 9 2016 Prashanth Pai <ppai@redhat.com> - 1.1-1
- Update spec file

* Wed May 20 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-1
- Change Package name to python-glusterfs-api instead of python-gluster-gfapi.

* Mon May 18 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0beta3
- Added license macro.

* Wed Apr 15 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0beta2
- Added detailed description for this package.

* Tue Apr 14 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0beta1
- Renamed glusterfs module to gluster

* Wed Feb 11 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0
- Introducing spec file.
