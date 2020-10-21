Name:           lv2-mdala-plugins
Version:        1.2.4
Release:        2%{?dist}
Summary:        A collection of LV2 plugins ported from the MDA VST plugins

# BSD for waflib
License:        GPLv3+ and BSD
URL:            https://drobilla.net
Source0:        https://download.drobilla.net/mda-lv2-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
Requires:       lv2

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%autosetup -n mda-lv2-%{version}
# Correct unversioned python shebang
sed -i 's|python|python3|' waf
# Correct build flags
export OPT_WAF=$(echo %{optflags} | sed "s| |', '|g")
sed -i "s|'lvz/wrapper.cpp'],|'lvz/wrapper.cpp'],\ncxxflags = ['$OPT_WAF'],|" wscript

%build
./waf configure -v --prefix=%{_prefix} --libdir=%{_libdir}
./waf -v build %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}

%files
%doc NEWS README.md
%license COPYING
%{_libdir}/lv2/mda.lv2/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu May 17 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-2
- correct CFLAGS, remove encoding script

* Thu May 17 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-1
- Update to 1.0.0 

* Thu Nov 24 2011 Brendan Jones <brendan.jones.it@gmail.com> 0.0.0-0.3.svn3580
- Remove README from encoding fix and remove obsolete buildroot tag

* Tue Nov 15 2011 Brendan Jones <brendan.jones.it@gmail.com> 0.0.0-0.2.svn3580
- Correct files

* Mon Oct 31 2011 Brendan Jones <brendan.jones.it@gmail.com> 0.0.0-0.1.svn3580
- Initial build

