Name:           ffcall
Version:        2.2
Release:        3%{?dist}
Summary:        Libraries for foreign function call interfaces

License:        GPLv2+
URL:            http://www.gnu.org/software/libffcall/
Source0:        https://ftp.gnu.org/gnu/libffcall/lib%{name}-%{version}.tar.gz
Patch0:         configure.patch

BuildRequires:  gcc
BuildRequires:  gnulib-devel

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.  The four
packages are:
 - avcall: calling C functions with variable arguments
 - vacall: C functions accepting variable argument prototypes
 - trampoline: closures as first-class C functions
 - callback: closures with variable arguments as first-class C functions
   (a reentrant combination of vacall and trampoline)

%package devel
Summary:        Files needed to develop programs with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed to develop programs with %{name}.

%package static
Summary:        Static libraries for foreign function call interfaces
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for foreign function call interfaces.


%prep
%setup -q -n lib%{name}-%{version}
%patch0 -p1

%build
%configure CFLAGS="%{optflags} -fno-strict-aliasing"

# Build the actual library
make # %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}
make install DESTDIR=$RPM_BUILD_ROOT
rm -fr $RPM_BUILD_ROOT%{_datadir}/html
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Fix permissions
chmod a+x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*

# Advertise supported architectures
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
cat > $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.%{name} << EOF
# arches that ffcall supports
%%ffcall_arches %{ffcall_arches}
EOF

# Fix man pages with overly generic names (bz 800360)
pushd $RPM_BUILD_ROOT%{_mandir}/man3
for page in *; do
  mv $page %{name}-$page
done
popd


%files
%license COPYING
%doc README NEWS
%{_libdir}/lib*.so.*

%files devel
%doc avcall/avcall.html
%doc callback/callback.html
%doc callback/trampoline_r/trampoline_r.html
%doc trampoline/trampoline.html
%doc vacall/vacall.html
%{_includedir}/*
%{_libdir}/lib*.so
%{_mandir}/man*/*
%{_rpmconfigdir}/macros.d/macros.%{name}

%files static
%{_libdir}/*.a


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 2.2-2
- Fix autoconf generated configure tests that are compromised
  by LTO.

* Mon Aug 26 2019 Jerry James <loganjerry@gmail.com> - 2.2-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jerry James <loganjerry@gmail.com> - 2.1-1
- New upstream release
- Drop ExclusiveArch; all Fedora arches supported

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Jerry James <loganjerry@gmail.com> - 2.0-1
- New upstream release
- Make -devel and -static subpackages

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Jerry James <loganjerry@gmail.com> - 1.13-3
- Update to the final 1.13 release
- Drop patches and workarounds for problems fixed upstream

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 1.13-2
- Fix missing symbols in the i386 build

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 1.13-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Jerry James <loganjerry@gmail.com> - 1.12-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-18.20120424cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Jerry James <loganjerry@gmail.com> - 1.10-17.20120424cvs
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-16.20120424cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-15.20120424cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Jerry James <loganjerry@gmail.com> - 1.10-14.20120424cvs
- Update location of rpm macro file for rpm >= 4.11

* Fri Sep  6 2013 Jerry James <loganjerry@gmail.com> - 1.10-13.20120424cvs
- Update -arm patch to really use the EABI and hopefully fix clisp

* Wed Sep  4 2013 Jerry James <loganjerry@gmail.com> - 1.10-12.20120424cvs
- Add -arm patch to fix clisp build failure

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-11.20120424cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Jerry James <loganjerry@gmail.com> - 1.10-10.20120424cvs
- Update to CVS 20120424
- List all architectures supported by this package (bz 925335)
- Rename man pages to avoid conflicts (bz 800360)
- Add Provides: ffcall-static

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-9.20100903cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-8.20100903cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 1.10-7.20100903cvs
- Clean out prebuilt object files
- Add trampoline patch to force use of mmap() to get executable memory

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.10-6.20100903cvs
- Update to CVS 20100903
- Minor spec file cleanups

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5.20080704cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4.20080704cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3.20080704cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Jochen Schmitt <Jochen herr-schmitt de> - 1.10-2.20080704cvs.1
- Fix -FPIC issue (BZ #475112)

* Fri Jul  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.10-2.20080704cvs
- update to cvs 20080704
- support for ppc64

* Mon Feb 25 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.10-1
- first Fedora release
