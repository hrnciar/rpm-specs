%global shortname mediawriter

%{?mingw_package_header}

Name:           mingw-mediawriter
Version:        4.1.6
Release:        1%{?dist}
Summary:        Fedora Media Writer

License:        GPLv2+
URL:            https://github.com/FedoraQt/MediaWriter
Source0:        https://github.com/FedoraQt/MediaWriter/archive/MediaWriter-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtdeclarative
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-xz-libs

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtdeclarative
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-xz-libs

BuildRequires:  gettext

%description
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.


# Win32
%package -n mingw32-%{shortname}
Summary:        Fedora Media Writer
BuildArch:      noarch

%description -n mingw32-%{shortname}
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.

# Win64
%package -n mingw64-%{shortname}
Summary:        Fedora Media Writer
BuildArch:      noarch

%description -n mingw64-%{shortname}
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n MediaWriter-%{version}

%build
mkdir build_win32
pushd build_win32
%mingw32_qmake_qt5 PREFIX=%{mingw32_prefix} MEDIAWRITER_VERSION=%{version}-%{release} ../%{shortname}.pro
popd

mkdir build_win64
pushd build_win64
%mingw64_qmake_qt5 PREFIX=%{mingw64_prefix} MEDIAWRITER_VERSION=%{version}-%{release} ../%{shortname}.pro
popd

%mingw_make %{?_smp_mflags}

%install
%mingw_make install INSTALL_ROOT=$RPM_BUILD_ROOT


# Win32
%files -n mingw32-%{shortname}
%{mingw32_bindir}/%{shortname}.exe
%dir %{mingw32_libexecdir}/%{shortname}/
%{mingw32_libexecdir}/%{shortname}/helper.exe

%files -n mingw64-%{shortname}
%{mingw64_bindir}/%{shortname}.exe
%dir %{mingw64_libexecdir}/%{shortname}/
%{mingw64_libexecdir}/%{shortname}/helper.exe

%changelog
* Wed Sep 16 2020 Jan Grulich <jgrulich@redhat.com> - 4.1.6-1
- 4.1.6

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Martin Bříza <m@rtinbriza.cz> - 4.1.5-1
- Update to 4.1.5
- Resolves #1818673

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 4.1.4-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Tomáš Popela <tpopela@redhat.com> - 4.1.4-1
- Update to 4.1.4

* Sun Apr 21 2019 Martin Bříza <m@rtinbriza.cz> - 4.1.3-1
- Update to 4.1.3
- Resolves #1664530

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Martin Bříza <m@rtinbriza.cz> - 4.1.2-1
- Update to 4.1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Martin Bříza <mbriza@redhat.com> - 4.1.1-1
- Update to 4.1.1

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 4.1.0-3
- Fix debug file in main package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Martin Bříza <mbriza@redhat.com> 4.1.0-1
- Update to 4.1.0

* Wed Mar 22 2017 Martin Bříza <mbriza@redhat.com> 4.0.95-1
- Update to 4.0.95

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Martin Bříza <mbriza@redhat.com> 4.0.8-0
- Update to 4.0.8

* Tue Nov 22 2016 Martin Bříza <mbriza@redhat.com> 4.0.7-0
- Update to 4.0.7

* Fri Nov 11 2016 Martin Bříza <mbriza@redhat.com> 4.0.4-0
- Update to 4.0.4

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-0
- Update to 4.0.0

* Tue Oct 11 2016 Martin Bříza <mbriza@redhat.com> 3.97.2-0
- Update to 3.97.2

* Fri Sep 23 2016 Martin Bříza <mbriza@redhat.com> 3.97.1-0
- Update to 3.97.1

* Thu Sep 22 2016 Martin Bříza <mbriza@redhat.com> 3.97.0-0
- Update to 3.97.0

* Fri Sep 16 2016 Martin Bříza <mbriza@redhat.com> 3.96.0-0
- Update to 3.96.0

* Thu Aug 25 2016 Martin Bříza <mbriza@redhat.com> 0-0.1git0049ab3
- Initial release
