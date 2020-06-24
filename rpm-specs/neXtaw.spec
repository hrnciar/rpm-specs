Summary:        Modified version of the Athena Widgets with N*XTSTEP appearance
Name:           neXtaw
Version:        0.15.1
Release:        33%{?dist}

URL:            http://siag.nu/neXtaw/
Source0:        http://siag.nu/pub/neXtaw/%{name}-%{version}.tar.gz
# Upstream has been dead since circa 2003, so no patches have been sent.
# Fix an ANSCI C strict aliasing violation
Patch0:         %{name}-alias.patch
# Add missing includes
Patch1:         %{name}-header.patch
# Enable aarch64 support.
Patch2:         %{name}-aarch64.patch
License:        MIT

BuildRequires:  gcc
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libXmu-devel

%description
neXtaw is a replacement library for the Athena (libXaw) widget set. It
is based on Xaw3d, by Kaleb Keithley and is almost 100% backward
compatible with it. Its goal is to try to emulate the look and feel of
the N*XTSTEP GUI.

%package        devel
Summary:        Development files for the neXtaw library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libXmu-devel%{?_isa}
Requires:       libXt-devel%{?_isa}

%description devel
neXtaw is a replacement library for the Athena (libXaw) widget set. It
is based on Xaw3d, by Kaleb Keithley and is almost 100% backward
compatible with it. Its goal is to try to emulate the look and feel of
the N*XTSTEP GUI. This package contains the development files of the
neXtaw library.


%prep
%setup -q
%patch0
%patch1
%patch2
f=README ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; touch -r $f.utf8 $f; mv $f.utf8 $f


%build
%configure --disable-static --disable-dependency-tracking \
    --x-libraries=%{_libdir}
make %{?_smp_mflags}


%install
rm -rf __docs
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
cp -a doc __docs
rm __docs/{Makefile*,TODO,app-defaults/Makefile*}


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README TODO __docs/*
%license COPYING
%{_libdir}/libneXtaw.so.*

%files devel
%{_includedir}/X11/neXtaw/
%{_libdir}/libneXtaw.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.15.1-23
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 0.15.1-19
- Add -alias patch to fix a strict aliasing violation
- Add -header patch to supply missing function prototypes
- Add -aarch64 patch to enable building on aarch64 platforms (bz 926230)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 0.15.1-16
- Rebuild for GCC 4.7
- Remove unnecessary spec file elements (BuildRoot, etc.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-12
- Include more docs, convert README to UTF-8.

* Mon Aug  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-11
- License: MIT

* Mon Aug 28 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-10
- Rebuild.

* Sun Jun  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-9
- Fix linkage on lib64 archs.
- Drop static lib build option.

* Mon Feb 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-8
- Rebuild.

* Fri Nov 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-7
- Adapt to modular X11 packaging.
- Don't ship static libraries by default.
- Build with dependency tracking disabled.
- Use "rm" instead of %%exclude.
- Specfile cleanups.

* Sat Jun 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-6
- Rebuild.

* Sun Jun 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-5
- Require X devel in -devel.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.15.1-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.15.1-2
- rebuilt

* Thu Oct  2 2003 Dams <anvil[AT]livna.org> 0:0.15.1-0.fdr.1
- Updated to 0.15.1
- Removed marker after scriptlets

* Tue Sep  2 2003 Dams <anvil[AT]livna.org> 0:0.15.0-0.fdr.1
- Updated to 0.15.0

* Thu May  8 2003 Dams <anvil[AT]livna.org> 0:0.14.0-0.fdr.3
- Modified BuildRoot
- Modified defattr
- Added doc files
- Buildroot -> RPM_BUILD_ROOT
- Added post/postun scriptlets
- Exclude ".la" files.
- Added missing epoch in -devel Requires.
- Added missing BuildRequires

* Mon Mar 31 2003 Dams <anvil[AT]livna.org> 0:0.14.0-0.fdr.2
- Added Epoch

* Tue Mar 25 2003 Dams <anvil[AT]livna.org> 0.fdr.1
- modified spec according to fedora template

* Sat Feb 22 2003 Dams <anvil[AT]livna.org>
- Initial build.
