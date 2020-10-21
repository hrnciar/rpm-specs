%global pname abGate
Name:           lv2-abGate
Version:        1.1.9
Release:        3%{?dist}
Summary:        An LV2 Noise Gate

License:        GPLv3+
URL:            https://abgate.sourceforge.io/
Source0:        https://github.com/antanasbruzas/%{pname}/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Patch0:         Makefile.patch
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  gtkmm24-devel
Requires:       lv2 >= 1.8.1

%description
A Noise Gate plugin 

%prep
%autosetup -p 1 -n %{pname}-%{version}

# Do not build Qt5 GUI for now
rm -rf abGateQt

# Fix plugin path
sed -i -e "s|/usr/lib/lv2|%{_libdir}/lv2|g" plugin_configuration.h

%build
%set_build_flags
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} INSTALL_DIR=%{buildroot}/%{_libdir}/lv2

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/%{pname}.lv2


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.1.9-1
- Version 1.1.9

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.1.3-13
- Rework sed-pattern to modify Makefile and plugin_configuration.h (Fix FTBFS).
- Add %%license.
- Eliminate "File listed twice" warnings.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1.3-6
- Correct merge typo in spec file

* Fri May 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1.3-5
- Build against new lv2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for c++ ABI breakage

* Fri Jan 20 2012 Dan Horák <dan[at]danny.cz> 1.1.3-3
- fix build on non-x86 64-bit arches

* Fri Jan 6 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1.3-2
- Removed lv2config

* Mon Oct 31 2011 Brendan Jones <brendan.jones.it@gmail.com> 1.1.3-1
- Initial build

