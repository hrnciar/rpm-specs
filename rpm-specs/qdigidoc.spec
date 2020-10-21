# Tool for managing estonian ID card and provide fully qualified digital
# signature for users of Estonian ID card.
# Limited support is also available for ID Cards of Latvia and Finland.
%global upstream_name qdigidoc4

Name:           qdigidoc
Version:        4.2.7
Release:        2%{?dist}
Summary:        Estonian digital signature and encryption application
License:        LGPLv2+
URL:            https://github.com/open-eid/DigiDoc4-Client
Source0:        %{url}/releases/download/v%{version}/%{upstream_name}-%{version}.tar.gz
Source1:        config.json
Source2:        config.pub
Source3:        config.rsa
Source4:        config.qrc
Source5:        EE.xml
Source6:        TSL.qrc
Source7:        eu-lotl.xml

Patch0:         sandbox-qdigidoc4.patch
Patch1:         qdigidoc-nautilus-extension.patch

BuildRequires:  cmake3 >= 3.5
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libdigidocpp-devel >= 3.14.4
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(libpcsclite) >= 1.7
BuildRequires:  libappstream-glib
BuildRequires:  qtsingleapplication-qt5-devel
Requires:       hicolor-icon-theme
# Dynamically loaded library
Requires:       opensc%{?_isa}
Requires:       pcsc-lite-ccid%{?_isa}

Obsoletes:     qesteidutil <= 3.2.1
Provides:      qesteidutil >= 4.0.0

%description
DigiDoc4 Client is an application for digitally signing and encrypting
documents; the software includes functionality to manage Estonian ID-card -
change pin codes, update certificates etc.


%package        nautilus
Summary:        Nautilus extension for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus-python

%description    nautilus
The %{name}-nautilus package contains the %{name} 
extension for the nautilus file manager.

%prep
%setup -q -n %{upstream_name}-%{version}

%patch0 -p1
%patch1 -p1

cp %{S:1} %{S:2} %{S:3} %{S:4} common/
cp %{S:5} %{S:6} %{S:7} client/

%build
%if 0%{?el7}
. /opt/rh/devtoolset-7/enable
mkdir %{_target_platform} 
pushd %{_target_platform}
%cmake3 \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DDONT_USE_INTERNAL_LUA=OFF \
        -DBUILD_NOISE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=ON \
        %ifarch ppc64le
        -DUSE_OPENCL=OFF \
        %endif
        ..
%endif
#
# Germano Massullo: I wanted to use %%elseif but it is not yet active in
# Fedora, etc., despite is supported upstream. I did not compare the Fedora RPM version
# but I empirically verified that %%elseif and %%elif do not work here, even if you don't get
# errors during builds
# https://github.com/rpm-software-management/rpm/issues/311
# https://github.com/debbuild/debbuild/issues/182
# 
#
%if (0%{?el8} || (0%{?fedora} < 33))
mkdir %{_target_platform} 
pushd %{_target_platform}
%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir}
        ..
%else
%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir}
%endif

%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_build
%else
%make_build
popd
%endif

%install
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_install
%else
pushd %{_target_platform}
%make_install
popd
%endif

desktop-file-validate %{buildroot}/%{_datadir}/applications/qdigidoc4.desktop

%find_lang nautilus-qdigidoc

%files
%doc README.md CONTRIBUTING.md RELEASE-NOTES.md
%license COPYING LICENSE.LGPL
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_mandir}/man1/qdigidoc4.1*
%{_datadir}/kservices5/*.desktop

%files nautilus -f nautilus-qdigidoc.lang
%{_datadir}/nautilus-python/extensions/*

%changelog
* Mon Oct 12 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.7-2
- Reinistate sandbox build patch

* Fri Oct 09 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.7-1
- Upstream release 4.2.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.5-2
- Update dependency to latest libdigidocpp (3.14.3)

* Fri Jun 26 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.5-1
- Upstream release 4.2.5

* Thu Jan 30 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.4-1
- Upstream release 4.2.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.3-1
- Upstream release 4.2.3

* Tue Aug 06 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.2-4
- Call cmake3 explicitly to fix epel7 build

* Wed Jul 31 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.2-3
- Patch nautilus extension to work with python 3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.2-1
- Upstream release 4.2.2

* Fri Jul 19 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.1-1
- Upstream release 4.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Germano Massullo <germano@germanomassullo.org> - 4.2.0-4
- added Provides: qesteidutil

* Tue Dec 11 2018 Germano Massullo <germano@germanomassullo.org> - 4.2.0-3
- adding obsoletes: qesteidutil for F30

* Tue Dec 04 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.0-2
- Add proper provides and obsoletes

* Tue Dec 04 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.2.0-1
- Upstream release 4.2.0

* Mon Nov 19 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.1.0-1
- Upstream release 4.1.0

* Thu Oct 04 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.0.0-4
- Use the officially provided zip pack
- Update static resource files

* Mon Jun 25 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.0.0-3
- Add instructions on how to obtain the tarball
- Re-pack the sources tarball with ones obtained from VCS.

* Mon Jun 18 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.0.0-2
- Add a patch for sanbox compilation

* Wed Jun 13 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 4.0.0-1
- Update sources to the 4.0.0 release
- Add a patch to workaround the Qt 5.11 compatibility

* Sun Jun 03 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 0.6.0-3
- Update sources to the latest one

* Thu May 03 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 0.6.0-2
- Remove filetype bindings and icons to avoid conflict with DigiDoc3

* Tue May 01 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 0.6.0-1
- Initial packaging of 0.6.0 beta
