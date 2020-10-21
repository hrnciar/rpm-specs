Name:           vdpauinfo
Version:        1.0
Release:        16%{?dist}
Summary:        Tool to query the capabilities of a VDPAU implementation

License:        MIT
URL:            https://gitlab.freedesktop.org/vdpau/vdpauinfo
Source0:        %{url}/uploads/a62b87300dff4ad0ac2d4dedb832ec13/vdpauinfo-%{version}.tar.gz
Patch0:         %{url}/commit/edb1f9315df03f904b310efd2ba02d1e425a33f7.patch
Patch1:         %{url}/commit/8f586fe834a8f485fcf96e36656ce02f8b05a2ff.patch

BuildRequires:  gcc-c++
BuildRequires:  libvdpau-devel >= 1.0


%description
Tool to query the capabilities of a VDPAU implementation.

%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install



%files
%license COPYING
%{_bindir}/vdpauinfo


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.0-14
- Backport "Add support for VP9 in vdpauinfo"

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.0-12
- Switch to gitlab
- Spec refresh
- Backport "names for the new 4:4:4 surface formats"

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.0-2
- Rebuilt for libvdpau-1.1

* Thu Mar 12 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.0-1
- Update to 1.0

* Fri Dec 19 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.9-0.1
- Update to 0.9

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1-1
- Update to 0.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 17 2009 kwizart < kwizart at gmail.com > - 0.0.6-2
- Tagged archive compatible with livdpau 0.2

* Sun Mar 22 2009 kwizart < kwizart at gmail.com > - 0.0.6-1
- Initial package
