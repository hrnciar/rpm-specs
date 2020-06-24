%global commit dae177189b12f74ea01ac2389b76326c06d9be78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20190925

Name:           non-ntk
Version:        1.3.1000
Release:        0.3.%{commitdate}git%{shortcommit}%{?dist}
Summary:        A fork of FLTK for the non audio suite

# themes are GPLv2+, FLTK derived code is LGPLv2+
License:        LGPLv2+ with exceptions and GPLv2+
URL:            http://non.tuxfamily.org/
Source0:        %{name}-%{commitdate}-git%{shortcommit}.tar.xz
# script to create source tarball from git
# sh non-snapshot.sh $(rev)
Source1:        %{name}-snapshot.sh
# No desktop file in tarball
Source2:        ntk-fluid.desktop
# Appdata for ntk-fluid
Source3:        ntk-fluid.appdata.xml
# Desktop file for ntk-chtheme
Source4:        ntk-chtheme.desktop
# Fix wrong FSF address
Patch0:         %{name}-fsf.patch
# Use system provided scandir
Patch1:         %{name}-scandir.patch
# Delete wrong compiler flags
Patch2:         %{name}-flags.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel >= 1.10.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python3
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xft)

%description
%{name} is a fork of the FLTK UI toolkit. It employs cairo support and
other additions not accepted upstream. It is currently used by the non-*
audio suite of programs.

%package devel
Summary:        Development files for the non-ntk GUI library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the Non-ntk GUI library

%package fluid
Summary: Fast Light User Interface Designer
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description fluid
%{summary}, an interactive GUI designer for %{name}.

%prep
%autosetup -p 1 -n non-ntk-%{commitdate}

%build
%set_build_flags
python3 ./waf -v configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --enable-gl
python3 ./waf -v %{?_smp_mflags}

%install
# Do not run ldconfig
export DESTDIR="%{buildroot}"

python3 ./waf -v install --destdir=%{buildroot}

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
 %{SOURCE2} %{SOURCE4}

# Install appdata file
install -d -m755 %{buildroot}%{_metainfodir}
install -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}

# Delete static libraries
rm %{buildroot}%{_libdir}/libntk*.a*

%check
# Validate desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-fluid.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-chtheme.desktop

# Validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ntk-fluid.appdata.xml

%files
%doc README
%license COPYING
%{_libdir}/libntk*.so.1*

%files devel
%{_libdir}/libntk.so
%{_libdir}/libntk_images.so
%{_libdir}/libntk_gl.so
%{_includedir}/ntk
%{_libdir}/pkgconfig/*

%files fluid
%{_datadir}/applications/ntk-fluid.desktop
%{_datadir}/applications/ntk-chtheme.desktop
%{_metainfodir}/ntk-fluid.appdata.xml
%{_bindir}/ntk-*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1000-0.3.20190925gitdae1771
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.1000-0.2.20190925gitdae1771
- Add appdata for ntk-fluid
- Add desktop file for ntk-chtheme
- Correctly glob shared libraries
- Document patches

* Sun Jan 05 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.1000-0.1.20190925gitdae1771
- Unretire non-ntk

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.17.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.16.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.15.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.14.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.13.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.12.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.0-0.11.20130730gitd006352
- buildfix: missing fl_scandir
- Added BR: python2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.10.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.9.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.8.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.7.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.6.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.5.20130730gitd006352
- Add exceptions to LGPLv2 license
- add desktop scriptlet post fluid

* Mon Sep 02 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.4.20130730gitd006352
- Adjust license 
- Remove icon scriptlets
- Correct BRs

* Thu Aug 29 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.3.20130730gitd006352
- Correct license
- Remove static libraries
- Correct optflags and BRs

* Sat Aug 17 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.1.20130730gitd006352
- Initial package
