Name:           libvdpau
Version:        1.4
Release:        3%{?dist}
Summary:        Wrapper library for the Video Decode and Presentation API
License:        MIT
URL:            https://freedesktop.org/wiki/Software/VDPAU/
Source0:        https://gitlab.freedesktop.org/vdpau/libvdpau/-/archive/libvdpau-%{version}/libvdpau-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  meson
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires:  tex(latex)
%else
BuildRequires:  tetex-latex
%endif
BuildRequires:  xorg-x11-proto-devel

%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an
interface to video decode acceleration and presentation hardware present in
modern GPUs.

%package        trace
Summary:        Trace library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
Supplements:    %{name}-debuginfo%{?_isa}
%endif

%description    trace
The %{name}-trace package contains trace library for %{name}.

%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch
Provides:       libvdpau-docs = %{version}-%{release}
Obsoletes:      libvdpau-docs < 0.6-2

%description    docs
The %{name}-docs package contains documentation for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#Multilibs trace
Requires:       %{name}-trace%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1 -n libvdpau-libvdpau-1.4-c3d1a9dbafdfe6144ff474d0d523dc01b068750f


%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete
# Let %%doc macro create the correct location in the rpm file, creates a
# versioned docdir in <= f19 and an unversioned docdir in >= f20.
rm -fr %{buildroot}%{_docdir}
mv %{_vpath_builddir}/doc/html html


%ldconfig_scriptlets


%files
%doc AUTHORS
%license COPYING
%config(noreplace) %{_sysconfdir}/vdpau_wrapper.cfg
%{_libdir}/*.so.*
%dir %{_libdir}/vdpau/

%files trace
%{_libdir}/vdpau/%{name}_trace.so*

%files docs
%doc html

%files devel
%{_includedir}/vdpau/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vdpau.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4-2
- Rebuilt

* Fri Apr 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4-1
- Update to 1.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3-1
- Update to 1.3
- Switch to meson build
- Use an easier URL for source

* Wed Aug 21 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.2-3
- Fetch VP9 support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.2-1
- Update to 1.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-11
- Apply patches from upstream

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-10
- Add missng cc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-8
- Move libvdpau_trace to trace sub-package
- Spec file clean-up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-2
- Backport current patches
- Switch to new upstream git repository on freedesktop.org

* Tue Sep 01 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-1
- Update to 1.1.1
  Security fix for CVE-2015-5198, CVE-2015-5199, CVE-2015-5200

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.1-1
- Update to 1.1

* Tue Mar 10 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.0-1
- Update to 1.0

* Fri Dec 19 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.9-1
- Update to 0.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.8-1
- Update to 0.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Simone Caronni <negativo17@gmail.com> - 0.7-1
- Update to 0.7; adds prime support.

* Wed Jul 31 2013 Simone Caronni <negativo17@gmail.com> - 0.6-2
- Enable documentation by default.
- Clean up spec file a bit; remove el5 tags.
- Let %%doc find the proper location for the documentation.

* Mon Feb 04 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6-1
- Update to 0.6

* Wed Sep 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5-1
- Update to 0.5

* Sun Aug 19 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.4.1-9
- Added flash workarounds

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-7
- Fetch current backport

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-3
- Rebuilt for gcc bug 634757

* Sun Sep 12 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Sat Mar 13 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.4-1
- Update to 0.4

* Sun Nov 22 2009 kwizart < kwizart at gmail.com > - 0.3-1
- Update to 0.3
- Create docs sub-package
- Allow --without docs conditional

* Thu Sep 17 2009 kwizart < kwizart at gmail.com > - 0.2-1
- Update to 0.2
- Disable ExclusiveArch

* Mon Sep  7 2009 kwizart < kwizart at gmail.com > - 0.1-0.6.20090904git
- Update to gitdate 20090904git

* Wed Sep  2 2009 kwizart < kwizart at gmail.com > - 0.1-0.5git20090902
- Update to gitdate 20090902 with merged patches

* Mon Jun 15 2009 kwizart < kwizart at gmail.com > - 0.1-0.3git20090318
- Add missing -ldl at link time

* Sun Mar 22 2009 kwizart < kwizart at gmail.com > - 0.1-0.2git20090318
- Backport fix thread_2

* Fri Mar  6 2009 kwizart < kwizart at gmail.com > - 0.1-0.1git20090318
- Initial spec file

