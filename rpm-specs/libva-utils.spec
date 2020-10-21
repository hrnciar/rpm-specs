#global pre_release .pre1

Name:		libva-utils
Version:	2.9.1
Release:	1%{?dist}
Summary:	Tools for VAAPI (including vainfo)
License:	MIT and BSD
URL:		https://github.com/intel/libva-utils
Source0:	%{url}/archive/%{version}%{?pre_release}/%{name}-%{version}%{?pre_release}.tar.gz

BuildRequires:  libtool
BuildRequires:  gcc-c++

BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
%{!?_without_wayland:
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client) >= 1
BuildRequires:  pkgconfig(wayland-scanner) >= 1
}

%description
The libva-utils package contains tools that are provided as part
of libva, including the vainfo tool for determining what (if any)
libva support is available on a system.


%prep
%autosetup -p1 -n %{name}-%{version}%{?pre_release}
autoreconf -vif


%build
%configure --disable-static \
%{?_without_wayland:--disable-wayland}

%make_build


%install
%make_install


%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_bindir}/vainfo
%{_bindir}/loadjpeg
%{_bindir}/jpegenc
%{_bindir}/avcenc
%{_bindir}/avcstreamoutdemo
%{_bindir}/h264encode
%{_bindir}/hevcencode
%{_bindir}/mpeg2vldemo
%{_bindir}/mpeg2vaenc
%{_bindir}/putsurface
%{_bindir}/sfcsample
%{_bindir}/vavpp
%{_bindir}/vp8enc
%{_bindir}/vp9enc
%{_bindir}/vppblending
%{_bindir}/vppchromasitting
%{_bindir}/vppdenoise
%{_bindir}/vppscaling_csc
%{_bindir}/vppscaling_n_out_usrptr
%{_bindir}/vppsharpness
%{!?_without_wayland:%{_bindir}/putsurface_wayland}


%changelog
* Sun Oct 11 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Sun Sep 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Wed Sep 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.9.0-0.1.pre1
- Update to 2.9.0.pre1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Thu Apr 02 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.7.1-1
- Update to 2.7.1

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.6.0-1
- Update to 2.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Mon Sep 23 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Michael Cronenworth <mike@cchtml.com> - 2.4.0-1
- Update to 2.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jun 02 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.1-0.1.pre1
- Update to 2.1.1.pre1-20180601

* Mon Mar 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-2
- Switch to github.com/intel URL

* Mon Feb 12 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.3-1
- Update to 1.8.3

* Tue May 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Mon Apr 10 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Fri Mar 31 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.8.0-1
- Initial spec file for libva-utils

