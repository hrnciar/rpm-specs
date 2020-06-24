Name:		libfep
Version:	0.1.0
Release:	15%{?dist}
Summary:	Library to implement FEP (front end processor) on ANSI terminals

License:	BSD and GPLv3+
URL:		http://github.com/ueno/libfep
Source0:	https://github.com/ueno/libfep/releases/download/%{version}/%{name}-%{version}.tar.gz

# FIXME switch to libgee-0.8 once this package is ready for the new libgee API
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	gobject-introspection-devel
BuildRequires:	vala

%description
The libfep project aims to provide a server and a library to implement
input method FEP (front end processor), running on ANSI compliant
terminals.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
# needed to regenerate GIR
GIO_LIBS=`pkg-config gio-2.0 gmodule-2.0 --libs`
export GIO_LIBS
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'
cp -p fep/README README.fep


%ldconfig_scriptlets


%files
%doc README README.fep COPYING fep/COPYING.BSD ChangeLog
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Fep*.typelib
%{_bindir}/fep*
%{_mandir}/man1/fep*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Fep*.gir
%{_datadir}/vala/vapi/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.1.0-13
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.0-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun  4 2014 Daiki Ueno <dueno@redhat.com> - 0.1.0-1
- new upstream release
- drop intltool from BR

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Daiki Ueno <dueno@redhat.com> - 0.0.9-1
- new upstream release
- drop no_gets patch

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.0.8-3
- Fix gets call for glibc-2.16 changes

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Daiki Ueno <dueno@redhat.com> - 0.0.8-1
- new upstream release

* Thu Mar 29 2012 Daiki Ueno <dueno@redhat.com> - 0.0.7-1
- new upstream release

* Tue Mar  6 2012 Daiki Ueno <dueno@redhat.com> - 0.0.6-1
- new upstream release

* Wed Feb 15 2012 Daiki Ueno <dueno@redhat.com> - 0.0.5-1
- new upstream release

* Fri Feb 10 2012 Daiki Ueno <dueno@redhat.com> - 0.0.4-1
- new upstream release
- install manpages
- add ChangeLog to %%doc and drop empty %%doc from -devel subpackage
- single quote {} of the find command
- drop vala-tools from BR

* Fri Feb  3 2012 Daiki Ueno <dueno@redhat.com> - 0.0.1-1
- initial packaging for Fedora

