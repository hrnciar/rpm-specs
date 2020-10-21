%global shortname graphlcd

Summary:        GraphLCD drivers and tools
Name:           %shortname-base
Version:        2.0.0
Release:        2%{?dist}
License:        GPLv2+
URL:            http://projects.vdr-developer.org/projects/graphlcd
Source0:        https://projects.vdr-developer.org/git/%{name}.git/snapshot/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  perl-interpreter
BuildRequires:  systemd
BuildRequires:  zlib-devel

%description
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

%package -n glcddrivers
Summary:        GraphLCD shared driver library
License:        GPLv2+ 
Provides:       libglcddrivers%{?_isa}  = %{version}-%{release}
# While the library doesn't use graphlcd-config directly, it is
# useless without the linked program using it.
# (Anssi) FIXME: What? If the above is true then this is bogus.
Requires:       %shortname-common%{?_isa}  >= %{version}

%description -n glcddrivers
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the driver library needed to run programs
dynamically linked with GraphLCD.

%package -n %{shortname}-devel
Summary:        Headers for graphlcd
License:        GPLv2+
Requires:       glcddrivers%{?_isa}  = %{version}
Requires:       glcdgraphics%{?_isa}  = %{version}
Requires:       glcdskin%{?_isa}  = %{version}
Provides:       libglcddrivers-devel%{?_isa}  = %{version}-%{release}
Provides:       glcddrivers-devel%{?_isa}  = %{version}-%{release}
Provides:       libglcdgraphics-devel%{?_isa}  = %{version}-%{release}
Provides:       glcdgraphics-devel%{?_isa}  = %{version}-%{release}
Provides:       graphlcd-devel%{?_isa}  = %{version}-%{release}

%description -n %{shortname}-devel
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the headers that programmers will need to
develop applications which will use graphlcd-base.

%package -n glcdgraphics
Summary:        GraphLCD shared graphics library
License:        GPLv2+
Provides:       libglcdgraphics%{?_isa}  = %{version}-%{release}
# While the library doesn't use graphlcd-config directly, it is
# useless without the linked program using it.
# (Anssi) FIXME: See previous fixme.
Requires:       %{shortname}-common%{?_isa}  >= %{version}

%description -n glcdgraphics
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the graphics library needed to run programs
dynamically linked with GraphLCD.

%package -n glcdskin
Summary:        GraphLCD shared skin library
License:        GPL+

%description -n glcdskin
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the skin library needed to run programs
dynamically linked with libglcdskin.

%package -n graphlcd-common
Summary:        GraphLCD configuration file and documentation
License:        GPL+

%description -n graphlcd-common
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the GraphLCD configuration file and GraphLCD
documentation.

%package -n graphlcd-tools
Summary:        GraphLCD tools
License:        GPLv2+

%description -n graphlcd-tools
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains tools to use with GraphLCD.

%prep
%autosetup -p1
# don't strip nor chmod to root
perl -pi -e 's,-o root -g root -s,,' $(find -name Makefile)

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX ?= /usr/local|PREFIX ?= %{_prefix}|' \
    -e 's|LIBDIR ?= $(PREFIX)/lib|LIBDIR ?= %{_libdir}|' \
    -e 's|UDEVRULESDIR ?= /etc/udev/rules.d|UDEVRULESDIR ?= %{_udevrulesdir}|' \
    Make.config

# W: file-not-utf8
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
%make_build

%install
%make_install

install -d -m755 %{buildroot}%{_sysconfdir}
install -m644 graphlcd.conf %{buildroot}%{_sysconfdir}

%files -n glcddrivers
%doc README
%license COPYING
%{_libdir}/libglcddrivers.so.2*

%files -n %{shortname}-devel
%doc README
%dir %{_includedir}/glcddrivers/
%dir %{_includedir}/glcdgraphics/
%dir %{_includedir}/glcdskin/
%{_includedir}/glcddrivers
%{_includedir}/glcdgraphics
%{_includedir}/glcdskin
%{_libdir}/libglcddrivers.so
%{_libdir}/libglcdgraphics.so
%{_libdir}/libglcdskin.so

%files -n glcdgraphics
%doc README
%license COPYING
%{_libdir}/libglcdgraphics.so.2*

%files -n glcdskin
%doc README
%license COPYING
%{_libdir}/libglcdskin.so.2*

%files -n graphlcd-common
%doc README HISTORY docs
%license COPYING
%config(noreplace) %{_sysconfdir}/graphlcd.conf
%{_udevrulesdir}/*-%{name}.rules

%files -n graphlcd-tools
%doc README docs/README.*
%license COPYING
%{_bindir}/*


%changelog
* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-2
- Rebuilt for new VDR API version

* Sat Aug 15 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-6
- add compiler macro for armv7hl to patch graphlcd-base-no-io.h.patch fixes (BZ#1735312)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-3
- Add %%{name}-no-io.h.patch

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-2
- Avoid unintentional soname bump, be more specific
- Use %%global instead of %%define unless justified
- Install COPYING file as %%license
- License is GPLv2+, not GPL+

* Sat Nov 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sat Nov 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-2
- Add %%{name}-Improved-trim-function.patch

* Tue Nov 06 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- Initial package
