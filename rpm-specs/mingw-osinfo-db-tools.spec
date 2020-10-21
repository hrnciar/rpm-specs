%{?mingw_package_header}

Name: mingw-osinfo-db-tools
Version: 1.7.0
Release: 5%{?dist}
Summary: MinGW Windows port of a library for managing OS information for virtualization
License: LGPLv2+
Source: https://releases.pagure.org/libosinfo/osinfo-db-tools-%{version}.tar.xz
URL: https://libosinfo.org

BuildArch: noarch

BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext

BuildRequires: mingw32-filesystem >= 107
BuildRequires: mingw64-filesystem >= 107
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-glib2
BuildRequires: mingw64-glib2
BuildRequires: mingw32-json-glib
BuildRequires: mingw64-json-glib
BuildRequires: mingw32-libxml2
BuildRequires: mingw64-libxml2
BuildRequires: mingw32-libxslt
BuildRequires: mingw64-libxslt
BuildRequires: mingw32-libarchive
BuildRequires: mingw64-libarchive
BuildRequires: mingw32-libsoup
BuildRequires: mingw64-libsoup

BuildRequires: pkgconfig

BuildRequires: /usr/bin/pod2man

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%package -n mingw32-osinfo-db-tools
Summary: %{summary}

Requires: pkgconfig

%description -n mingw32-osinfo-db-tools
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%package -n mingw64-osinfo-db-tools
Summary: %{summary}

Requires: pkgconfig

%description -n mingw64-osinfo-db-tools
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%{?mingw_debug_package}

%prep
%setup -q -n osinfo-db-tools-%{version}

%build
%mingw_meson
%mingw_ninja

%install
%mingw_ninja_install

# Manpages don't need to be bundled
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

%mingw_find_lang osinfo-db-tools

%files -n mingw32-osinfo-db-tools -f mingw32-osinfo-db-tools.lang
%doc NEWS README
%license COPYING
%{mingw32_bindir}/osinfo-db-export.exe
%{mingw32_bindir}/osinfo-db-import.exe
%{mingw32_bindir}/osinfo-db-path.exe
%{mingw32_bindir}/osinfo-db-validate.exe

%files -n mingw64-osinfo-db-tools -f mingw64-osinfo-db-tools.lang
%doc NEWS README
%license COPYING
%{mingw64_bindir}/osinfo-db-export.exe
%{mingw64_bindir}/osinfo-db-import.exe
%{mingw64_bindir}/osinfo-db-path.exe
%{mingw64_bindir}/osinfo-db-validate.exe

%changelog
* Wed Aug 12 13:44:13 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.7.0-5
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.7.0-3
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.7.0-1
- Update to 1.7.0 release

* Fri Jul 26 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.6.0-1
- Update to 1.6.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.5.0-1
- Update to 1.5.0 release

* Mon Mar 04 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.4.0-1
- Initial package
