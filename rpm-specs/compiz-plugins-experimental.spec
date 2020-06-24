%global  basever 0.8.16

Name:    compiz-plugins-experimental
Epoch:   1
Version: %{basever}
Release: 4%{?dist}
Summary: Additional plugins for Compiz
License: GPLv2+
URL:     https://gitlab.com/compiz/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Patch0:  compiz-plugins-experimental-0.8.16-gcc-10-fix.patch
# libdrm is not available on these arches
ExcludeArch: s390 s390x

BuildRequires: gcc-c++
BuildRequires: compiz-plugins-main-devel >= %{basever}
BuildRequires: compiz-plugins-extra-devel >= %{basever}
BuildRequires: compiz-bcop >= %{basever}
BuildRequires: perl(XML::Parser)
BuildRequires: intltool
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libtool
BuildRequires: libXScrnSaver-devel
BuildRequires: automake

Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
Requires: compiz-plugins-extra%{?_isa} >= %{basever}
Provides: compiz-plugins-unsupported%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported < %{epoch}:%{version}-%{release}

%description
The Compiz Fusion Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.
This package contains additional plugins from the Compiz Fusion Project

%package devel
Summary: Development files for Compiz-Fusion
Requires: compiz-plugins-main-devel%{?_isa} >= %{basever}
Requires: compiz-plugins-extra-devel%{?_isa} >= %{basever}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported-devel%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported-devel = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported-devel < %{epoch}:%{version}-%{release}

%description devel
This package contain development files required for developing other plugins


%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1 -b .gcc-10-fix
chmod -x src/cubemodel/fileParser.c src/cubemodel/cubemodel.c src/cubemodel/cubemodel-internal.h

%build
./autogen.sh
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%find_lang %{name}


%files -f %{name}.lang
%doc COPYING AUTHORS NEWS
%{_libdir}/compiz/*.so
%dir %{_datadir}/compiz/elements/
%dir %{_datadir}/compiz/fireflies/
%dir %{_datadir}/compiz/snow/
%dir %{_datadir}/compiz/stars/
%dir %{_datadir}/compiz/earth/
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*/*.frag
%{_datadir}/compiz/*/*.png
%{_datadir}/compiz/*/*.svg
%{_datadir}/compiz/*/*.vert
%{_datadir}/compiz/icons/hicolor/scalable/apps/*.svg

%files devel
%{_includedir}/compiz/compiz-elements.h


%changelog
* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-4
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1799249

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- Add models for the cubemodel plugin.
- Many improvements to the elements plugin.
- Increase bonanza animation speed.
- Add a default enabled option for stars, fireflies, wizard and snow.
- Improvements to the static plugin.
- Exit on user input after starting screensaver manually.
- Improve the default snow texture.
- Increase maximum text size in workspacenames.
- Add earth plugin.
- Update translations.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 28 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-3
- add correct epoch versions
- own directories
- fix permissions

* Sun Mar 27 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-2
- initial package
- rename compiz-plugins-unsupported to compiz-plugins-experimental

