#global commit 5760c9d30e793de3d65475167ad1a0a652f3a16f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           svg2svgt
Version:        0.9.6
Release:        7%{?commit:.git%shortcommit}%{?dist}
Summary:        SVG to SVG Tiny converter

License:        LGPLv2+
URL:            https://github.com/manisandro/svg2svgt
Source0:        https://github.com/manisandro/svg2svgt/archive/%{?commit:%commit}%{!?commit:v%version}/%{name}-%{?commit:%shortcommit}%{!?commit:%version}.tar.gz

# Add missing include
Patch0:         svg2svgt_includes.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
Library and tools to convert SVG images to SVG Tiny, the subset of SVG
implemented by QtSvg.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%autosetup -p1 -n %{name}-%{?commit:%commit}%{!?commit:%version}


%build
LDFLAGS="%{__global_ldflags} -Wl,--as-needed" %cmake .
%make_build


%install
%make_install

%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %{name} --with-qt


%check
make check %{?_smp_mflags}

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSE.LGPL
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_libdir}/lib%{name}.so.*
%dir %{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.6-2
- Remove obsolete scriptlets

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-1
- Update to 0.9.6

* Wed Aug 30 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.3.git5760c9d
- Added %%{?_smp_mflags} to make check

* Tue Aug 29 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.2.git5760c9d
- Added desktop and appdata files
- Add -Wl,--as-needed

* Mon Aug 28 2017 Sandro Mani <manisandro@gmail.com> - 0.9.6-0.1.git7a182a9
- Initial package
