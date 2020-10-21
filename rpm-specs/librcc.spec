Name:           librcc
Version:        0.2.12
Release:        17%{?dist}
Summary:        RusXMMS Charset Conversion Library

License:        LGPLv2+
URL:            http://rusxmms.sourceforge.net
Source0:        http://dside.dyndns.org/files/rusxmms/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  enca-devel
%if 0%{?fedora} || 0%{?rhel} < 8
BuildRequires:  gtk+-devel
%endif
BuildRequires:  gtk2-devel
# RHEL has no gtk3 and libguess
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:  gtk3-devel
BuildRequires:  libguess-devel
%endif
BuildRequires:  aspell-devel
BuildRequires:  librcd-devel

%description
The Abilities of LibRCC Library

- Language Autodetection.
- On the fly translation between languages, using online-services!
- Encoding Autodetection for most of European Languages.
- Support for encoding detection plugins (besides Enca and LibRCD)
- Recoding/translation of multi-language playlists!
- Cache to speed-up re-recoding.
- Possibility to configure new languages and encodings.
- Shared configuration file. For example mentioned TagLib and LibID3
  patches do not have their own user interface, but will utilize the
  same recoding configuration as XMMS.
- As well the separate program for configuration adjustment is
  available.
- GTK2 UI Library: you can add properties page to your GTK application
  with 3 lines of code.
- Menu localization opportunity.

%if 0%{?fedora} || 0%{?rhel} < 8
%package        gtk+
Summary:        RusXMMS Encoding Conversion Library GTK+ bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk+
The %{name}-gtk+ package contains GTK+ bindings for RusXMMS Encoding
Conversion Library
%endif

%package        gtk2
Summary:        RusXMMS Encoding Conversion Library GTK2 bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk2
The %{name}-gtk2 package contains GTK2 bindings for RusXMMS Encoding
Conversion Library

%if 0%{?fedora} || 0%{?rhel} > 6
%package        gtk3
Summary:        RusXMMS Encoding Conversion Library GTK3 bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk3
The %{name}-gtk3 package contains GTK3 bindings for RusXMMS Encoding
Conversion Library
%endif

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} < 8
Requires:       %{name}-gtk+%{?_isa} = %{version}-%{release}
%endif
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 6
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

# fix permissions
chmod 644 examples/rusxmms_cache.pl

%build
# LDFLAGS to prevent rpmlint W: unused-direct-shlib-dependency
LDFLAGS="-Wl,--as-needed $RPM_LD_FLAGS" %configure --disable-static --disable-libtranslate --disable-bdb

# To remove hardcoded rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete


%ldconfig_scriptlets

%if 0%{?fedora} || 0%{?rhel} < 8
%ldconfig_scriptlets gtk+
%endif

%ldconfig_scriptlets gtk2

%if 0%{?fedora} || 0%{?rhel} > 6
%ldconfig_scriptlets gtk3
%endif

%files
%doc COPYING NEWS AUTHORS README
%{_libdir}/librcc.so.*
%{_libdir}/librccui.so.*
%{_libdir}/rcc

%if 0%{?fedora} || 0%{?rhel} < 8
%files gtk+
%{_libdir}/librccgtk.so.*
%endif

%files gtk2
%{_libdir}/librccgtk2.so.*

%if 0%{?fedora} || 0%{?rhel} > 6
%files gtk3
%{_libdir}/librccgtk3.so.*
%endif

%files devel
%doc examples
%{_includedir}/librcc*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/librcc.so
%{_libdir}/librccui.so
%if 0%{?fedora} || 0%{?rhel} < 8
%{_libdir}/librccgtk.so
%endif
%{_libdir}/librccgtk2.so
%if 0%{?fedora} || 0%{?rhel} > 6
%{_libdir}/librccgtk3.so
%endif

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Leigh Scott <leigh123linux@gmail.com> - 0.2.12-15
- fix up for epel7 and 8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Ivan Romanov <drizt@land.ru> - 0.2.12-3
- dropped Group tag

* Tue Nov 19 2013 Ivan Romanov <drizt@land.ru> - 0.2.12-2
- do not buil gtk3 libs for RHEL
- no libguess support for RHEL

* Mon Nov 18 2013 Ivan Romanov <drizt@land.ru> - 0.2.12-1
- updated to 0.2.12
- added libguess and librcd for greater autodetection accuracy
- use %%make_install macros
- new source tarball url

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jan 30 2013 Ivan Romanov <drizt@land.ru> - 0.2.10-1
- updated to 0.2.10
- dropped patches (applied by upstream)
- new -gkt+ and -gtk3 subpackage

* Sat Nov  3 2012 Ivan Romanov <drizt@land.ru> - 0.2.9-3
- added LDFLAGS for %%configure

* Fri Nov  2 2012 Ivan Romanov <drizt@land.ru> - 0.2.9-2
- corrected Source0
- add patch1
- explicity turn off libtranslate and db4 support
- added aspell to BR

* Mon Oct 29 2012 Ivan Romanov <drizt@land.ru> - 0.2.9-1
- initial version of package
