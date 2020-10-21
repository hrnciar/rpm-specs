Name:           libquvi
Version:        0.9.4
Release:        18%{?dist}
Summary:        A cross-platform library for parsing flash media stream
License:        AGPLv3+
URL:            http://quvi.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/quvi/0.9/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  lua-devel lua-socket
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel libgcrypt-devel libproxy-devel libquvi-scripts
BuildRequires:  doxygen
Requires:       libquvi-scripts

%if 0%{?fedora}
# From rhughes-f20-gnome-3-12 copr
Obsoletes:      compat-libquvi092 < 0.9.4
%endif

%description
Libquvi is a cross-platform library for parsing flash media stream
URLs with C API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      quvi-devel <= 0.2.19
Provides:       quvi-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags} V=1
make doc

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README 
%{_libdir}/%{name}-0.9-%{version}.so
%{_mandir}/man3/%{name}.3*

%files devel
%{_includedir}/quvi-0.9
%{_libdir}/%{name}-0.9.so
%{_libdir}/pkgconfig/%{name}-0.9.pc
%{_mandir}/man7/quvi-object.7*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Bastien Nocera <bnocera@redhat.com> 0.9.4-6
- Rebuild for new lua

* Sun Nov 16 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.4-5
- Obsolete compat-libquvi092 from rhughes-f20-gnome-3-12 copr

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 0.9.4-2
- Rebuild for new libgcrypt

* Tue Nov 26 2013 Christopher Meng <rpm@cicku.me> - 0.9.4-1
- New version.

* Mon Aug 26 2013 Christopher Meng <rpm@cicku.me> - 0.9.2-1
- New version.
- SPEC Cleanup.
- New version.
- License changed to AGPL.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.1-1
- Update to 0.4.1

* Sun Dec 11 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-5
- Fix Obsoletes version

* Wed Oct 19 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-4
- Remove the pkgconfig require for the devel package

* Tue Oct 11 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-3
- Fix BuilRequires

* Sun Oct 09 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-2
- Fix requires

* Sat Oct 08 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-1
- Initial build
