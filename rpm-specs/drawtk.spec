Name:		drawtk
Version:	2.0
Release:	10%{?dist}
Summary:	A C library to perform efficient 3D drawings

License:	LGPLv3+
URL:		http://cnbi.epfl.ch/software/drawtk.html

# source code is maintained in github repo:
# https://github.com/nbourdau/drawtk
# however the latest released tarball was lost, so it is restored
# from alioth repo containing exactly the same files in the 'upstream' branch:
# git://anonscm.debian.org/pkg-exppsy/drawtk.git
# git archive --prefix drawtk-2.0/ upstream/2.0 | xz > ../drawtk-2.0.tar.xz
Source0:	%{name}-%{version}.tar.xz
Patch0:		drawtk-fix-include.patch

BuildRequires:	gcc
BuildRequires:	SDL-devel
BuildRequires:	freetype-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freeimage-devel

%description
drawtk provides a C library to perform efficient 2D drawings. The drawing is
done by OpenGL which allow us fast and nice rendering of basic shapes, text,
images and video (file, webcam, network). It has been implemented as a thin
layer that hides the complexity of the OpenGL library.


%package devel
Summary:	A C library to perform efficient 3D drawings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL-devel
Requires:	freetype-devel
Requires:	gstreamer-devel
Requires:	gstreamer-plugins-base-devel
Requires:	fontconfig-devel
Requires:	freeimage-devel

%description devel
Development files for drawtk library.


%prep
%setup -q
%if 0%{?fedora} && 0%{?fedora} < 24
%patch0 -p1
%endif


%build
%configure
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la


%ldconfig_scriptlets


%files
%license COPYING
%{_libdir}/libdrawtk.so.*


%files devel
%doc %{_docdir}/%{name}
%{_libdir}/libdrawtk.so
%{_libdir}/pkgconfig/drawtk.pc
%{_includedir}/*.h
%{_mandir}/man3/*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 6 2015 Dmitry Mikhirev <mikhirev@gmail.com> 2.0-1
- Initial package
