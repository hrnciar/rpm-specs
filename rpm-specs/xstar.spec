Name:           xstar
Version:        2.2.0
Release:        23%{?dist}
Summary:        Program that simulates the movement of stars

License:        GPLv2+
URL:            http://www.schlitt.net/xstar/
Source0:        http://www.schlitt.net/xstar/%{name}.tar.gz
Source10:	%{name}.conf
Source11:	%{name}.xml

BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  imake
BuildRequires:  libXext-devel

%description
XStar is a Unix program that simulates the movement of stars. It starts by
putting a bunch of stars on the screen, and then it lets the inter-body
gravitational forces move the stars around. The result is a lot of neat
wandering paths, as the stars interact and collide.

Along with the program, there is a fairly large document that explains the
N-Body problem in a fair amount of detail. It doesn't get into the gory
details of the "real" N-body solvers, but it does give you an overview of
the techniques they use.

%package	xscreensaver
Summary:	XScreenSaver support for %{name}
Requires:	%{name} = %{version}-%{release}
Requires(post):		xscreensaver-base
Requires(postun):	xscreensaver-base

%description	xscreensaver
This package contains the files needed to use %{name} with XScreenSaver.


%prep
%setup -q


%build
xmkmf
make MANSRCSUFFIX=1 CC="%{__cc} $RPM_OPT_FLAGS" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install install.man MANSRCSUFFIX=1 DESTDIR=$RPM_BUILD_ROOT

# XScreenSaver related
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xscreensaver/hacks.conf.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xscreensaver/config
install -c -p -m 644 %{SOURCE10} \
	$RPM_BUILD_ROOT%{_datadir}/xscreensaver/hacks.conf.d/
install -c -p -m 644 %{SOURCE11} \
	$RPM_BUILD_ROOT%{_datadir}/xscreensaver/config/


%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
	%{_sbindir}/update-xscreensaver-hacks || :
fi


%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
	%{_sbindir}/update-xscreensaver-hacks || :
fi


%files
%{_bindir}/xstar
%{_mandir}/man1/xstar.1*
%doc n-body.ps COPYING README README.xgrav

%files xscreensaver
%{_datadir}/xscreensaver/config/%{name}.xml
%{_datadir}/xscreensaver/hacks.conf.d/%{name}.conf


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.2.0-19
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.0-3
- Autorebuild for GCC 4.3

* Mon Dec 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 2.2.0-2
- Support XScreenSaver
- Honor Fedora specific compilaton flags

* Mon Dec 17 2007 Lubomir Kundrak <lkundrak@redhat.com> 2.2.0-1
- Initial package
