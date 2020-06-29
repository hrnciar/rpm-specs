%global         rctag rc3

Name:           unicorn
Version:        1.0.2
Release:        0.2.%{rctag}%{?dist}
Summary:        A lightweight multi-platform, multi-architecture CPU emulator framework

# GPLv2:        Most of unicorn is licensed under the GPLv2, with exception
#               being the code which followed the project's fork of QEMU.
# LGPLv2:       Portions of code from QEMU
# MIT:          Portions of code from QEMU
# BSD:          Portions of code from QEMU
License:        GPLv2 and LGPLv2+ and MIT and BSD
URL:            https://www.unicorn-engine.org/
Source0:        https://github.com/unicorn-engine/%{name}/archive/%{version}%{rctag}/%{name}-%{version}-%{rctag}.tar.gz
BuildRequires:  gcc
BuildRequires:  python3-devel

# Much of Unicorn follows from QEMU, which the Unicorn project forked in
# 2015. Since then, the Unicorn team has applied a number of bugfixes to
# the forked QEMU code along with the modifications necessary for Unicorn.
# QEMU 2.2.1 formed the basis of this work. The Unicorn project documents
# the relationship between Unicorn and QEMU at
# http://www.unicorn-engine.org/docs/beyond_qemu.html.
Provides: bundled(qemu) = 2.2.1

%description
Unicorn is a lightweight multi-platform, multi-architecture CPU emulator
framework.

%package devel
Summary:        Files needed to develop applications using unicorn
Requires:       %{name} = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other resources
needed for developing applications using unicorn.

%package -n python3-unicorn
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-unicorn
The unicorn-python3 package contains python3 bindings for unicorn.

%prep
%autosetup -n %{name}-%{version}-%{rctag}

%build
%make_build
pushd bindings/python
%py3_build
popd

%install
%make_install LIBDIRARCH=%{_lib} UNICORN_STATIC=no
pushd bindings/python
%py3_install
popd
rm -rf %{buildroot}%{python3_sitelib}/unicorn/include
rm -rf %{buildroot}%{python3_sitelib}/unicorn/lib

%ldconfig_scriptlets

%files
%doc AUTHORS.TXT ChangeLog CREDITS.TXT README.md
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/unicorn.pc
%{_includedir}/unicorn/

%files -n python3-unicorn
%{python3_sitelib}/%{name}-%{version}%{rctag}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-0.2.rc3
- Rebuilt for Python 3.9

* Mon May 18 2020 W. Michael Petullo <mike@flyn.org> - 1.0.2-0.1.rc3
- Update to 1.0.2-rc3 to satisfy pwntools (Red Hat Bugzilla #1836767 and #1833654)
- Removed obsolete patch to use python2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-7
- Subpackage python2-unicorn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-6
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 W. Michael Petullo <mike@flyn.org> - 1.0.1-3
- Add patch to use python2 rather than python when building

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 W. Michael Petullo <mike@flyn.org> - 1.0.1-1
- Initial package
